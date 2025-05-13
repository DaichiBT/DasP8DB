import mysql.connector


connection = mysql.connector.connect(
   user='daichit',
   password='230958233',
   host='10.8.37.226',
   database='daichit_db'
)


cursor = connection.cursor()


student_id = input("Enter a student ID: ")


query = f"CALL Get_Student_Schedule({student_id});"
cursor.execute(query)


print()
for row in cursor:
   print(f"Period: {row[0]}")
   print(f"Course: {row[1]}")
   print(f"Room: {row[2]}")
   print(f"Teacher: {row[3]} {row[4]}")
   print()


cursor.close()
connection.close()
