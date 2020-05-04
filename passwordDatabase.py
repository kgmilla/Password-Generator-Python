import sqlite3
import time
import datetime
from dateutil.relativedelta import relativedelta
import bitsToAscii

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()


def getCurrentDateStr():
    '''Gets the current date in order to give database
    creation time'''
    currentTime = time.time()
    return str(datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d'))

def getExpireDateStr(monthsUntilPassExp, daysUntilPassExp):
    '''Takes in the months and days until password should
    expire in order to give the database the time the password
    should be changed'''
    currentTime = datetime.datetime.utcnow()
    expDate = currentTime + relativedelta(months=monthsUntilPassExp, days=daysUntilPassExp)
    return str(expDate.date())


def createTable():
    '''Creates the sqlite3 database table, if it is not already
    created, and adds the necessary values for passwords, date creation,
    and expiration date'''
    cursor.execute('CREATE TABLE IF NOT EXISTS passwords(passwords TEXT, dateCreated REAL, dateExpire REAL)')


def dynamicDataInput(password, dateCreated, dateExpire):
    '''This function takes the inputs for password, creation date, and 
    expiration date and adds those values into the database dynamically.'''
    cursor.execute("INSERT INTO passwords (passwords, dateCreated, dateExpire) Values (?, ?, ?)",
    (password, dateCreated, dateExpire))
    conn.commit()

def saveDataInput():
    '''This function saves changes to the database and closes the current
    connection to the database.'''
    conn.commit()
    cursor.close()
    conn.close()



def addToDB(passwordsToCreate, passwordLength, monthsTilExp, daysTilExp):
    '''Uses the functions above to create the database table and add data
    dynamically and saves the changes to the database file'''
    createTable()
    for x in range(passToMake):
        dynamicDataInput(bitsToAscii.createAsciiStr(passwordLength), getCurrentDateStr(), getExpireDateStr(monthsTilExp, daysTilExp))
    saveDataInput()

