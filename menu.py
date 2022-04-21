import MySQLdb
import re
import os


# email validation check
emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if(re.fullmatch(emailRegex, email)):
        return True
    else:
        return False


def checkString(str):
    if(re.fullmatch('[a-zA-Z\s]+$', str)):
        return True
    else:
        return False


def connectToDB():
    con = MySQLdb.connect('localhost', 'root', 'Awad36148', 'python')
    return con


def createEmpTable():
    con = connectToDB()
    mycursor = con.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS employee(id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(30) NOT NULL, workmood VARCHAR(30) NOT NULL, salary int NOT NULL,is_manager BOOLEAN NOT NULL,office_id INT NOT NULL,reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY (office_id) REFERENCES office(id))")


# person class
createEmpTable()


def createOfficeTable():
    con = connectToDB()
    mycursor = con.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS office(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL)")


createOfficeTable()


class Person:
    healthRate = 0

    def __init__(self, full_name, money, sleepmood, healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.healthRate = healthRate

    # sleep method
    @ classmethod
    def sleep(cls, hours):
        if(hours == 7):
            cls.sleepmood = 'happy'
            return cls.sleepmood
        elif(hours < 7):
            cls.sleepmood = 'tired'
            return cls.sleepmood
        elif(hours > 7):
            cls.sleepmood = 'lazy'
            return cls.sleepmood
        else:
            return 'please enter values in range'

    # eat method
    @ classmethod
    def eat(cls, meals):
        if(meals == 3):
            cls.healthRate = 100
            return cls.healthRate
        elif(meals == 2):
            cls.healthRate = 75
            return cls.healthRate
        elif(meals == 1):
            cls.healthRate = 50
            return cls.healthRate
        else:
            return 'please enter values in range'

    @ classmethod
    def buy(cls, items):
        if(items == 1):
            cls.money = cls.money - 10
        else:
            return 'please enter values in range'

    def healthRate(self, healthRate):
        if(healthRate > 100 or healthRate < 0):
            return 'health rates must be between 0 and 100'
        else:
            self.healthRate = healthRate


# employee class
class Employee(Person):

    def __init__(self, email, workmood, salary, is_manager, office_id):
        self.office_id = office_id
        if(check(email)):
            self.email = email
        else:
            print('invalid email')
        self.workmood = workmood
        if(salary < 1000):
            print('salary is too low, it must be 1000 or more')
        else:
            self.salary = salary
        self.is_manager = is_manager

    def send_email(self, to, subject, body, receiver_name):
        tempFile = open('file.txt', 'w')
        Line = [str(to), ",", str(subject), ",",
                str(body), ",", str(receiver_name)]
        tempFile.writelines(Line)
        tempFile.close()

    def work(self, hours):
        if(hours == 8):
            self.workmood = 'happy'
            return self.workmood
        elif(hours > 8):
            self.workmood = 'tired'
            return self.workmood
        elif(hours < 8):
            self.workmood = 'lazy'
            return self.workmood

    def add_employee(self):
        con = connectToDB()
        mycursor = con.cursor()
        mycursor.execute("INSERT INTO employee(email,workmood,salary,is_manager,office_id) VALUES(%s,%s,%s,%s,%s)",
                         (self.email, self.workmood, self.salary, self.is_manager, self.office_id))
        con.commit()
        con.close()

    @classmethod
    def fire_employee(cls, id):
        # fire employee by id
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "DELETE FROM employee WHERE id = " + str(id))
        cont.commit()
        return 'employee fired'


class Office(Employee):

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all_employees(cls, id):
        # return all employees
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "SELECT * FROM employee WHERE office_id = " + str(id))
        myresult = mycursor.fetchall()
        return myresult

    @classmethod
    def get_employee_by_id(cls, id):
        # get employee by id
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "SELECT * FROM employee WHERE id = " + str(id))
        myresult = mycursor.fetchall()
        return myresult

    def hire_employee(self, employee, offce_id):
        # hire employee
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "INSERT INTO employee(email, workmood, salary, is_manager, office_id) VALUES ('" + employee.email + "','" + employee.workmood + "','" + str(employee.salary) + "','" + str(employee.is_manager) + "','" + str(offce_id) + "')")
        cont.commit()
        cont.close()

    @classmethod
    def get_all_offices(cls):
        # return all offices
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute("SELECT * FROM office")
        myresult = mycursor.fetchall()
        return myresult

    def add_office(self):
        # add office
        cont = connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "INSERT INTO office(name) VALUES('" + self.name + "')")
        mycursor.execute("commit")
        return 'office added'
# ##############################################################################


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


###############################################################################
# new employee


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


def display_all_offices():
    eksde = Office.get_all_offices()
    for i in eksde:
        print("Office Id : ", i[0])
        print("Office Name : ", i[1])


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
