python_version >= "3.11"

# Document automation

This project send the user with docx file on his email. for now user is added from sample_response.json file. program is not storing the document(docx) file any where. it's getting stored in temporary memory.

### ------ SETUP WITH VIRTUAL ENVIRONMENT ------

### FOLLOW BELOW STEPS -

### INSTALL LIBRARIES
pip install -r requirements.txt

### MODIFY DATABASE SETTINGS

1. Please open .env file
2. set the values accordingly

### CHECK DATABASE CONNECTION - from database folder

python database.py

###### RUN CRON JOB

python email_sender_cron_job.py

After the above two commands, the email scheduler will be start.

###### sample .env file
DB_USER="root"<br />
DB_HOST="localhost"<br />
DB_PASSWORD="admin"<br />
DB_NAME="document"<br />
USER_EMAIL="test@gmail.com"<br />
USER_EMAIL_PASSWORD="test@1234"<br />