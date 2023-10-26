import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule
from decouple import config

from main import get_doc_file, update_is_sent

current_file_index = [0]
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = config('USER_EMAIL')
sender_password = config('USER_EMAIL_PASSWORD')


def send_email():
    docx_file_paths = get_doc_file()
    if current_file_index[0] < len(docx_file_paths):
        file_path = docx_file_paths[current_file_index[0]]['file_path']
        receiver_email = docx_file_paths[current_file_index[0]]['email']
        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Attachment Test'

        # Email body
        body = 'Please find the attached .docx file.'
        msg.attach(MIMEText(body, 'plain'))

        # Attach the .docx file from the current file path
        with open(file_path, 'rb') as f:
            attach = MIMEApplication(f.read(), _subtype="docx")
            file_name = file_path.split("/")[-1]
            attach.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(attach)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            update_is_sent(docx_file_paths[current_file_index[0]]['id'])
            print(f"Email sent successfully for {file_path}")
        except Exception as e:
            print(f"Error sending email for {file_path}: {str(e)}")

        current_file_index[0] += 1
    else:
        current_file_index[0] = 0


# Schedule the job to run every 5 minutes
schedule.every(2).minutes.do(send_email)

# Schedule the job to run every day at 2:30 PM
# schedule.every().day.at("14:30").do(my_cron_job)

while True:
    schedule.run_pending()
    time.sleep(2)
