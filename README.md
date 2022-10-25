# AWS Profile Manager

[![Actions Status](https://github.com/99stealth/aws-profile-manager/workflows/Check%20and%20Test/badge.svg)](https://github.com/99stealth/aws-profile-manager/actions)
[![PyPI version](https://badge.fury.io/py/aws-profile-manager.svg)](https://badge.fury.io/py/aws-profile-manager)
![GitHub License](https://img.shields.io/github/license/99stealth/aws-profile-manager)
![Commit Activity](https://img.shields.io/github/commit-activity/m/99stealth/aws-profile-manager)

The tool which allows you to jump between your profiles in your `~/.aws/credentials`

## Problematics
Well, if you are operating only one AWS account then you will not find this util useful. Problem appears when there are more than 3 accounts under your control. Sure, you can use `--profile` flag with any your aws cli command. But what if you need to run number of commands for several accounts, then make sure you don't forget to add `--profile` to your command or specified the right profile name. 
Another example is about Hashicorp Terraform. Let's imagine that you have one module which you need to apply for several accounts. Unfortunately, terraform doesn't allow you to specify `--profile` and that's logically since Terraform is not about AWS. So, you will need to hardcode your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY or go to `~/.aws/credentials` and change the `[default]` profile.

## How to install
That's easy just run
```
sudo pip install aws-profile-manager
```
Or `clone` this repository and run
```
make install
```

## Usage

```
Usage: aws-profile-manager [OPTIONS] COMMAND [ARGS]...

  This tool's subcommands are loaded from a plugin folder dynamically.

Options:
  --version    Show the version and exit.
  -q, --quiet  Less outputs
  --help       Show this message and exit.

Commands:
  profile-add      Add new AWS profile to your ~/.aws/credentials
  profile-current  Shows current default AWS profile from your ~/.aws/credentials
  profile-edit     Edit AWS profile from your ~/.aws/credentials
  profile-list     Shows all AWS profile from your ~/.aws/credentials
  profile-remove   Removes AWS profile from your ~/.aws/credentials
  profile-switch   Switch default AWS profile in your ~/.aws/credentials
  rotate-keys      Rotate keys for defined profile ~/.aws/credentials
```

## How does it work
### Add profile
Allows to add new profile to your `~/.aws/credentials`
To run `profile-add` in interactive run next command
```
aws-profile-manager profile-add
```
Or you can specify everything inline
```
aws-profile-manager profile-add --aws-profile-name=your-profile-name --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ
```

### Edit profile
Allows to edit existing profile in your `~/.aws/credentials`
To run `profile-edit` in interactive run next command
```
aws-profile-manager profile-edit
```
Or you can specify everything inline
```
aws-profile-manager profile-edit --aws-profile-name=your-profile-name --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ
```

### Remove profile
Allows to add remove profile from your `~/.aws/credentials`
To run `profile-remove` in interactive mode run next command
```
aws-profile-manager profile-remove
```
Or you can specify the profile inline and confirm that you understand that profile will be removed from your file using flag `--yes`
```
aws-profile-manager profile-remove --aws-profile-name=your-profile-name --yes
```

### Switch profile 
Makes a specified profile default in your `~/.aws/credentials`
To run `profile-switch` in interactive mode run next command
```
aws-profile-manager profile-switch
```
Unfortunately, there is no inline option here, but I swear it will be added in the nearest future

### List profiles
Shows all AWS profile from your `~/.aws/credentials` and exits
```
aws-profile-manager profile-list
```

### Rotate keys
Rotate keys for defined profile `~/.aws/credentials`
To run `rotate-keys` in interactive mode run next command
```
aws-profile-manager rotate-keys 
```
Or you can specify the profile inline and confirm that you understand that keys for profile will be rotated using flag `--yes`
```
aws-profile-manager rotate-keys --aws-profile-name=your-profile-name --yes
```
> :warning: Be careful in case you specified `--yes` flag since you will not see tips regarding your keys. Rotation will DELETE your key second key if such exists since there may be only two keys per user and the rotation procedure requires to create new key before deleting an old one
Also, you can make the rotaton on a regular basis using cron. Simply add this line to your `crontab`.
```
crontab -e
```
In order to rotate on monthly basis add next line
```
@monthly aws-profile-manager rotate-keys --aws-profile-name=your-profile-name --yes
```
