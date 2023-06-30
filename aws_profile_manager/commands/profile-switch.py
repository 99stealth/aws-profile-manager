import click
import logging
from aws_profile_manager import Common, Switch

@click.command()
@click.option('--aws-profile-name', required=False, help="AWS profile to switch", type=str)
def cli(aws_profile_name):
    """ Switch default AWS profile in your ~/.aws/credentials """
    common = Common()
    switch = Switch()

    users_home = common.get_users_home()
    all_profiles = common.get_all_profiles(users_home)
    new_default_profile_name = aws_profile_name
    if not new_default_profile_name:
        if "default" not in all_profiles:
            logging.warning(f"There is no [default] profile in your {users_home}/.aws/credentials. It will be automatically created")
        else:
            defaults_backup = switch.get_defaults_backup(all_profiles)
            if defaults_backup:
                logging.warning(f"Your current default is \033[1m{defaults_backup}\033[0m (excluded from options below)\n")
            else:
                new_default_profile_name = switch.ask_new_name_for_default_profile(users_home, all_profiles)
                if new_default_profile_name:
                    all_profiles = switch.create_backup_for_default(all_profiles, new_default_profile_name)
        new_default = common.choose_profile(all_profiles, operation="switch your current default", skip_profiles=["default", new_default_profile_name, defaults_backup])
    else:
        if new_default_profile_name in all_profiles:
            new_default = new_default_profile_name
        else:
            logging.error(f"No such profile \033[1m{new_default_profile_name}\033[0m\n in profiles' list")
            exit(1)
    new_profiles_list = common.generate_new_profile_list(all_profiles, new_default)
    common.rewrite_credentials_file(new_profiles_list, users_home)
    logging.info(f'Default profile has been changed to \033[1m{new_default}\033[0m')