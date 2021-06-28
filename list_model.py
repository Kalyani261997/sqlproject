import psycopg2
from psycopg2.extras import RealDictCursor
from flask import make_response

class list_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def list_model(self,post_data):
        self.cur.execute("INSERT INTO list(data,status,created_by)values('"+post_data["data"]+"','"+post_data["status"]+"',"+post_data["created_by"]+")") 
        # rows = self.cur.fetchall()n
        # print(post_data["created_by"])
        #print("INSERT INTO list(data,status,created_by)values('"+post_data["data"]+"','"+post_data["status"]+"',"+post_data["created_by"]+")")
        return make_response({"created_by":post_data},200)