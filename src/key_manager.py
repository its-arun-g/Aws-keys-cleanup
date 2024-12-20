import boto3
from src.utils import get_username_from_key
from src.utils import get_logger


iam_client = boto3.client('iam')

logger = get_logger()

def disable_key(access_key):
    """Disable a single AWS access key."""
    username = get_username_from_key(access_key)
    if not username:
        return 
    try:
        iam_client.update_access_key(
            AccessKeyId=access_key,
            Status='Inactive',
            UserName=username
        )
        logger.info(f"Disabled key {access_key} for user {username}.")
        return
    except Exception as e:
        logger.error(f"Failed to disable key {access_key}: {e}")
        return

def delete_key(access_key):
    """Delete a single AWS access key."""
    username = get_username_from_key(access_key)
    if not username:
        return
    try:
        iam_client.delete_access_key(
            AccessKeyId=access_key,
            UserName=username
        )
        logger.info(f"Deleted key {access_key} for user {username}.")
        return
    except Exception as e:
        logger.error(f"Failed to delete key {access_key}: {e}")
        return
