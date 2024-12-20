import boto3
from .utils import get_username_from_key

iam_client = boto3.client('iam')

def disable_key(access_key):
    """Disable a single AWS access key."""
    username = get_username_from_key(access_key)
    if not username:
        return f"Skipping key {access_key}: Username not found."
    try:
        iam_client.update_access_key(
            AccessKeyId=access_key,
            Status='Inactive',
            UserName=username
        )
        return f"Disabled key {access_key} for user {username}."
    except Exception as e:
        return f"Failed to disable key {access_key}: {e}"

def delete_key(access_key):
    """Delete a single AWS access key."""
    username = get_username_from_key(access_key)
    if not username:
        return f"Skipping key {access_key}: Username not found."
    try:
        iam_client.delete_access_key(
            AccessKeyId=access_key,
            UserName=username
        )
        return f"Deleted key {access_key} for user {username}."
    except Exception as e:
        return f"Failed to delete key {access_key}: {e}"
