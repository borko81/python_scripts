# Unclock gmail use less secure password for APP found here: https://www.abstractapi.com/guides/sending-email-with-python

import sys
import os
from collections import defaultdict
from datetime import datetime
import smtplib
import ssl

from control_data import *


# Need to send email, accaunt need to be with rights for use for less secure program
EMAIL_PORT = EMAIL_PORT
EMAIL_SMTP = EMAIL_SMTP
gmail_user = gmail_user

# path to common folder with archive
# FOLDER_TO_CHECK = r"C:\Users\Borko\Desktop\files"
FOLDER_TO_CHECK = sys.argv[1]

# what expect like number from any folder
folder_number_of_arc = folder_number_of_arc


def check_if_folder_exists(FOLDER_TO_CHECK):
    """Check if path exists"""
    return os.path.exists(FOLDER_TO_CHECK)


def convert_timestamp_to_date_format(stamp, format_data, today_date=datetime.now()):
    """After get timestamp from date modify, convert it to human readable date tormmat"""
    return (
        datetime.fromtimestamp(stamp).strftime(format_data),
        today_date.strftime(format_data),
    )


def send_email(message, list_with_users="borkounreal@gmail.com"):
    ctx = ssl.create_default_context()
    password = password  # Your app password goes here get from step above!
    sender = gmail_user  # Your e-mail address
    receiver = list_with_users  # Recipient's address
    message = """
	Backup status found error's: {}
	""".format(
        message
    )

    with smtplib.SMTP_SSL(EMAIL_SMTP, port=EMAIL_PORT, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


class ValidateBackup:
    def __init__(self, folder_name=FOLDER_TO_CHECK):
        self.folder_name = folder_name
        self.error_messages = []
        self.format_data = "%d.%m.%y"

    def return_all_folders(self):
        """List all subfolders"""
        folders = os.listdir(self.folder_name)
        return [dirname for dirname in folders]

    def walk_into_the_folder(self):
        """walk folder one by one to check count is corect or not"""
        for item in self.return_all_folders():
            error_check = defaultdict(int)
            for root, dirname, files in os.walk(os.path.join(self.folder_name, item)):
                for file in files:
                    modify = os.stat(
                        os.path.join(self.folder_name, item, file)
                    ).st_mtime
                    date_created, today_date = convert_timestamp_to_date_format(
                        modify, self.format_data
                    )
                    if date_created == today_date:
                        error_check[item] += 1

                if item not in folder_number_of_arc:
                    self.error_messages.append(f"Folder {item} not found into script configuration")
                else:   
                    if error_check[item] != folder_number_of_arc[item]:
                        self.error_messages.append(f"Error in folder {item}")

    @property
    def is_error_or_not(self):
        return self.error_messages


def main():
    validate = ValidateBackup()
    validate.walk_into_the_folder()
    errors = validate.is_error_or_not
    if len(errors) > 0:
        print(errors)
        send_email(errors)


if __name__ == "__main__":
    try:
        check_if_folder_exists(FOLDER_TO_CHECK) == True
    except:
        raise ("Error with common folder, maybe mising...")
    else:
        main()
