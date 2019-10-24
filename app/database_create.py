from environs import Env
import os
import datetime
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
my_date_str = "2019-10-24T16:00:00Z"
my_datetime = dateutil.parser.parse(my_date_str)

expense = {
        "expense": "99.99",
        "description": "pub night thursday",
        "category": "entertainment",
        "date": my_datetime
        }
id = expenses.insert_one(expense).inserted_id
print(id)
