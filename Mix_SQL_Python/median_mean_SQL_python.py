"""
Data-Driven Astronomy

@author: lauratrain99
date: 01/06/2020

This program  runs a SQL simple program using Psycopg2 module.
It calculates the mean and median of a selected column
in either Star or Planet table
"""

import psycopg2
import numpy as np
def column_stats(tablename,columnname):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('SELECT '+ columnname + ' FROM ' + tablename + ';')
  records = cursor.fetchall()
  records = np.array(records)
  return np.mean(records), np.median(records)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  print(column_stats('Star','t_eff'))