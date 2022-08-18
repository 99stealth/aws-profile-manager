import sys
import logging
from typing import List, Tuple
import boto3
from botocore import exceptions

class Rotate:
    def __init__(self, aws_profile_name) -> None:
        """ Class constructor """
        try:
            self.session = boto3.Session(profile_name=aws_profile_name)
            self.username = self.session.client('sts').get_caller_identity().get("Arn").split("/")[-1]
            self.iam_client = self.session.client('iam')
        except exceptions.ClientError:
            logging.error("There is some issue with connection to the AWS using your current credentials. Exit...")
            sys.exit(1)

    def get_access_keys(self) -> List:
        """ Method reaches AWS IAM service to get data about users AWS Access Keys.
            Returns list of Access Keys assigned to user in IAM """
        _access_keys_data = self.iam_client.list_access_keys(UserName=self.username).get('AccessKeyMetadata')
        _access_keys = [ i.get('AccessKeyId') for i in _access_keys_data ]
        return _access_keys

    def delete_access_key(self, access_key_id: str) -> bool:
        """ Method allows to deletes Access Keys for defined user """
        try:
            response = self.iam_client.delete_access_key(
                UserName=self.username,
                AccessKeyId=access_key_id
            )
        except:
            logging.error(f"Something went wrong during the {access_key_id} access key removal")
            return response
        else:
            logging.info(f"Access key {access_key_id} has been successfully removed")
        return

    def create_access_key(self) -> Tuple[str, str]:
        """ Method allows to create Access Keys for defined user """
        try:
            response = self.iam_client.create_access_key(
                UserName=self.username
            )
        except:
            logging.error(f"Something went wrong during the process of new credentials creation")
            return (False, False)
        else:
            logging.info(f"New credentials for user {self.username} have been successfully created")
        return (response.get('AccessKey').get('AccessKeyId'), response.get('AccessKey').get('SecretAccessKey'))
        
    def get_access_key_last_used(self, access_key_id: str) -> str:
        """ Method returns data about when and how Access Key was used """
        try:
            response = self.iam_client.get_access_key_last_used(
                AccessKeyId=access_key_id
            )
        except:
            logging.error(f"Couldn't get info about access key {access_key_id}")
            return ''
        else:
            logging.info(f"Last time the key {access_key_id} was used on {response.get('AccessKeyLastUsed').get('LastUsedDate')} in the {response.get('AccessKeyLastUsed').get('Region')} region")
        return response.get('AccessKeyLastUsed')

