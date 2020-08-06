import sys
from os.path import expanduser
from typing import Dict
import configparser

class Common:
    def get_users_home(self) -> str:
        """ Function returns user's home path """

        return expanduser("~")

    def get_all_profiles(self, users_home: str) -> Dict:
        """ Function receive user's home and parses file .aws/credentials.
            It returns all aws profiles and their credentials in dictionary """
    
        profiles = {}
        config = configparser.ConfigParser()
        config.read('{}/.aws/credentials'.format(users_home))
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
        config.write(open('{}/.aws/credentials'.format(users_home), 'w'))