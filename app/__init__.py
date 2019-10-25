#! usr/bin/env python3

'''
Expense tracker app
Created by Paul, Pramod and Chris
'''

import os
from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI) # Connect to Cluster
db = client[""] # Selecting the database
expenses = db.expenses # Selecting the cafes collection

class Expense_Data():
    '''
    This class gets the json data from the mongo database.

    The data is then parsed by the methods to get cumulative results for display.
    '''
    def __init__(self):
        '''
        Calls the database and returns the json object.
        '''
        

    def food_total(self):
        '''
        Uses the databased data to calculate cumulative totals for the categories.
        '''


@app.route('/', method=['GET'])
def login():
    '''
    Gets the HTML and displays it for the user
    '''
    return render_template('index.html' title='home', form = 'form')

@app.route('/', method=['POST'])
def calculate():
    '''
    Calculates cumulative expenses and displays it to browser.
    '''
    