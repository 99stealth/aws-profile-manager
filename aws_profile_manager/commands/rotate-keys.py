import sys
import click
import logging

from aws_profile_manager import Common, Rotate

@click.command()
@click.option('--aws-profile-name', required=False, help="AWS profile to rotate keys", type=str)
@click.option('--yes', is_flag=True, required=False, help="Confirm that you agree to rotate keys. Avoids manual confirmation", default=False, type=bool)
def cli(aws_profile_name, yes):
    """ Rotate keys for defined profile ~/.aws/credentials """
    common = Common()
    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    if not aws_profile_name:
        aws_profile_name = common.choose_profile(all_profiles, operation="rotate")
    try:
        access_key_id = all_profiles.get(aws_profile_name).get('aws_access_key_id')
    except:
        logging.error(f"No such profile {aws_profile_name} in your credentials file")
        sys.exit(1)
    rotate = Rotate(aws_profile_name)
    current_access_keys = rotate.get_access_keys()
    if len(current_access_keys) > 1:
        logging.warning('There is more than one access key is created for the current user. '
        f'One (which is not used in profile [{aws_profile_name}]) should be deleted. '
        'Otherwise, it is not possible to make a credentials rotation')
        for _ak in current_access_keys:
            if _ak != access_key_id:
                while True:
                    if yes:
                        answer = 'yes'
                    else:
                        _ak_last_used = rotate.get_access_key_last_used(_ak)
                        answer = input(f"\nAccess key {_ak} (last used: {_ak_last_used['LastUsedDate'] if 'LastUsedDate' in _ak_last_used else 'N/A'}) will be deleted. Do you agree with that? [Y/n] ")
                    if answer.lower() == "yes" or answer.lower() == "y":
                        rotate.delete_access_key(access_key_id=_ak)
                        break
                    elif answer.lower() == "no" or answer.lower() == "n":
                        print('Exit...')
                        sys.exit(1)
                    else:
                        print("Yes or No?")
    aws_access_key_id, aws_secret_access_key = rotate.create_access_key()
    if aws_access_key_id and aws_secret_access_key:
        rotate.delete_access_key(access_key_id=access_key_id)
        all_profiles[aws_profile_name]['aws_access_key_id'] = aws_access_key_id
        all_profiles[aws_profile_name]['aws_secret_access_key'] = aws_secret_access_key
        common.rewrite_credentials_file(all_profiles, users_home)
