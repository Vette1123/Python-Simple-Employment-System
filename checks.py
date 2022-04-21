import re
from dbConnection import connectToDB


def check(email):
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(emailRegex, email)):
        return True

    return False


def checkString(str):
    if(re.fullmatch('[a-zA-Z\s]+$', str)):
        return True

    return False


def check_office_name(name):
    # check if office name is unique
    cont = connectToDB()
    mycursor = cont.cursor()
    mycursor.execute(
        "SELECT * FROM office WHERE name = '" + name + "'")
    myresult = mycursor.fetchall()
    if(myresult):
        return False
    else:
        return True


def check_office_id(id):
    # check if office id is unique
    cont = connectToDB()
    mycursor = cont.cursor()
    mycursor.execute(
        "SELECT * FROM office WHERE id = '" + id + "'")
    myresult = mycursor.fetchall()
    if(myresult):
        return False
    else:
        return True


def check_Employee():
    emp_id = input("Enter Employee Id : ")
    cont = connectToDB()
    mycursor = cont.cursor()
    mycursor.execute(
        "SELECT * FROM employee WHERE id = " + str(emp_id))
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        return False
    else:
        return True


def check_EmployeeWithoutID(emp_id):
    cont = connectToDB()
    mycursor = cont.cursor()
    mycursor.execute(
        "SELECT * FROM employee WHERE id = " + str(emp_id))
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        return False
    else:
        return True


def dummy_display_lines():
    print("Enter your Choice ")
    print("1 to Add Employee")
    print("2 to Add Office ")
    print("3 to Fire Employee")
    print("4 to Display All Employees")
    print("5 to Display All Offices")
    print("6 to Display Specific Employee")
    print("7 to Hire Employee into an office")
    print("q to Exit")
