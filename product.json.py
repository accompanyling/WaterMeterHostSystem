import sqlite3
import json
import time
import sys
import os
import shutil

user_list=['17754928919','13028390277']

class User:
    def __init__(self,name,date,num):
        self.name=name
        self.data=Data(date,num)
    def __repr__(self):
        return repr((self.name,self.data.date,self.data.num))

class Data:
    def __init__(self,date,num):
        self.date=date
        self.num=num
    def __repr__(self):
        return repr((self.date,self.num))


t=1
while True:
    time.sleep(1)
    conn = sqlite3.connect("fitdatas_test.db")
    c = conn.cursor()
    for user in user_list:
        person = []
        user_name = 'user_' + user
        result = c.execute("SELECT date,num FROM " + user_name).fetchall()
        for i in range(len(result)):
            date = result[i][0]
            num = result[i][1]
            user_example = User(user_name, date, num)
            person.append(user_example)
        json_str = json.dumps(person, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        if user_name == 'user_17754928919':
            f = open('1.json', 'w')
            print(json_str, file=f)
        if user_name == 'user_13028390277':
            f = open('2.json', 'w')
            print(json_str, file=f)
    conn.commit()
    conn.close()
    print(t)
    t+=1
    shutil.copyfile('1.json','C:\\DISK\\Code_Store\\Node_Store\\Node_For_Water\\public\\1.json')
    shutil.copyfile('2.json','C:\\DISK\\Code_Store\\Node_Store\\Node_For_Water\\public\\2.json')

