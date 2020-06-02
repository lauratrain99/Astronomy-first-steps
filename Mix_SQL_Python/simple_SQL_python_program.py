"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program runs a SQL simple program using Psycopg2 module.
"""


import psycopg2
def select_all(SQLdb):
  conn = psycopg2.connect(dbname = 'db', user = 'grok')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM ' +SQLdb+ ';')
  records = cursor.fetchall()
  return records

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  print(select_all('Star'))
  print(select_all('Planet'))