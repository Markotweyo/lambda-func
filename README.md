Lambda Function Code
1. Create a lambda_function.py File: This file will contain the code for your Lambda function.
2. Package Dependencies: Install the necessary libraries and create a deployment package.
Here's how you can set it up:

1. Create lambda_function.py
2. Package Dependencies
To ensure the Lambda function has all necessary libraries, follow these steps:

a. Create a virtual environment and install the required libraries:

mkdir my_lambda_function
cd my_lambda_function
python3 -m venv venv
source venv/bin/activate
pip install gitpython

b. Package the environment and your Lambda function:

deactivate
cd venv/lib/python3.*/site-packages
zip -r9 ../../../../my_lambda_function.zip .
cd ../../../../
zip -g my_lambda_function.zip lambda_function.py


3. Upload the Deployment Package
Go back to the AWS Management Console:

Navigate to the Lambda function you created.
Under "Function code", select "Upload from" and choose ".zip file".
Upload my_lambda_function.zip.
4. Set Up IAM Role and Permissions
Ensure that your Lambda function has the necessary permissions. Attach the AWSLambdaBasicExecutionRole to your Lambda function.

5. Test the Lambda Function
You can test your Lambda function using the following event JSON:

Replace the gitlab_url, file_path, and access_token with your actual repository URL, file path, and personal access token.