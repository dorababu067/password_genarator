import sqlite3

conn = sqlite3.connect('mylocal.db')
#print("your database test is created succefully")
cur = conn.cursor()
#creating tabel
#result = cur.execute('''CREATE TABLE password(password text,purpose text)''')
#conn.commit()
#print("Table object Addres:",result)
#print(cur.execute("INSERT INTO pword VALUES (?,?)",(password.gen_password,password.purpose)))
#
#print("Data Inserted Sucesfylly")
#conn.commit()
#
#print("Your database_connection closed")