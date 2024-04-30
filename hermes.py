#!/usr/bin/env python3

# class Color:
#     RESET = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     RED = '\033[91m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     BLUE = '\033[94m'
#     MAGENTA = '\033[95m'
#     CYAN = '\033[96m'

import subprocess
import sys
import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

def send_email(sender, recipient, subject, body, smtp_server="emailrelay:25", attachment=None):

    '''
    Function to send an email using the mailx command
    sender: email address of the sender
    recipient: email address of the recipient
    subject: email subject
    body: email body
    smtp_server: SMTP server to use for sending the email
    attachment: file path of the attachment (optional)

    Note: The mailx command must be installed on the system to use this function.

    Example usage:
    sender = "address_res@smartnet.com" <- This can be any custom email address
    recipient = "youremail@smartlinkgroup.com"
    subject = "Address Res ENodeB|LTE Check Failed"
    body = "The following sites did not pass the test"
    smtp_server = "emailrelay:25" <- This is the SMTP server!!!
    attachment = "/path/to/attachment.txt"  # Change to the actual file path

    send_email(sender, recipient, subject, body, smtp_server)
    '''

    subject  =subject + " " + date

    try:
        print(f"===============================================")
        print("Preparing to send email...")
        print(f"Sender: {sender}")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Attachment: {attachment}")

        # Construct the mailx command
        command = [
            'mailx',
            '-r', sender,
            '-s', subject,
            '-S', f'smtp={smtp_server}',
            recipient
        ]

        # Add attachment to the command if provided
        if attachment:
            command.extend(['-a', attachment])

        # Open a subprocess to execute the command
        print("Executing command:", " ".join(command))
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Write the email body to the subprocess stdin
        print("Writing email body to subprocess stdin...")
        process.stdin.write(body.encode())  # Write the email body
        process.stdin.close()

        # Wait for the process to complete
        print("Waiting for email to be sent...")
        stdout, stderr = process.communicate()

        # Check if there were any errors
        if stderr:
            print("Error:", stderr.decode())
        else:
            print("Email sent successfully.")
    
    except Exception as e:
        print("An error occurred:", e)

    print("Done")

if __name__ == "__main__":
    # Parse command-line arguments for sender, recipient, subject, body, and SMTP server
    sender = sys.argv[1]
    recipient = sys.argv[2]
    subject = sys.argv[3]
    body = sys.argv[4]
    smtp_server = sys.argv[5]

    # Call the send_email function with the parsed arguments
    send_email(sender, recipient, subject, body, smtp_server)

# if __name__ == "__main__":
#     #For test purpuoses
#     sender = "address_res@smartnet.com" 
#     recipient = "youremail@smartlinkgroup.com"
#     subject = "Address Res ENodeB|LTE Check Failed"
#     body = "The following sites did not pass the test"
#     smtp_server = "emailrelay:25"