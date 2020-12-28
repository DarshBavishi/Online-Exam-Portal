import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tabulate import tabulate

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='YOUR_PASSWORD')  

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE EXAM_PORTAL")
        print("Database Created!")
        
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='EXAM_PORTAL',
                                         user='root',
                                         password='YOUR_PASSWORD')  
     
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

# Student Table
try:
    mySql_Create_Table_Query = """CREATE TABLE StudentInfo (
                             RollNo int(9) NOT NULL,
                             Name varchar(100) NOT NULL,
                             Branch varchar(100) NOT NULL,
                             PRIMARY KEY (RollNo)) """

    result = cursor.execute(mySql_Create_Table_Query)
    print("StudentInfo Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

# Scores Table
try :
    mySql_Create_Table_Query = """CREATE TABLE Scores (
                             RollNo int(9) NOT NULL,
                             Score int(3) NOT NULL ,
                             PRIMARY KEY (RollNo),
                             FOREIGN KEY (RollNo) REFERENCES StudentInfo(RollNo)) """
    
    result = cursor.execute(mySql_Create_Table_Query)
    print("Scores Table created successfully ")
    
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

# Filling Info in StudentInfo Table
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070060,"darsh bavishi","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070061,"joy purohit","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070062,"siddharth shah","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070063,"bhavya mehta","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070064,"dhruvin gandhi","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070065,"vaishnavi shah","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070066,"parth shah","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070067,"amit shah","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070068,"abhishek joshi","CS") """)
cursor.execute("""INSERT INTO StudentInfo (RollNo,Name,Branch) 
            VALUES (191070069,"kush kothari","CS") """)
connection.commit()




#Filling Scores Table on DB
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070060,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070061,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070062,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070063,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070064,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070065,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070066,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070067,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070068,0) """)
cursor.execute("""INSERT INTO Scores (RollNo,Score) 
            VALUES (191070069,0) """)        
connection.commit()

