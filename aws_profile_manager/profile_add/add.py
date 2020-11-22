import sys
import logging

class Add:
    def ask_profile_name(self):
        """ TBD """
        aws_profile_name = input("New profile name: ")
        return aws_profile_name

    def ask_aws_access_key_id(self):
        """ TBD """
        aws_access_key_id = input("AWS Access Key ID: ")
        return aws_access_key_id
        
    def ask_aws_secret_access_key(self):
        """ TBD """
        aws_secret_access_key = input("AWS Secret Access Key: ")
        return aws_secret_access_key

