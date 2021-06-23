import psycopg2
from psycopg2.extras import RealDictCursor
from flask import make_response

class users_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        

    def signup_model(self):
        print("Please sign up your account:")


    def max_model(self):
        self.cur.execute("SELECT max(Stipend) FROM students")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)

    def avg_model(self):
        self.cur.execute("SELECT avg(stipend) from students")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)

    def sum_model(self):
        self.cur.execute("SELECT SUM(stipend) from students")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)

    def where_model(self):
        self.cur.execute("SELECT * from students where stipend=3000")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)

    def desc_model(self):
        self.cur.execute("SELECT * from students order by stipend DESC")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)

    def asc_model(self):
        self.cur.execute("SELECT * from students order by stipend ASC")
        rows = self.cur.fetchall()
        return make_response({"data":rows},201)
        