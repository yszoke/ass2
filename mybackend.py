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

    """ This function adds the data to the DB"""
    def add_data(self,fileName,conn,table_name):
        try:
            data = pd.read_csv(fileName)
            data.to_sql(name='dataTable', con=conn, if_exists='append', index=False)
        except ValueError:
            return

    """This function performing a query, commit and close"""
    """ later on the function sorts the output and return the places that was found suitable"""
    def find_recommends(self, place, duration, num_of_results):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM dataTable WHERE StartStationName=? AND TripDurationinmin<=?", (place,duration))
        rows_location_before_sort=self.cur.fetchall()
        # sorting the output of the query according to the duration and the date
        rows_location=sorted(rows_location_before_sort, key=lambda x: (x[15], x[1]), reverse=True)
        # checks if the output of the query is empty
        if len(rows_location)==0:
            return rows_location
        places={}
        counter=0
        for i in range(len(rows_location)):
            # checks if the length of the places's list is not bigger than what the user asked for
            if counter<int(num_of_results):
                # checks if the place is not in the list and that its not the input from the user
                if rows_location[i][8] != place and rows_location[i][8] not in places:
                    places[rows_location[i][8]]=rows_location[i][15]
                    counter+=1
            else:
                return list(places.keys())

        return list(places.keys())