import logging
import click
from aws_profile_manager import Common, Switch

@click.command()
def cli():
    """ Shows current default AWS profile from your ~/.aws/credentials """
    common = Common()
    switch = Switch()
    
    logging.warning(switch.get_defaults_backup(common.get_all_profiles(common.get_users_home())))