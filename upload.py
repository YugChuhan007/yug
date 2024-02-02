import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import schedule

def get_random_name(name_array, used_names):
    available_names = [name for name in name_array if name not in used_names]
    
    if available_names:
        selected_name = random.choice(available_names)
        used_names.add(selected_name)  # Add the selected name to the used_names set
        return selected_name
    else:
        return None

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.elasticemail.com', 2525) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

def main():
    # Define arrays of names for each subject
    maths = [
        "PAPER 1 MATHS_SOLUTION",
        "PAPER 2 MATHS_SOLUTION",
        "PAPER 3 MATHS_SOLUTION",
        "PAPER 4 MATHS_SOLUTION",
        "PAPER 5 MATHS_SOLUTION",
        "PAPER 6 MATHS_SOLUTION",
        "PAPER 7 MATHS_SOLUTION",
        "PAPER 8 MATHS_SOLUTION",
        "PAPER 9 MATHS_SOLUTION",
        "PAPER 10 MATHS_SOLUTION",
    ]
    physics = [
        "PAPER 1 PHY_SOLUTION",
        "PAPER 2 PHY_SOLUTION",
        "PAPER 3 PHY_SOLUTION",
        "PAPER 4 PHY_SOLUTION",
        "PAPER 5 PHY_SOLUTION",
        "PAPER 6 PHY_SOLUTION",
        "PAPER 7 PHY_SOLUTION",
        "PAPER 8 PHY_SOLUTION",
        "PAPER 9 PHY_SOLUTION",
        "PAPER 10 PHY_SOLUTION",
        "PAPER 11 PHY_SOLUTION",
        "PAPER 12 PHY_SOLUTION",
        "PAPER 13 PHY_SOLUTION",
        "PAPER 14 PHY_SOLUTION",
        "PAPER 15 PHY_SOLUTION",
        "PAPER 16 PHY_SOLUTION",
        "PAPER 17 PHY_SOLUTION",
        "PAPER 18 PHY_SOLUTION",
        "PAPER 19 PHY_SOLUTION",
        "PAPER 20 PHY_SOLUTION",
    ]
    chemistry = [
        "PAPER 1 CHEM_SOLUTION",
        "PAPER 2 CHEM_SOLUTION",
        "PAPER 3 CHEM_SOLUTION",
        "PAPER 4 CHEM_SOLUTION",
        "PAPER 5 CHEM_SOLUTION",
        "PAPER 6 CHEM_SOLUTION",
        "PAPER 7 CHEM_SOLUTION",
        "PAPER 8 CHEM_SOLUTION",
        "PAPER 9 CHEM_SOLUTION",
        "PAPER 10 CHEM_SOLUTION",
        "PAPER 11 CHEM_SOLUTION",
        "PAPER 12 CHEM_SOLUTION",
        "PAPER 13 CHEM_SOLUTION",
        "PAPER 14 CHEM_SOLUTION",
        "PAPER 15 CHEM_SOLUTION",
        "PAPER 16 CHEM_SOLUTION",
        "PAPER 17 CHEM_SOLUTION",
        "PAPER 18 CHEM_SOLUTION",
        "PAPER 19 CHEM_SOLUTION",
        "PAPER 20 CHEM_SOLUTION",
    ]
    his_civ=[
        "PAPER 1 HIS_CIV_SOLUTION",
        "PAPER 2 HIS_CIV_SOLUTION",
        "PAPER 3 HIS_CIV_SOLUTION",
        "PAPER 4 HIS_CIV_SOLUTION",
        "PAPER 5 HIS_CIV_SOLUTION",
        "PAPER 6 HIS_CIV_SOLUTION",
        "PAPER 7 HIS_CIV_SOLUTION",
        "PAPER 8 HIS_CIV_SOLUTION",
        "PAPER 9 HIS_CIV_SOLUTION",
        "PAPER 10 HIS_CIV_SOLUTION",
        "PAPER 11 HIS_CIV_SOLUTION",
        "PAPER 12 HIS_CIV_SOLUTION",
        "PAPER 13 HIS_CIV_SOLUTION",
        "PAPER 14 HIS_CIV_SOLUTION",
        "PAPER 15 HIS_CIV_SOLUTION",
        "PAPER 16 HIS_CIV_SOLUTION",
        "PAPER 17 HIS_CIV_SOLUTION",
        "PAPER 18 HIS_CIV_SOLUTION",
        "PAPER 19 HIS_CIV_SOLUTION",
        "PAPER 20 HIS_CIV_SOLUTION",
    ]
    geo = [
        "PAPER 1 GEO_SOLUTION",
        "PAPER 2 GEO_SOLUTION",
        "PAPER 3 GEO_SOLUTION",
        "PAPER 4 GEO_SOLUTION",
        "PAPER 5 GEO_SOLUTION",
        "PAPER 6 GEO_SOLUTION",
        "PAPER 7 GEO_SOLUTION",
        "PAPER 8 GEO_SOLUTION",
        "PAPER 9 GEO_SOLUTION",
        "PAPER 10 GEO_SOLUTION",
        "PAPER 11 GEO_SOLUTION",
        "PAPER 12 GEO_SOLUTION",
        "PAPER 13 GEO_SOLUTION",
        "PAPER 14 GEO_SOLUTION",
        "PAPER 15 GEO_SOLUTION",
        "PAPER 16 GEO_SOLUTION",
        "PAPER 17 GEO_SOLUTION",
        "PAPER 18 GEO_SOLUTION",
        "PAPER 19 GEO_SOLUTION",
        "PAPER 20 GEO_SOLUTION",
    ]
    bio= [
        "PAPER 1 BIO_SOLUTION",
        "PAPER 2 BIO_SOLUTION",
        "PAPER 3 BIO_SOLUTION",
        "PAPER 4 BIO_SOLUTION",
        "PAPER 5 BIO_SOLUTION",
        "PAPER 6 BIO_SOLUTION",
        "PAPER 7 BIO_SOLUTION",
        "PAPER 8 BIO_SOLUTION",
        "PAPER 9 BIO_SOLUTION",
        "PAPER 10 BIO_SOLUTION",
        "PAPER 11 BIO_SOLUTION",
        "PAPER 12 BIO_SOLUTION",
        "PAPER 13 BIO_SOLUTION",
        "PAPER 14 BIO_SOLUTION",
        "PAPER 15 BIO_SOLUTION",
        "PAPER 16 BIO_SOLUTION",
        "PAPER 17 BIO_SOLUTION",
        "PAPER 18 BIO_SOLUTION",
        "PAPER 19 BIO_SOLUTION",
        "PAPER 20 BIO_SOLUTION",
    ]

    used_names=set()

    # Randomly select one name from the "maths" array
    selected_name_maths = get_random_name(maths,used_names)

    # Randomly select two subjects (excluding "maths")
    other_subjects = [physics, chemistry,his_civ,geo,bio]
    selected_subjects = random.sample(other_subjects, k=3)

    # Randomly select one name from each of the two selected subjects
    selected_name_subject1 = get_random_name(selected_subjects[0],used_names)
    selected_name_subject2 = get_random_name(selected_subjects[1],used_names)
    selected_name_subject3 = get_random_name(selected_subjects[2],used_names)

    # Send a notification with the selected names via email
    subject = 'Random Name Selector Notification'
    message = f"Selected SUBJECTS:\nMaths: {selected_name_maths}\nSubject 2: {selected_name_subject1}\nSubject 3: {selected_name_subject2}\nSubject 4: {selected_name_subject3}"
    
    # Add your Gmail credentials and recipient email address here
    sender_email ='mrwhite3727@gmail.com'
    sender_password = '3FDA82A92B962094F90DF1063E108EA7AFB2'
    recipient_email = 'tewhite2529q@gmail.com'
    
    send_email(sender_email, sender_password, recipient_email, subject, message)


schedule.every().day.at("15:20").do(main)

# Your main loop
if __name__ == "__main__":
 print("HELLO")
 while True:
    schedule.run_pending()  # Check if any scheduled tasks are ready to run

