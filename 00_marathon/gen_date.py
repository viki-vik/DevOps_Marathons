#!/usr/bin/env python3

import os
import datetime
import sqlite3

now = datetime.datetime.now()

def gen_html(ct):
    time_stamp = str(ct)
    f = open("index.html","w")
    f.write('<H1> Welcome to  My awesome app <H1>'+time_stamp)
    f.close()

def write_to_db(db,table,time_stamp):
    sql = f'INSERT INTO {table}(JUST_NOW) VALUES(?)'
    val = [f'{time_stamp}']
    conn = sqlite3.connect(db)
    conn.execute(sql,val)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    gen_html(now)
    write_to_db('index.db' ,'DATES' ,now)
