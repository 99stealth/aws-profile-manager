import click
from aws_profile_manager import Common, Switch


@click.command()
def cli():
    """ Show current aws profile from ~/.aws/credentials """
    common = Common()
    switch = Switch()

    print(switch.get_defaults_backup(common.get_all_profiles(common.get_users_home())))
