import boto3

iam_client = boto3.client('iam')

def delete_user(username):
    """Delete a single IAM user."""
    try:
        # Delete all access keys for the user
        response = iam_client.list_access_keys(UserName=username)
        for key in response.get('AccessKeyMetadata', []):
            iam_client.delete_access_key(
                AccessKeyId=key['AccessKeyId'],
                UserName=username
            )
            print(f"Deleted access key {key['AccessKeyId']} for user {username}.")
        # Delete the user
        iam_client.delete_user(UserName=username)
        return f"Deleted user {username}."
    except Exception as e:
        return f"Failed to delete user {username}: {e}"
