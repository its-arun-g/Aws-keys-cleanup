# AWS Manager
A Python script to cleanup AWS access keys and IAM users 
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
    usage: main.py [-h] --object {key,user} --action {disable,delete} --file FILE [--threads THREADS]

    Manage AWS access keys and users.

    options:
    -h, --help            show this help message and exit
    --object {key,user}   The object to manage (key or user).
    --action {disable,delete}
                            The action to perform (disable or delete).
    --file FILE           Path to the file containing access keys or usernames (newline-separated).
    --threads THREADS     Number of threads to use for processing.
    ```


### To disable AWS access keys
```bash
python3 main.py --object key --action disable --file key_list.txt --threads 10 
```
### To delete AWS access keys
```bash
python3 main.py --object key --action delete --file key_list.txt --threads 10
```
### To delete IAM users
```bash
python3 main.py --object user --action delete --file user_list.txt --threads 10
```
