import MySQLdb


def connectToDB():
    con = MySQLdb.connect('localhost', 'root', 'Awad36148', 'python')
    return con


def createOfficeTable():
    con = connectToDB()
    mycursor = con.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS office(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL)")


createOfficeTable()


def createEmpTable():
    con = connectToDB()
    mycursor = con.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS employee(id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(30) NOT NULL, workmood VARCHAR(30) NOT NULL, salary int NOT NULL,is_manager BOOLEAN NOT NULL,office_id INT NOT NULL,reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY (office_id) REFERENCES office(id))")


createEmpTable()
