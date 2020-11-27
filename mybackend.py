import sqlite3
from sqlite3 import Error
import pandas as pd

class database:
    def __init__(self):
        """Creating a connection"""
        self.conn = sqlite3.connect('database.db')

        """Creating a cursor object"""
        self.cur = self.conn.cursor()

        """Performing a query, commit and close"""
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
        self.conn.close()


    def add_data(self,fileName,conn,table_name):
        try:
            data = pd.read_csv(fileName)
            data.to_sql(name='dataTable', con=conn, if_exists='append', index=False)
        except ValueError:
            return

    """Performing a query, commit and close"""
    def view(self):
        # conn=sqlite3.connect('lite.db')
        # cur=conn.cursor()
        self.cur.execute("SELECT * FROM dataTable")
        rows=self.cur.fetchall()
        for row in rows:
            print (row )
