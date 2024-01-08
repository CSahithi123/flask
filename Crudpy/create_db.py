import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_villa.db')

#Create a Connection
cur = con.cursor()

#Drop user table if already exsist.
cur.execute("DROP TABLE IF EXISTS villa")
cur.execute("DROP TABLE IF EXISTS register")

#Create villa table  in db_villa database
sql ='''CREATE TABLE "villa" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT,
	"CONTACT"	TEXT,
    "PRICE" INTEGER,
    "SQFT" INTEGER,
    "OCCUPANCY" INTEGER
)'''
cur.execute(sql)

cur.execute('''
CREATE TABLE IF NOT EXISTS register(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            confirmpassword TEXT NOT NULL
)
            ''')

#commit changes
con.commit()

#close the connection
con.close()