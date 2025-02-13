import boto3
from src.utils import get_logger

iam_client = boto3.client('iam')
logger = get_logger()

def delete_user(username):
    """Delete a single IAM user."""
    try:
        # Detach user from groups
        groups = iam_client.list_groups_for_user(UserName=username)
        for group in groups['Groups']:
            iam_client.remove_user_from_group(UserName=username, GroupName=group['GroupName'])
            #logger.info(f"Removed {username} from group {group['GroupName']}")

        # Delete all access keys for the user
        response = iam_client.list_access_keys(UserName=username)
        for key in response.get('AccessKeyMetadata', []):
            iam_client.delete_access_key(
                AccessKeyId=key['AccessKeyId'],
                UserName=username
            )
        # Delete the user
        iam_client.delete_user(UserName=username)
        logger.info(f"Deleted user {username}.")
    except Exception as e:
        logger.error(f"Failed to delete user {username}: {e}")
    return
