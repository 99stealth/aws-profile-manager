import unittest
from aws_profile_switcher import Common

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


if __name__ == '__main__':
    unittest.main()