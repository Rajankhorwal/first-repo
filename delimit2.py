import mysql.connector
from new import fact

mydb = mysql.connector.connect(host="localhost", user="root", password="rajan@24", database="student")

print(mydb)

mycursor = mydb.cursor()


def fact(SQL):
    line = SQL.split(" ")
    str = " "
    s = 0
    while s == "DELIMITER":
       for s in line:

           str = str +" "+ s

       return str


SQL = """ USE student; DELIMITER $$ show tables $$"""
print(fact(SQL))
#
# for i in mycursor.execute(fact(SQL), multi=True):
#     pass
# for i in mycursor:
#     print(i)

# mycursor.callproc('delim')
# for result in mycursor.stored_results():
#     print(result.fetchall())

mydb.commit()

mycursor.close()
mydb.close()
mydb.disconnect()