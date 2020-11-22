import unittest
from aws_profile_manager import Switch

class TestCommon(unittest.TestCase):
    def setUp(self):
        self.switch = Switch()

    def test_get_defaults_backup_without_default_backup(self):
        test_data = {
                    'default': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'
                        },
                    'test1': 
                        {
                            'aws_access_key_id': 'AKIAZZZZZZZZZZZZZZZZ',
                            'aws_secret_access_key': 'zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ'}
                    }
        expected_output = None
        self.assertEquals(self.switch.get_defaults_backup(test_data), expected_output)

    def test_get_defaults_backup_with_default_backup(self):
        test_data = {
                    'default': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'
                        },
                    'test1': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'}
                    }
        expected_output = 'test1'
        self.assertEquals(self.switch.get_defaults_backup(test_data), expected_output)

    def test_create_backup_for_default(self):
        test_data = {
                    'default': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'
                        },
                    'test1': 
                        {
                            'aws_access_key_id': 'AKIAZZZZZZZZZZZZZZZZ',
                            'aws_secret_access_key': 'zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ'}
                    }
        expected_output = {
                    'default': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'
                        },
                    'test1': 
                        {
                            'aws_access_key_id': 'AKIAZZZZZZZZZZZZZZZZ',
                            'aws_secret_access_key': 'zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ'},
                    'test2': 
                        {
                            'aws_access_key_id': 'AKIAYYYYYYYYYYYYYYYY',
                            'aws_secret_access_key': 'yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY'}
                    }
        self.assertDictEqual(self.switch.create_backup_for_default(test_data, 'test2'), expected_output)

if __name__ == '__main__':
    unittest.main()