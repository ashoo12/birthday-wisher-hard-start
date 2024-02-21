import pandas
import smtplib
import datetime as dt
import random

# -------------------------BIRTHDAY DICT----------------------------------------------------------------
data=pandas.read_csv("birthdays.csv").to_dict()
birthday_person=data["name"][0]


birthdays_dict = {
    "month":data["month"],
    "day":data["day"]
}
# ----------------------------------LETTER TEMPLATES------------------------------------------------------
with open(file="./letter_templates/letter_1.txt")as letter_1_text:
    letter_1=letter_1_text.read()
    letter_1=letter_1.replace("[NAME]",birthday_person)

with open(file="./letter_templates/letter_2.txt")as letter_2_text:
    letter_2=letter_2_text.read()
    letter_2 = letter_2.replace("[NAME]", birthday_person)
letters=[letter_1,letter_2]

# ---------------------------- DATE TIME MODULE---------------------------------------------------------
now=dt.datetime.now()
month=now.month
day=now.day
if day==birthdays_dict["day"][0] and month==birthdays_dict["month"][0] :
    selected_letter=random.choice(letters)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
my_email="newtester420@gmail.com"
my_password= "qwnjfytbgjevradi"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,to_addrs="newtester420@yahoo.com",msg=f"subject:Birthday wishes \n\n {selected_letter}")


