#!/usr/bin/python

from faker import Faker
fake = Faker()
print("{Fake Name Generator}\n")
print("Name: " + fake.name())
print("Country: " + fake.country())
print("City: " + fake.city())
print("State: " + fake.state())
print("Address: " + fake.address())
print("Zip Code: " + fake.zipcode())
print("Credit Card: " + fake.credit_card_number())
print("Credit Card Security Code: " + fake.credit_card_security_code())
print("Credit Card Expire Date: " + fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"))
print("Birth Date: " + fake.date(pattern="%Y-%m-%d", end_datetime=None))
print("Email: " + fake.ascii_email())
print("Job: " + fake.job())

wait = input("\nPress [Enter] to go back...")
os.system("python3 DPredator.py")
