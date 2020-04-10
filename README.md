# AWS Profile Switcher
The tool which allows you to jump between your profiles in your `~/.aws/credentials`

## Problematics
Well, if you are operating only one AWS account then you will not find this util useful. Problem appears when there are more than 3 accounts under your control. Sure, you can use `--profile` flag with any your aws cli command. But what if you need to run number of commands for several accounts, then make sure you don't forget to add `--profile` to your command or specified the right profile name. 
Another example is about Hasicorp Terraform. Let's imagine that you have one module which you need to apply for several accounts. Unfortunately, terraform doesn't allow you to specify `--profile` and that's logically since Terraform is not about AWS. So, you will need to hardcode your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY or go to `~/.aws/credentials` and change the `[default]` profile.

## How to install
That's easy just run
```
sudo pip install aws-profile-switcher
```
Or `clone` this repository and run
```
make install
```