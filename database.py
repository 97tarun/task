import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)
cursor = db_connection.cursor()
cursor.execute("create database if not exists school")
cursor.execute("use school")
cursor.execute("""
    create table if not exists students (
        student_id int auto_increment primary key,
        first_name varchar(50),
        last_name varchar(50),
        age int,
        grade float)
""")
insert_student = """
    insert into students (first_name, last_name, age, grade)
    values (%s, %s, %s, %s)
"""
student_data = ("Alice", "Smith", 18, 95.5)
cursor.execute(insert_student, student_data)
db_connection.commit()
update_grade = """
    update students
    set grade = %s
    where first_name = %s
"""
new_grade = (97.0, "Alice")
cursor.execute(update_grade, new_grade)
db_connection.commit()
delete_student = """
    delete from students
    where last_name = %s
"""
student_to_delete = ("Smith",)
cursor.execute(delete_student, student_to_delete)
db_connection.commit()
cursor.execute("select * from students")
students = cursor.fetchall()
for student in students:
    print("Student Id:", student[0])
    print("First Name:", student[1])
    print("Last Name:", student[2])
    print("Age:", student[3])
    print("Grade:", student[4])
    print()
cursor.close()
db_connection.close()
