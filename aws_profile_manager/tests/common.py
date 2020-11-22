import unittest
from aws_profile_manager import Common

class TestCommon(unittest.TestCase):
    def setUp(self):
        self.common = Common()
    
    def test_generate_new_profile_list(self):
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
                                    'aws_access_key_id': 'AKIAZZZZZZZZZZZZZZZZ',
                                    'aws_secret_access_key': 'zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ'
                                },
                            'test1': 
                                {
                                    'aws_access_key_id': 'AKIAZZZZZZZZZZZZZZZZ',
                                    'aws_secret_access_key': 'zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ'
                                }
                            }
        self.assertDictEqual(self.common.generate_new_profile_list(test_data, 'test1'), expected_output)

    def test_aws_access_key_id_with_valid_value(self):
        self.assertTrue(self.common.aws_access_key_id_is_valid('AKIAAAAAAAAAAAAAAAAA'))

    def test_aws_access_key_id_with_invalid_value(self):
        self.assertFalse(self.common.aws_access_key_id_is_valid('AKIAAAAAAAAAAAAAAAA'))

    def test_aws_secret_access_key_with_valid_value(self):
        self.assertTrue(self.common.aws_secret_access_key_is_valid('Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ'))

    def test_aws_secret_access_key_with_invalid_value(self):
        self.assertFalse(self.common.aws_secret_access_key_is_valid('0ZzzZZzZZz0zZ'))


if __name__ == '__main__':
    unittest.main()