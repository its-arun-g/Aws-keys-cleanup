# AWS Manager
A Python script to cleanup AWS access keys and IAM users in multiple accounts using AWS profiles. 

**NOTE** - Required profiles MUST be present in the `.aws/config` file
## Features
- Disable AWS access keys
- Delete AWS access keys
- Delete IAM users

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/its-arun-g/Aws-keys-cleanup.git
    ```
2. Set up the environment:
    ```bash
    python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install -r requirements.txt
    ```

3. Usage  
    ```bash
    usage: main.py [-h] --object {key,user} --action {disable,delete} --files-path FILE_PATH --profile-name PROFILE [--threads THREADS]

    Manage AWS access keys and users.

    options:
    -h, --help               show this help message and exit
    --object {key,user}      The object to manage (key or user).
    --action {disable,delete}
                             The action to perform (disable or delete).
    --profile-name           Profile name which is present for all required accounts
    --files-path FILE_PATH   Path to multiple files with account_id as the file name containing access keys or usernames present in that account (newline-separated).
    --threads THREADS        Number of threads to use for processing.
    ```


### To disable AWS access keys
```bash
python3 main.py --object key --action disable --files-path key_list/ --profile-name AdministratorAccess
```
### To delete AWS access keys
```bash
python3 main.py --object key --action delete --files-path key_list/ --profile-name AdministratorAccess
```
### To delete IAM users
```bash
python3 main.py --object user --action delete --files-path user_list/ --profile-name AdministratorAccess
```