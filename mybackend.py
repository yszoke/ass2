import sqlite3
from sqlite3 import Error
import pandas as pd

class Database:

    """ This function opens the connection and creates (if does not exists) a database"""
    def __init__(self):
        """Creating a connection"""
        self.conn = sqlite3.connect('database.db')

        """Creating a cursor object"""
        self.cur = self.conn.cursor()

        """Performing a query, commit and close"""

        ## checks if the table already exists
        check_if_exists = self.cur.execute(
            ''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='dataTable' ''')
        if check_if_exists.fetchone()[0] != 1:
            self.cur.execute("CREATE TABLE IF NOT EXISTS dataTable ("
                             "TripDuration INTEGER,"
                             "StartTime DATE ,"
                             "StopTime DATE ,"
                             "StartStationID INTEGER,"
                             " StartStationName MESSAGE_TEXT,"
                             " StartStationLatitude REAL,"
                             " StartStationLongitude REAL,"
                             " EndStationID INTEGER,"
                             " EndStationName MESSAGE_TEXT,"
                             " EndStationLatitude REAL,"
                             " EndStationLongitude REAL,"
                             " BikeID INTEGER, UserType MESSAGE_TEXT,"
                             " BirthYear INTEGER, Gender INTEGER,"
                             " TripDurationinmin INTEGER)")

            self.add_data("BikeShare.csv", self.conn,"dataTable")
        self.conn.commit()
        self.conn.close() # closes the connection


    def add_data(self,fileName,conn,table_name):
        try:
            data = pd.read_csv(fileName)
            data.to_sql(name='dataTable', con=conn, if_exists='append', index=False)
        except ValueError:
            return

    """Performing a query, commit and close"""
    def find_recommends(self, place, duration, recommends):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM dataTable WHERE StartStationName=?", (place,))
        rows_location=self.cur.fetchall()
        if len(rows_location)==0:
            return rows_location
        ############### should return a pop up
        self.cur.execute("SELECT * FROM dataTable WHERE TripDurationinmin=?", (duration,))
        rows_duration=self.cur.fetchall()
        return "test"