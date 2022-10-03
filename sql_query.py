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
                                            "brend"	TEXT,
                                            "founder"	TEXT,
                                            "number"	INTEGER,
                                            "location"	TEXT
                                        );""")

    """
                                        Functions for adding data
    """
    def add_brend(self, city, brend):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {city} (brend) VALUES (?)", (brend,) )

    def add_founder(self, city, founder):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {city} (founder) VALUES (?)", (founder,) )

    def add_number(self, city, number):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {city} (number) VALUES (?)", (number,) )

    def add_location(self, city, location):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {city} (location) VALUES (?)", (location,) )

    """                                  Get a list of stores                            """
    def get_shop(self,city):
        with self.connection:
            # get in the form of a dataframe
            sql_query = pd.read_sql_query(f"SELECT * FROM {city}", self.connection)
            return pd.DataFrame(sql_query, columns=['brend', 'founder', 'number', "location"])
            # get in the form of a list =>
            # return self.cursor.execute(f"SELECT * FROM {city}").fetchall()


    """                                 
                                        Functions for remove data
    """
    def remove_data(self,city,brend=None, founder=None, number=None):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM {city} WHERE brend = ? OR founder = ? OR number = ?", (brend, founder, number,) )



# db = Database('client.db')
# db.create_table("Samarqand")
# db.add_brend(city="Toshkent", brend="flowers")
# db.add_founder(city="Toshkent", founder="Alisher")
# db.add_number(city="Samarqand", number=998977099197)
# db.remove_data(city="Toshkent", brend="flowers")
# db.remove_data(city="Toshkent", founder="Alisher")

# print(db.get_shop(city="Toshkent"))