#!/usr/bin/python3

from os.path import expanduser
import sys
from typing import Dict
import configparser
import logging


def get_users_home() -> str:
    """ Function returns user's home path """

    return expanduser("~")

def get_all_profiles(users_home: str) -> Dict:
    """ Function receive user's home and return all aws profiles """

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

def get_defaults_backup(profiles: Dict):
    """ Function receives all profiles and looks for duplication of default. 
        It returns default if one is found and None if not """

    for profile in profiles:
        if profile == 'default':
            continue
        if profiles[profile] == profiles['default']:
            return profile
    return None

def ask_new_name_for_default_profile(users_home: str, profiles: Dict):
    print("There is no default profile duplication among all accounts in {}/.aws/credentials".format(users_home))
    while True:
        answer = input("Do you want to make backup of your current [default] profile? [Y/n] ")
        if answer.lower() == "yes" or answer.lower() == "y":
            new_default_name = input("Enter new name for your currnet [default] profile: ")
            if new_default_name in profiles:
                print("Profile with name {} is already exists in {}/.aws/credentials. Try once more".format(new_default_name, users_home))
                continue
            else:
                return new_default_name
        elif answer.lower() == "no" or answer.lower() == "n":
            while True:
                answer = input("Are you sure? Current [default] will be lost [Y/n] ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    return None
                elif answer.lower() == "no" or answer.lower() == "n":
                    break
                else:
                    print("Yes or No?")
        else:
            print("Yes or No?")

def create_backup_for_default(profiles: Dict, new_default_profile_name: str) -> Dict:
    profiles[new_default_profile_name] = profiles["default"]
    return profiles

def choose_new_default(profiles: Dict, new_default_profile_name: str) -> str:
    i = 1
    counter = {}
    for profile in profiles:
        if profile == "default" or profile == new_default_profile_name:
            continue
        counter[i] = profile
        i += 1
    for c in counter:
        print("{}: {}".format(c, counter[c]))
    answer = input("\nChoose a number of the account to which you want to switch your current default: ")
    return counter[int(answer)]

def generate_new_profile_list(profiles: Dict, new_default: str) -> Dict:
    new_profile_list = {"default": {}}
    for item in profiles[new_default]:
        new_profile_list["default"][item] = profiles[new_default][item]
    profiles.pop('default', None)
    for item in profiles:
        new_profile_list[item] = profiles[item]
    return new_profile_list

def rewrite_credentials_file(new_profiles_list: Dict, users_home: str):
    config = configparser.ConfigParser()
    for profile in new_profiles_list:
        config[profile] = new_profiles_list[profile]
    config.write(open('{}/.aws/credentials'.format(users_home), 'w'))

def setup_logging(quiet: bool, verbose: bool):
    ''' Function is setting logging configuration '''

    if verbose:
        logging_level = logging.INFO
    elif quiet:
        logging_level = logging.ERROR
    else:
        logging_level = logging.WARNING
    logging.basicConfig(format='%(message)s', level=logging_level)

def main():
    setup_logging(quiet=False, verbose=False)
    users_home = get_users_home()
    all_profiles = get_all_profiles(users_home)
    new_default_profile_name = None
    if "default" not in all_profiles:
        logging.warning("There is no [default] profile in your {}/.aws/credentials. It will be automatically created".format(users_home))
    else:
        defaults_backup = get_defaults_backup(all_profiles)
        if defaults_backup:
            logging.warning("Your current default is \033[1m{}\033[0m \n".format(defaults_backup))
        else:
            new_default_profile_name = ask_new_name_for_default_profile(users_home, all_profiles)
            if new_default_profile_name:
                all_profiles = create_backup_for_default(all_profiles, new_default_profile_name)
    new_default = choose_new_default(all_profiles, new_default_profile_name)
    new_profiles_list = generate_new_profile_list(all_profiles, new_default)
    rewrite_credentials_file(new_profiles_list, users_home)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("\nProcess has been stopped. Interrupted by user")
        sys.exit(1)