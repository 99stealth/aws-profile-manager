import click
import logging
from aws_profile_manager import Common, Add

@click.command()
@click.option('--aws-profile-name', required=False, help="New AWS profile name", type=str)
@click.option('--aws-access-key-id', required=False, help="AWS Access Key ID", type=str)
@click.option('--aws-secret-access-key', required=False, help="AWS Secret Access Key", type=str)
@click.option('--aws-session-token', required=False, help="AWS Session Token", type=str)
def cli(aws_profile_name, aws_access_key_id, aws_secret_access_key, aws_session_token):
    """ Add new AWS profile to your ~/.aws/credentials """
    common = Common()
    add = Add()
    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        while True:
            aws_profile_name = add.ask_profile_name()
            if aws_profile_name in all_profiles:
                logging.error(f"Profile {aws_profile_name} already exists... Please, try again")
            else:
                break
    else:
        if aws_profile_name in all_profiles:
            logging.error(f"Profile {aws_profile_name} already exists... Exit")
            exit(1)
    if not aws_access_key_id:
        while True:
            aws_access_key_id = add.ask_aws_access_key_id()
            if not common.aws_access_key_id_is_valid(aws_access_key_id) and not common.aws_access_key_id_for_session_token_is_valid(aws_access_key_id):
                logging.error("Invalid AWS_ACCESS_KEY_ID format. Please, try again")
            else:
                break
    else:
        if not common.aws_access_key_id_is_valid(aws_access_key_id) and not common.aws_access_key_id_for_session_token_is_valid(aws_access_key_id):
            logging.error("Invalid AWS_ACCESS_KEY_ID format... Exit")
            exit(1)
    if not aws_secret_access_key:
        while True:
            aws_secret_access_key = add.ask_aws_secret_access_key()
            if not common.aws_secret_access_key_is_valid(aws_secret_access_key):
                logging.error("Invalid AWS_SECRET_ACCESS_KEY format. Please, try again")
            else:
                break
    else:
        if not common.aws_secret_access_key_is_valid(aws_secret_access_key):
            logging.error("Invalid AWS_SECRET_ACCESS_KEY format... Exit")
            exit(1)

    if not aws_session_token and common.aws_access_key_id_for_session_token_is_valid(aws_access_key_id):
        aws_session_token = add.ask_aws_session_token()

    all_profiles[aws_profile_name] = {
        'aws_access_key_id': aws_access_key_id, 
        'aws_secret_access_key': aws_secret_access_key
        }
    
    if aws_session_token:
        all_profiles[aws_profile_name]['aws_session_token'] = aws_session_token
    
    common.rewrite_credentials_file(all_profiles, users_home)
