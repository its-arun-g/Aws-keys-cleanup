import boto3
import logging

iam_client = boto3.client('iam')

def get_username_from_key(access_key):
    """Fetch the username associated with an access key."""
    try:
        response = iam_client.get_access_key_last_used(AccessKeyId=access_key)
        return response.get('UserName')
    except Exception as e:
        print(f"Error fetching username for key {access_key}: {e}")
        return None
    
def get_logger() -> logging.Logger:
    format = "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
    logging.basicConfig(format=format)
    logger = logging.getLogger("aws-keys-cleanup")
    logger.setLevel("INFO")
    return logger
