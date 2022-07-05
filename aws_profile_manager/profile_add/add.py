class Add:
    def ask_profile_name(self):
        """ Function simply asks a profile name and returns what it """
        aws_profile_name = input("New profile name: ")
        return aws_profile_name

    def ask_aws_access_key_id(self):
        """ Function simply asks a aws_access_key_id and returns what it """
        aws_access_key_id = input("AWS Access Key ID: ")
        return aws_access_key_id
        
    def ask_aws_secret_access_key(self):
        """ Function simply asks a aws_secret_access_key and returns what it """
        aws_secret_access_key = input("AWS Secret Access Key: ")
        return aws_secret_access_key

