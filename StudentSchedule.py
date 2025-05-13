import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        user='daichit',
        password='230958233',
        host='10.8.37.226',
        database='daichit_db'
    )
    return connection

def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()
    return results

def get_student_schedule(student_id):
    statement = f"CALL Get_Student_Schedule({student_id});"
    return execute_statement(get_database_connection(), statement)

student_id = input("Enter a student ID: ")
results = get_student_schedule(student_id)

for result in results:
    period = result[0]
    class_name = result[1]
    room = result[2]
    teacher_first = result[3]
    teacher_last = result[4]

    print(f"Period: {period}")
    print(f"Course: {class_name}")
    print(f"Room: {room}")
    print(f"Teacher: {teacher_first} {teacher_last}")
    print()
