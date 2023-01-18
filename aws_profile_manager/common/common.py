import sys
import re
from os.path import expanduser
from typing import Dict
import configparser
import logging

class Common:
    def get_users_home(self) -> str:
        """ Function returns user's home path """

        return expanduser("~")

    def get_all_profiles(self, users_home: str) -> Dict:
        """ Function receive user's home and parses file .aws/credentials.
            It returns all aws profiles and their credentials in dictionary """
    
        profiles = {}
        config = configparser.ConfigParser()
        config.read(f'{users_home}/.aws/credentials')
        sections = config.sections()
        for section in sections:
            section_items = {}
            for key in config[section]:
                section_items[key] = config[section][key]
            profiles[section] = section_items
        return profiles

    def generate_new_profile_list(self, profiles: Dict, new_default: str) -> Dict:
        """ Function receives list of profiles and name of new default. 
            Function returns regenerated list of profiles with new default """

        new_profile_list = {"default": {}}
        for item in profiles[new_default]:
            new_profile_list["default"][item] = profiles[new_default][item]
        profiles.pop('default', None)
        for item in profiles:
            new_profile_list[item] = profiles[item]
        return new_profile_list

    def rewrite_credentials_file(self, new_profiles_list: Dict, users_home: str):
        """ Function receives new_profile_list and users_home. 
            Function revrites credentials file with updated profiles """

        config = configparser.ConfigParser()
        for profile in new_profiles_list:
            config[profile] = new_profiles_list[profile]
        config.write(open(f'{users_home}/.aws/credentials', 'w'))

    def aws_access_key_id_is_valid(self, aws_access_key_id):
        ''' The method receives the string with AWS Access Key ID and checks if
        it is valid. If everything is in order it will return True otherwise
        it returns False '''

        if re.match('^AK[A-Z0-9]{18}$', aws_access_key_id):
            return True
        return False

    def aws_access_key_id_for_session_token_is_valid(self, aws_access_key_id):
        ''' The method receives the string with AWS Access Key ID and checks if
        it is valid. If everything is in order it will return True otherwise
        it returns False '''

        if re.match('^AS[A-Z0-9]{18}$', aws_access_key_id):
            return True
        return False

    def aws_secret_access_key_is_valid(self, aws_secret_access_key):
        ''' The method receives the string with AWS Secret Access Key and
        checks if it is valid. If everything is in order it will return True
        otherwise it returns False '''

        if re.match('^[A-Za-z0-9+=/]{40}$', aws_secret_access_key):
            return True
        return False

    def choose_profile(self, profiles: Dict, operation: str, skip_profiles=[]) -> str:
        i = 1
        counter = {}
        for profile in profiles:
            if profile in skip_profiles:
                continue
            counter[i] = profile
            i += 1
        for c in counter:
            print(f"{c}: {counter[c]}")
        while True:
            try:
                answer = input(f"\nChoose a number of the profile which you want to {operation}: ")
            except (KeyboardInterrupt, EOFError):
                logging.error("\nProcess has been stopped. Interrupted by user")
                sys.exit(1)
            try:
                return counter[int(answer)]
            except (ValueError, KeyError) as e:
                logging.error(f"Answer \"{answer}\" is not valid. Please provide number from 1 to {len(counter)}")
                logging.debug(e)