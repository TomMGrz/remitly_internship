import json

def json_verification(data):
    try:
        if isinstance(data, str):
            data = json.loads(data)

        policy_doc = data["PolicyDocument"]
        if not policy_doc:
            print('Policy document not found')
            return None
        
        statements = policy_doc["Statement"]
        if not statements or not isinstance(statements, list):
            print('Statements are missing or are not a list')
            return None

        for statement in statements:
            resource = statement["Resource"]
            if resource == "*":
                return False
        return True
    
    except Exception as e:
        print(f'Error veryfing data: {e}')
        return None
    
data = {
    "PolicyName": "root",
    "PolicyDocument": {
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
    }
}    
print('Verification result: ', json_verification(data))