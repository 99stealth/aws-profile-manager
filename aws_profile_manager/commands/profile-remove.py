import sys
import click
import logging
from aws_profile_manager import Common, Remove

@click.command()
@click.option('--aws-profile-name', required=False, help="AWS profile to remove", type=str)
def cli(aws_profile_name):
    """ Removes AWS profile from your ~/.aws/credentials """
    common = Common()
    remove = Remove()

    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        aws_profile_name = remove.choose_profile_to_remove(all_profiles)
    try:
        while True:
            answer = input("Profile [{}] will be removed. Are you sure you want to proceed? [Y/n] ".format(aws_profile_name))
            if answer.lower() == "yes" or answer.lower() == "y":
                del all_profiles[aws_profile_name]
                logging.info("Profile {} has been successfuly removed from {}/.aws/credentials".format(aws_profile_name, users_home))
                break
            elif answer.lower() == "no" or answer.lower() == "n":
                break
            else:
                print("Yes or No?")
    except KeyError as e:
        logging.error("Looks like profile {} does not exist in {}/.aws/credentials".format(e, users_home))
        sys.exit(1)
    common.rewrite_credentials_file(all_profiles, users_home)