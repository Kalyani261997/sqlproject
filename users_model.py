import time
import datetime
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import make_response
from jwt import jwt
import json


class users_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        
    
    # def login_model(self, post_data):
    #     try:
    #         print(post_data)
    #         qry = "select * from users where email='"+post_data["email"]+"' AND password='"+post_data["password"]+"' AND status='a'"
    #         self.cur.execute(qry)
    #         rows = self.cur.fetchall()
    #         if len(rows) > 0:
    #             print(rows)
    #             token = jwt.encode({"data":rows,"exp":datetime.datetime.utcnow()+datetime.timedelta(days=100)},"EncryptionKey")
    #             return make_response({"payload":token},200)
    #         else:
    #             return make_response({"error":"Please check the id or password"},403)

    #     except Exception as e:
    #         return make_response({"error":str(e)},500)

    def add_user_model(self,post_data):
        try:
            self.cur.execute("Insert into users(status,full_name,email,phone,password)values('"+post_data["status"]+"','"+post_data["full_name"]+"','"+post_data["email"]+"','"+post_data["phone"]+"','"+post_data["password"]+"')")
            return make_response({"success":"user created"},200)

        except Exception as e:
            return make_response({"error":str(e)},500)


    def user_profile_model(self,user_id):
        self.cur.execute("SELECT * FROM users WHERE id="+user_id) 
        select = self.cur.fetchall()
        res = {"data":select}
        if len(select) == 0:
            res = {"message": "no data found"}
        return make_response(res,200)

    
    def mylist_model(self,id):
        self.cur.execute("SELECT * from list where created_by="+id) 
        select = self.cur.fetchall()
        res = {"data":select}
        if len(select) == 0:
            res = {"message": "no data found"}
        return make_response(res,200)

    def mydate_model(self,date1,date2):
        self.cur.execute("SELECT * FROM list WHERE created_on::date>='"+date1+"' AND created_on::date<='"+date2+"'") 
        select = self.cur.fetchall()
        res = {"data":select}
        if len(select) == 0:
            res = {"message": "no data found"}
        return make_response(res,200)
    
      


        

    