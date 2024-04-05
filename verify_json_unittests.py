import unittest
from verify_json import json_verification

class TestJsonVerification(unittest.TestCase):
    
    def test_wildcard_resource(self):
        data =     {"PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }}
        self.assertFalse(json_verification(data))

    def test_specific_resource(self):

        data =     {"PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": "arn:aws:iam::123456789012:user/*"
                }
            ]
        }}
        self.assertTrue(json_verification(data))

    def test_empty_resource(self):
        data =     {"PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": ""
                }
            ]
        }}
        self.assertTrue(json_verification(data))

    def test_empty_statements(self):
        data =     {"PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": []
        }}   
        self.assertIsNone(json_verification(data))

    def test_valid_json_format(self):
        data = {"PolicyName": "root"}

        self.assertIsNone(json_verification(data))


if __name__ == '__main__':
    unittest.main()