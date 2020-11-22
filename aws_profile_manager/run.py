#!/usr/bin/python3

import sys
import argparse
import logging
from aws_profile_manager import Common, Switch

from aws_profile_manager._version import __version__

def setup_logging(quiet: bool, verbose: bool):
    ''' Function is setting logging configuration '''

    if verbose:
        logging_level = logging.INFO
    elif quiet:
        logging_level = logging.ERROR
    else:
        logging_level = logging.WARNING
    logging.basicConfig(format='%(message)s', level=logging_level)

def parse_arguments():
    ''' Function allows to parse arguments from the line input and check if all
    of them are entered correctly '''

    parser = argparse.ArgumentParser(
        description='Manage AWS profile in a fast way',
        epilog='Find more at https://github.com/99stealth/aws-profile-switcher'
    )
    parser.add_argument('--version', action='version',
                        version='%(prog)s \033[0;32m{version}\033[0;0m'.format(version=__version__))

    args = parser.parse_args()
    return args

def main():
    common = Common()
    switch = Switch()

    args = parse_arguments()
    setup_logging(quiet=False, verbose=False)
    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    new_default_profile_name = None
    if "default" not in all_profiles:
        logging.warning("There is no [default] profile in your {}/.aws/credentials. It will be automatically created".format(users_home))
    else:
        defaults_backup = switch.get_defaults_backup(all_profiles)
        if defaults_backup:
            logging.warning("Your current default is \033[1m{}\033[0m \n".format(defaults_backup))
        else:
            new_default_profile_name = switch.ask_new_name_for_default_profile(users_home, all_profiles)
            if new_default_profile_name:
                all_profiles = switch.create_backup_for_default(all_profiles, new_default_profile_name)
    new_default = switch.choose_new_default(all_profiles, new_default_profile_name)
    new_profiles_list = common.generate_new_profile_list(all_profiles, new_default)
    common.rewrite_credentials_file(new_profiles_list, users_home)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("\nProcess has been stopped. Interrupted by user")
        sys.exit(1)