#!/usr/bin/python3

from os.path import expanduser
import sys
import configparser
import logging


def get_users_home():
    """ Function returns user's home path """

    return expanduser("~")

def get_all_profiles(users_home):
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

def find_default_profile_among_all(profiles):
    """ Function receives all profiles and looks for duplication of default. 
        It returns default if one is found and None if not """

    for profile in profiles:
        if profile == 'default':
            continue
        if profiles[profile] == profiles['default']:
            return profile
    return None

def new_profile_name_is_among_all_proiles(profiles, new_default_name):
    """ Function receives all profiles and new default name. 
        It returns True if name is already exists in among profiles and False if not """
    return new_default_name in profiles

def get_new_name_for_default_profile(users_home, profiles):
    print("There is no default profile duplication among all accounts in {}/.aws/credentials".format(users_home))
    while True:
        answer = input("Do you want to make backup of your current [default] profile? [Y/n] ")
        if answer.lower() == "yes" or answer.lower() == "y":
            new_default_name = input("Enter new name for your currnet [default] profile: ")
            if new_profile_name_is_among_all_proiles(profiles, new_default_name):
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

def create_backup_for_default(profiles, new_default_profile_name):
    profiles[new_default_profile_name] = profiles["default"]
    return profiles

def choose_new_default(profiles, new_default_profile_name):
    i = 1
    counter = {}
    for profile in profiles:
        if profile == "default" or profile == new_default_profile_name:
            continue
        counter[i] = profile
        i = i + 1
    for c in counter:
        print("{}: {}".format(c, counter[c]))
    answer = input("Choose a number of the account to which you want to switch your current default: ")
    return counter[int(answer)]

def generate_new_profile_list(profiles, new_default):
    profiles.pop('default', None)
    profiles["default"] = {}
    for i in profiles[new_default]:
        profiles["default"][i] = profiles[new_default][i]
    return profiles

def rewrite_credentials_file(new_profiles_list, users_home):
    config = configparser.ConfigParser()
    for profile in new_profiles_list:
        config[profile] = new_profiles_list[profile]
    config.write(open('{}/.aws/credentials'.format(users_home), 'w'))

def main():
    users_home = get_users_home()
    profiles = get_all_profiles(users_home)
    default_profile_name = find_default_profile_among_all(profiles)
    if not default_profile_name:
        new_default_profile_name = get_new_name_for_default_profile(users_home, profiles)
        if new_default_profile_name:
            profiles = create_backup_for_default(profiles, new_default_profile_name)
    else:
        new_default_profile_name = None
    new_default = choose_new_default(profiles, new_default_profile_name)
    new_profiles_list = generate_new_profile_list(profiles, new_default)
    rewrite_credentials_file(new_profiles_list, users_home)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("\nProcess has been stopped. Interrupted by user")
        sys.exit(1)