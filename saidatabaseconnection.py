
import mysql.connector as db

class Database:
    def __init__(self):
        self.connection = db.connect(user="root", password="AdmiN@123!", host="127.0.0.1", database="saihitechfuels")

        print("data bases connected")
        self.cursor = self.connection.cursor()
        print("Cursor Created...")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        # print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

class SaiHiTech:
    def __init__(self, name=None, mobile=None, vehicle=None, image=None):
        self.name = name
        self.mobile = mobile
        self.vehicle = vehicle
        self.image = image

    def insert_sql_command(self):
        sql = "insert into bpcl values( '{name}', '{mobile}', '{vehicle}', '{image}')".format_map(vars(self))
        return sql

    def fetch_sql_command(self):
        return "select * from bpcl"
