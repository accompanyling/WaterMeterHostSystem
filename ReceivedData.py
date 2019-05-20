import socket
import time
import sqlite3
import re
def new_msg(data):
    b=re.findall('User(.*):(.*)L',data)
    if len(b)!=0:
        who = b[0][0].lower()
        num = float(b[0][1])

        if num==0:
            pass
        else:
            num=0.0018*num-0.0029
            do_job(who,num)#插入数据库，对数据库内容进行更新


def do_job(user,num):
    moment = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    moment_hour = time.strftime("%Y-%m-%d %H:%M:", time.localtime())
    duration = time.strftime("%Y-%m-%d", time.localtime())
    conn=sqlite3.connect("fitdatas_test.db")
    c=conn.cursor()
    c.execute("create table if not exists user_"+user+'(date text,num real)')
    c.execute('SELECT COUNT(*)  FROM user_' + user + ' where date = "' + duration + '"')
    if c.fetchall()[0][0] == 0:
        c.execute('INSERT INTO  user_' + user + ' VALUES (?,?)', (duration, num))
    else:
        c.execute('SELECT num FROM user_' + user + ' WHERE date="' + duration + '"')
        before = c.fetchall()[0][0]
        c.execute('UPDATE user_' + user + ' SET num=? WHERE date = ?', (num + before, duration))
    c.execute('INSERT INTO user_'+user+' VALUES(?,?)',(moment,num))
    conn.commit()
    conn.close()



address=('115.29.240.46',6000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.sendto("ep=EXK6YGGT38VZH9XS&pw=140210".encode('utf-8'),address)#先要发送验证消息
print(s)
print("Connection estabished")
while True:
    s.sendto("ep=SBDLT4B27E5NSNF4&pw=233666".encode('utf-8'), address)  # 先要发送验证消息

    data,addr=s.recvfrom(2048)
    if not data:
        print("client has exit")
        continue
    print("recieved",data,"from",addr)
    new_msg(data=str(data))#将获得的数据插入数据库
s.close()