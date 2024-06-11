#Create a virtual environment and install the required libraries
mkdir my_lambda_function
cd my_lambda_function
python3 -m venv venv
source venv/bin/activate
pip install gitpython

#Package the environment and your Lambda function:
deactivate
cd venv/lib/python3.*/site-packages
zip -r9 ../../../../my_lambda_function.zip .
cd ../../../../
zip -g my_lambda_function.zip lambda_function.py
