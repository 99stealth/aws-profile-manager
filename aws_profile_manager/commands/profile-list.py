import click
from aws_profile_manager import Common

@click.command()
def cli():
    """ Shows all AWS profile from your ~/.aws/credentials """
    common = Common()

    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    _i = 0
    for _p in all_profiles:
        if _p == 'default' and len(all_profiles) > 1:
            for i in all_profiles:
                if i == 'default':
                    continue
                elif all_profiles[i] == all_profiles[_p]:
                    _p = f'{_p} (same as {i})'
                    break
        _i += 1
        print(f'{_i}. {_p}')