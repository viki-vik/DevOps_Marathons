#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('index.db')

conn.execute('CREATE TABLE DATES(ID INTEGER PRIMARY KEY NOT NULL, JUST_NOW TEXT NOT NULL);')

conn.commit()

conn.close()
