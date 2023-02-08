import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="college"
)
command_handler = db.cursor(buffered=True)


def student_session()
    print("LogIn Successful")
    print(f"Welcome student {username}")

    while 1:
        print("")
        print("Student Menu")
        print("1. View register")
        print("2. Download register")
        print("3. Logout")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("View Register")
            command_handler.execute("SELECT * FROM attendance WHERE username= %s AND privilege = 'student'")


def teacher_session():
    print("Login success")
    print("Welcome Teacher")
    while 1:
        print("")
        print("Teacher Menu")
        print("1. Mark student register")
        print("2. View register")
        print("3. Logout")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("Mark student register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date: DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                # Present | Absent | Late
                status = input(str(f'Status for {record} P/A/L: '))
                query_vals = (record, date, status)
                command_handler.execute("INSERT into attendance (username, date, status) VALUES (%s,%s,%s)", query_vals)
                db.commit()
                print(f"{record} marked as {status}")

        elif user_option == "2":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers")
            for record in records:
                print(record)

        elif user_option == "3":
            break
        else:
            print("No valid option selected")



def admin_session():
    print("Login success")
    print("Welcome admin")
    while 1:
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. delete existing teacher")
        print("5. Logout")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("Register new student")
            username = input(str("Student username: "))
            password = input(str("Student password: "))

            query_vals = (username, password)
            command_handler.execute("Insert into users (username, password1, privilege) VALUES (%s, %s,'student')",
                                    query_vals)
            db.commit()
            print(f"{username} has been registered as a student")

        elif user_option == "2":
            print("")
            print("Register new teacher")
            username = input(str("Teacher username: "))
            password = input(str("Teacher password: "))

            query_vals = (username, password)
            command_handler.execute("Insert into users (username, password1, privilege) VALUES (%s, %s,'teacher')",
                                    query_vals)
            db.commit()
            print(f"{username} has been registered as a teacher")

        elif user_option == "3":
            print("")
            print("Delete student")
            username = input(str("Student username: "))
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("No records deleted")
            else:
                print(f"Student {username} has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Teacher")
            username = input(str("Teacher username: "))
            query_vals = (username, "Teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("No records deleted")
            else:
                print(f"Teacher {username} has been deleted")

        elif user_option == "5":
            print("Logged out")
            break


def auth_student():
    print("")
    print(f"Welcome Student")
    print("")

    username = input(str("Username: "))
    password = input(str("Password: "))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'STUDENT'", query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognised")
    else:
        student_session()



def auth_teacher():
    print("")
    print("Teachers Login")
    print("")
    username = input(str("Username: "))
    password = input(str("Password: "))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password1 = %s AND privilege = 'teacher'",
                            query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognised")
    else:
        teacher_session()


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password!")
    else:
        print("Login details not recognised")


def main():
    while 1:
        print("********** Welcome to the college **********")
        print("")
        print("1. Student_Login")
        print("2. Teacher_Login")
        print("3. Admin Login")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
            print("Admin LogIn")

        else:
            print("No valid option was selected")


main()
