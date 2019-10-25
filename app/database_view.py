from environs import Env
import os
from datetime import datetime, timedelta
from pymongo import MongoClient
import dateutil.parser

# Instantiate.
env = Env()
env.read_env()

#print(os.getenv("TEST_ENV"))

URI = os.getenv("DB_URI")

#Connect to MongoDB
client = MongoClient(URI)
print(client.expence_tacker)

#Creating/Accessing a database called test
db = client["expense_tracker"]

# Creating/accessing a collection called greetings
expenses = db.expences

#d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
my_date_str = datetime.now()
my_datetime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

back_date = datetime.now() - timedelta(days=30)
print(f"back_date = {back_date}")
old_date = back_date.strftime('%d-%m-%Y %H:%M:%S')

expenses_all = list(expenses.find())
print("The whole list of expenses: \n", expenses_all, "\n")

for doc in expenses.find():
    # do things
    print(doc['expense'])
    print(doc['date'])

print(f"old_date = {old_date}, current_date = {my_datetime}")

# further investigation required to filter last one months data
expenses_date = expenses.find({'date': {'$gt':old_date, '$lt':my_datetime}})

print("The whole list of expenses: \n", expenses_date, "\n")

for doc in expenses_date:
    print(doc)