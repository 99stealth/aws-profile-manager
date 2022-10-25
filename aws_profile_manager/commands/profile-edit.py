import sys
import logging
import click
from aws_profile_manager import Common, Edit

@click.command()
@click.option('--aws-profile-name', required=False, help="AWS profile to edit", type=str)
@click.option('--aws-access-key-id', required=False, help="AWS Access Key ID", type=str)
@click.option('--aws-secret-access-key', required=False, help="AWS Secret Access Key", type=str)
def cli(aws_profile_name, aws_access_key_id, aws_secret_access_key):
    """ Edit AWS profile from your ~/.aws/credentials """
    common = Common()
    edit = Edit()

    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        aws_profile_name = common.choose_profile(all_profiles, operation="edit")
    if not aws_profile_name in all_profiles:
        logging.error(f"Looks like profile {aws_profile_name} does not exist in {users_home}/.aws/credentials")
        sys.exit(1)
    if not aws_access_key_id:
        while True:
            aws_access_key_id = edit.ask_aws_access_key_id()
            if not common.aws_access_key_id_is_valid(aws_access_key_id):
                logging.error("Invalid AWS_ACCESS_KEY_ID format. Please, try again")
            else:
                break
    if not aws_secret_access_key:
        while True:
            aws_secret_access_key = edit.ask_aws_secret_access_key()
            if not common.aws_secret_access_key_is_valid(aws_secret_access_key):
                logging.error("Invalid AWS_SECRET_ACCESS_KEY format. Please, try again")
            else:
                break
    all_profiles[aws_profile_name] = { 
        'aws_access_key_id': aws_access_key_id, 
        'aws_secret_access_key': aws_secret_access_key
        }
    common.rewrite_credentials_file(all_profiles, users_home)
    