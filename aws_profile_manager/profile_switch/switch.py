import sys
from typing import Dict
import logging

class Switch:
    def get_defaults_backup(self, profiles: Dict):
        """ The function receives all profiles and looks for duplication of default. 
            It returns default if one is found and None if not """

        for profile in profiles:
            if profile == 'default':
                continue
            if profiles[profile] == profiles['default']:
                return profile
        return None

    def ask_new_name_for_default_profile(self, users_home: str, profiles: Dict) -> None:
        """ The function receives user_home and profiles
            It uses users_home only for notification and profiles for backing up a current default profile 
            The function returns a backup name for current backup if the user agreed to back it up 
            otherwise it returns None """

        print(f"There is no default profile duplication among all accounts in {users_home}/.aws/credentials")
        while True:
            try:
                answer = input("Do you want to make backup of your current [default] profile? [Y/n] ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    new_default_name = input("Enter new name for your currnet [default] profile: ")
                    if new_default_name in profiles:
                        print(f"Profile with name {new_default_name} is already exists in {users_home}/.aws/credentials. Try once more")
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
            except (KeyboardInterrupt, EOFError):
                logging.error("\nProcess has been stopped. Interrupted by user")
                sys.exit(1)

    def create_backup_for_default(self, profiles: Dict, new_default_profile_name: str) -> Dict:
        profiles[new_default_profile_name] = profiles["default"]
        return profiles
