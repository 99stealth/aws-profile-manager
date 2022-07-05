import sys
import click
import logging
from aws_profile_manager import Common

@click.command()
@click.option('--aws-profile-name', required=False, help="AWS profile to remove", type=str)
@click.option('--yes', is_flag=True, required=False, help="Confirm that you agree to remove keys. Avoids manual confirmation", default=False, type=bool)
def cli(aws_profile_name, yes):
    """ Removes AWS profile from your ~/.aws/credentials """
    common = Common()

    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        aws_profile_name = common.choose_profile(all_profiles, operation="remove")
    try:
        while True:
            if yes:
                answer = 'yes'
            else:
                answer = input(f"Profile [{aws_profile_name}] will be removed. Are you sure you want to proceed? [Y/n] ")
            if answer.lower() == "yes" or answer.lower() == "y":
                del all_profiles[aws_profile_name]
                logging.info(f"Profile {aws_profile_name} has been successfuly removed from {users_home}/.aws/credentials")
                break
            elif answer.lower() == "no" or answer.lower() == "n":
                break
            else:
                print("Yes or No?")
    except KeyError as e:
        logging.error(f"Looks like profile {e} does not exist in {users_home}/.aws/credentials")
        sys.exit(1)
    common.rewrite_credentials_file(all_profiles, users_home)