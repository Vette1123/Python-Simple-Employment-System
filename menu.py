import os
from checks import *
from classes import *

# handle the menu


def new_employee():

    if(check_Employee()):
        print('Employee already exists')
        return
    else:
        email = input("Enter Employee Email : ")
        if(check(email)) == False:
            print('invalid email')
            return
        workmood = input("Enter Employee Workmood : ")
        salary = input("Enter Employee Salary : ")
        if(int(salary) < 1000):
            print('salary is too low, it must be 1000 or more')
            return
        is_manager = input("Is he/she Manager?, Please answer with 0/1 : ")
        office_id = input("Enter Employee Office Id : ")
        if(check_office_id(office_id) == True):
            print('Office Id is not valid')
            return
        office_name = input("Enter Employee Office Name : ")
        if(check_office_name(office_name) == True):
            print('Office Name is not valid')
            return
        employee = Employee(email, workmood, int(
            salary), is_manager, office_id)
        employee.add_employee()
        print('Employee added')


def hire_employee():
    if(check_Employee()):
        print('Employee already exists')
        return
    else:
        email = input("Enter Employee Email : ")
        if(check(email)) == False:
            print('invalid email')
            return
        workmood = input("Enter Employee Workmood : ")
        salary = input("Enter Employee Salary : ")
        if(int(salary) < 1000):
            print('salary is too low, it must be 1000 or more')
            return
        is_manager = input("Is he/she Manager?, Please answer with 0/1 : ")
        office_id = input("Enter Employee Office Id : ")
        if(check_office_id(office_id) == True):
            print('Office Id is not valid')
            return
        office_name = input("Enter Employee Office Name : ")
        if(check_office_name(office_name) == True):
            print('Office Name is not valid')
            return
        employee = Employee(email, workmood, int(
            salary), is_manager, office_id)
        office = Office(office_name)
        office.hire_employee(employee, office_id)
        print('Employee added')


def new_office():
    name = input("Enter Office Name : ")
    if(check_office_name(name) == False):
        print('Office Name was already taken')
        return
    if(checkString(name) == False):
        print('Office Name is not valid')
        return
    office = Office(name)
    office.add_office()
    print('Office added')


def delete_Employee():
    emp_id = input("Enter Employee Id : ")
    if(check_EmployeeWithoutID(emp_id)):
        Employee.fire_employee(emp_id)
        print('Employee deleted')
    else:
        print('Employee does not exist')


def display_all_employees():
    office_id = input("Enter Office Id : ")
    eksde = Office.get_all_employees(office_id)
    for i in eksde:
        print("Employee Id : ", i[0])
        print("Employee Email : ", i[1])
        print("Employee WorkMood : ", i[2])
        if(i[4] == 1):
            print("Employee Salary : Employee is Manager, You can't view his/her salary")
        else:
            print("Employee Salary : ", i[3])

        print("Employee Status(Manager) : ", bool(i[4]))
        print("Employee Office ID : ", i[5])
        print("Employee Reg Date: ", i[6])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def display_all_offices():
    eksde = Office.get_all_offices()
    for i in eksde:
        print("Office Id : ", i[0])
        print("Office Name : ", i[1])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def display_specific_employee():
    emp_id = input("Enter Employee Id : ")
    if(check_EmployeeWithoutID(emp_id)):
        eksde = Office.get_employee_by_id(emp_id)
        print("Employee Id : ", eksde[0][0])
        print("Employee Email : ", eksde[0][1])
        print("Employee WorkMood : ", eksde[0][2])
        if(eksde[0][4] == 1):
            print("Employee Salary : Employee is Manager, You can't view his/her salary")
        else:
            print("Employee Salary : ", eksde[0][3])

        print("Employee Status(Manager) : ", bool(eksde[0][4]))
        print("Employee Office ID : ", eksde[0][5])
        print("Employee Reg Date: ", eksde[0][6])
    else:
        print('Employee does not exist')


def menu():
    print("Welcome to Employee Management Record")
    dummy_display_lines()
    # Taking choice from user
    ch = input("Enter your Choice:  ")
    while(ch != 'q'):
        os.system('cls')
        if(ch == '1'):
            new_employee()
        elif(ch == '2'):
            new_office()
        elif(ch == '3'):
            delete_Employee()
        elif(ch == '4'):
            display_all_employees()
        elif(ch == '5'):
            display_all_offices()
        elif(ch == '6'):
            display_specific_employee()
        elif(ch == '7'):
            hire_employee()
        else:
            print("Invalid Choice")
        dummy_display_lines()
        ch = input("Enter your Choice ")


menu()
