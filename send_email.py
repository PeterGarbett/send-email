"""Send mail using a gmail account, the details of which are in a .json config file."""

import smtplib
import sys
import json


def load_config(config):
    """Load config from a json file"""

    try:
        with open(config, "r", encoding="ascii") as f:
            hosts = json.load(f)
            return hosts

    except Exception as err:
        print(err)
        return []

    return []


def send_email(user, pwd, recipient, subject, body):
    """The gubbins google require to send mail using a google email account"""
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (
        FROM,
        ", ".join(TO),
        SUBJECT,
        TEXT,
    )
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        # print("successfully sent the mail")
        return True
    except Exception as err:
        print("failed to send email", err)

    return False


def message_using_config(subject, message, recipient, config):
    """Send a message to a recipient using the email
    account/password/default recipient from a config file"""
    mail_details = load_config(config)

    if len(mail_details) != 3:
        print("ERROR: incorrect email config file")
        return

    user = mail_details[0]
    password = mail_details[1]

    # If the recipient isn't defined, use the default defined in the
    # config file

    if recipient == "":
        recipient = mail_details[2]

    #    print("recipient=", recipient)

    send_email(user, password, recipient, subject, message)


# Example call
# (Fill out email.config with reasonable values before trying this.)
# python3 send_email.py "./email.config"  "test subject" "test body" "fred@gmail.com"
#


def main():
    """Use command line entry to drive this test routine
    if the recipient is defined on the command line, use it, the default
    is in the config file"""

    sys.argv.pop(0)  # Discard routine name
    inputargs = sys.argv

    if not (len(inputargs) == 3 or len(inputargs) == 4):
        print("ERROR: incorrect number of arguments")
        sys.exit()

    config = inputargs[0]
    subject = inputargs[1]
    body = inputargs[2]

    # If we have 4 parameters, the final one is the required recipient

    if len(inputargs) == 4:
        target = inputargs[3]
    else:
        target = ""

    message_using_config(subject, body, target, config)

    sys.exit()


if __name__ == "__main__":
    main()
