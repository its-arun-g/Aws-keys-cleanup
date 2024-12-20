# AWS Manager
A Python script to manage AWS access keys and IAM users 
## Features
- Disable AWS access keys
- Delete AWS access keys
- Delete IAM users

## Prerequisites
- Python 3.x
- AWS credentials set up locally (e.g., via AWS CLI or environment variables)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Arun240726/Aws-keys-cleanup.git

2. Run the below commands:
   run:  |
          pip3 install poetry && \
          python3 -m virtualenv env/ && \
          source env/bin/activate && \
          poetry export --without-hashes --format=requirements.txt > requirements.txt && \
          pip3 install -r requirements.txt && \

## To meet your requirements for running the output, please execute one of the following commands.
1. For Disable AWS access keys
   python3 main.py --object key --action disable --file key_list.txt --threads 20 

2. For Delete AWS access keys
   python3 main.py --object key --action delete --file key_list.txt --threads 20

3. For Delete IAM users
   python3 main.py --object user --action delete --file user_list.txt --threads 20
