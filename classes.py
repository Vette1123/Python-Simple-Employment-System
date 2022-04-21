import dbConnection
from checks import *


class Person:

    def __init__(self, full_name, money, sleepmood, healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.healthRate = healthRate

    def sleep(self, hours):
        if(hours == 7):
            self.sleepmood = 'happy'
            return self.sleepmood
        elif(hours < 7):
            self.sleepmood = 'tired'
            return self.sleepmood
        elif(hours > 7):
            self.sleepmood = 'lazy'
            return self.sleepmood
        else:
            return 'please enter values in range'

    def eat(self, meals):
        if(meals == 3):
            self.healthRate = 100
            return self.healthRate
        elif(meals == 2):
            self.healthRate = 75
            return self.healthRate
        elif(meals == 1):
            self.healthRate = 50
            return self.healthRate
        else:
            return 'please enter values in range'

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
        try:
            tempFile = open('file.txt', 'w')
            Line = [str(to), ",", str(subject), ",",
                    str(body), ",", str(receiver_name)]
            tempFile.writelines(Line)
            tempFile.close()
        except:
            print('error')

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
        con = dbConnection.connectToDB()
        mycursor = con.cursor()
        mycursor.execute("INSERT INTO employee(email,workmood,salary,is_manager,office_id) VALUES(%s,%s,%s,%s,%s)",
                         (self.email, self.workmood, self.salary, self.is_manager, self.office_id))
        con.commit()
        con.close()

    @classmethod
    def fire_employee(cls, id):
        # fire employee by id
        cont = dbConnection.connectToDB()
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
        cont = dbConnection.connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "SELECT * FROM employee WHERE office_id = " + str(id))
        myresult = mycursor.fetchall()
        return myresult

    @classmethod
    def get_employee_by_id(cls, id):
        # get employee by id
        cont = dbConnection.connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "SELECT * FROM employee WHERE id = " + str(id))
        myresult = mycursor.fetchall()
        return myresult

    def hire_employee(self, employee, offce_id):
        cont = dbConnection.connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "INSERT INTO employee(email, workmood, salary, is_manager, office_id) VALUES ('" + employee.email + "','" + employee.workmood + "','" + str(employee.salary) + "','" + str(employee.is_manager) + "','" + str(offce_id) + "')")
        cont.commit()
        cont.close()

    @classmethod
    def get_all_offices(cls):
        cont = dbConnection.connectToDB()
        mycursor = cont.cursor()
        mycursor.execute("SELECT * FROM office")
        myresult = mycursor.fetchall()
        return myresult

    def add_office(self):
        cont = dbConnection.connectToDB()
        mycursor = cont.cursor()
        mycursor.execute(
            "INSERT INTO office(name) VALUES('" + self.name + "')")
        mycursor.execute("commit")
        return 'office added'
