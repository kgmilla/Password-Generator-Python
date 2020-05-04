import sqlite3
import time
import datetime
from dateutil.relativedelta import relativedelta
import bitsToAscii

passwordLength = 16
monthsExp = 2
daysExp = 0
passwordsToCreate = 5

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

def getCurrentDateStr():
    currentTime = time.time()
    return str(datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d'))

def getExpireDateStr(monthsUntilPassExp, daysUntilPassExp):
    currentTime = datetime.datetime.utcnow()
    expDate = currentTime + relativedelta(months=monthsUntilPassExp, days=daysUntilPassExp)
    return str(expDate.date())


def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS passwords(passwords TEXT, dateCreated REAL, dateExpire REAL)')


def dynamicDataInput(password, dateCreated, dateExpire):
    cursor.execute("INSERT INTO passwords (passwords, dateCreated, dateExpire) Values (?, ?, ?)",
    (password, dateCreated, dateExpire))
    conn.commit()

def saveDataInput():
    conn.commit()
    cursor.close()
    conn.close()


createTable()
for x in range(passwordsToCreate):
    dynamicDataInput(bitsToAscii.createAsciiStr(passwordLength), getCurrentDateStr(), getExpireDateStr(monthsExp, daysExp))

saveDataInput()

