import click
import logging
from aws_profile_manager import Common, Add

@click.command()
@click.option('--aws-profile-name', required=False, help="New AWS profile name", type=str)
@click.option('--aws-access-key-id', required=False, help="AWS Access Key ID", type=str)
@click.option('--aws-secret-access-key', required=False, help="AWS Secret Access Key", type=str)
def cli(aws_profile_name, aws_access_key_id, aws_secret_access_key):
    """ Add new AWS profile to your ~/.aws/credentials """
    common = Common()
    add = Add()
    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        aws_profile_name = add.ask_profile_name()
    if not aws_access_key_id:
        while True:
            aws_access_key_id = add.ask_aws_access_key_id()
            if not common.aws_access_key_id_is_valid(aws_access_key_id):
                logging.error("Invalid AWS_ACCESS_KEY_ID format. Please, try again")
            else:
                break
    if not aws_secret_access_key:
        while True:
            aws_secret_access_key = add.ask_aws_secret_access_key()
            if not common.aws_secret_access_key_is_valid(aws_secret_access_key):
                logging.error("Invalid AWS_SECRET_ACCESS_KEY format. Please, try again")
            else:
                break
    all_profiles[aws_profile_name] = { 
        'aws_access_key_id': aws_access_key_id, 
        'aws_secret_access_key': aws_secret_access_key
        }
    common.rewrite_credentials_file(all_profiles, users_home)
