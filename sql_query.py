import sqlite3
import pandas as pd

# from aiogram.dispatcher.filters.state import StatesGroup, State


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, city):
        with self.connection:
            return self.cursor.execute(f"""CREATE TABLE  IF NOT EXISTS {city} (
                                            "founder"	TEXT,
                                            "number"	INTEGER,
                                            "loc1"	INTEGER,
                                            "loc2" INTEGER
                                        );""")

    """
                                        Functions for adding data
    """
    def add_data(self, city, founder, number, loc1, loc2):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {city} (founder,number,loc1,loc2) VALUES (?,?,?,?)", (founder,number,loc1, loc2 ) )
    """                                  Get a list of stores                            """
    def get_shop(self,city):
        with self.connection:
            # get in the form of a dataframe
            sql_query = pd.read_sql_query(f"SELECT * FROM {city}", self.connection)
            return pd.DataFrame(sql_query, columns=['founder', 'number', "loc1", "loc2"])
            # get in the form of a list =>
            # return self.cursor.execute(f"SELECT * FROM {city}").fetchall()


    """                                 
                                        Functions for remove data
    """
    def remove_data(self,city,brend=None, founder=None, number=None):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM {city} WHERE brend = ? OR founder = ? OR number = ?", (brend, founder, number,) )


#
# db = Database('client.db')
# db.create_table("Samarqand")
# # db.add_founder(city="Samarqand", founder="Alisher")
# # db.add_number(city="Samarqand", number=998977099197)
# # db.add_location(city="Samarqand", location= "12.45678 45.6789" )
# db.add_data(city="Samarqand", founder="Alisher", number=998977099197, location= "12.45678 45.6789")
#
# print(db.get_shop(city="Samarqand"))