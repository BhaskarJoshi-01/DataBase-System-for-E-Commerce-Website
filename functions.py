import datetime

# import customer
# from customer import *
# from customer_address import *
# from customer_phonenumber import *
# from employee_address import *
# from employee_phonenumber import *
# import customer_address

# import datetime
# from functions import *


def customer(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Customer;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["First_Name"], info["Last_Name"] = (
                    input("Name (First_Name Last_Name): ")).split(' ')
                info["DOB"] = input("DOB (YYYY-MM-DD): ")
                info["Gender"] = input("Gender (Male, Female, Others): ")
                info["Email"] = input("Email: ")

                query = "INSERT INTO Customer(Customer_ID, First_Name, Last_Name, DOB, Gender,Email) VALUES('%d', '%s', '%s', '%s', '%s', '%s')" % (
                    info["Customer_ID"], info["First_Name"],  info["Last_Name"], info["DOB"], info["Gender"], info["Email"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Customer_ID to modify: "))
                query = "SELECT * FROM Customer where Customer_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Customer_ID: ")
                if info["ID"] != "":
                    row["Customer_ID"] = int(info["ID"])
                info["name"] = input("Name (First_Name Last_Name): ")
                if info["name"] != "":
                    row["First_Name"], row["Last_Name"] = info["name"].split(
                        ' ')
                info["DOB"] = input("DOB (YYYY-MM-DD): ")
                if info["DOB"] != "":
                    row["DOB"] = info["DOB"]
                info["Gender"] = input("Gender (Male, Female, Others): ")
                if info["Gender"] != "":
                    row["Gender"] = info["Gender"]
                info["Email"] = input("Email : ")
                if info["Email"] != "":
                    row["Email"] = info["Email"]
                query = "UPDATE Customer SET Customer_ID = '%d', First_Name = '%s', Last_Name = '%s', DOB = '%s', Gender = '%s', Email = '%s' WHERE Customer_ID = '%d'" % (
                    row["Customer_ID"], row["First_Name"], row["Last_Name"], row["DOB"], row["Gender"], row["Email"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Customer_ID you want to delete: "))
                query = "DELETE FROM Customer WHERE Customer_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def customer_address(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Customer_Address;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["Pin"] = int(input("Pin : "))
                info["State"] = input("State: ")
                info["Country"] = input("Country: ")
                info["Street_Name"] = input("Street_Name: ")
                query = "INSERT INTO Customer_Address(Customer_ID, Pin, State, Country, Street_Name) VALUES('%d', '%d', '%s', '%s', '%s')" % (
                    info["Customer_ID"], info["Pin"], info["State"], info["Country"], info["Street_Name"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Customer_ID to modify: "))
                pin = int(input("Enter Current Pin: "))
                state = input("Enter Current State: ")
                country = input("Enter Current Country: ")
                street = input("Enter Current Street Name: ")

                query = "SELECT * FROM Customer_Address where Customer_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    ID, pin, state, country, street)
                # print("Ho")
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Customer_ID"] = input("Customer_ID: ")
                if info["Customer_ID"] != "":
                    row["Customer_ID"] = int(info["Customer_ID"])
                info["Pin"] = input("Pin: ")
                if info["Pin"] != "":
                    row["Pin"] = int(info["Pin"])
                info["State"] = input("State: ")
                if info["State"] != "":
                    row["State"] = info["State"]
                info["Country"] = input("Country: ")
                if info["Country"] != "":
                    row["Country"] = (info["Country"])
                info["Street_Name"] = input("Street_Name: ")
                if info["Street_Name"] != "":
                    row["Street_Name"] = (info["Street_Name"])
                # print("Ho")

                query = "UPDATE Customer_Address SET Customer_ID = '%d', Pin = '%d', State = '%s', Country = '%s', Street_Name = '%s' WHERE Customer_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    row["Customer_ID"], row["Pin"], row["State"], row["Country"], row["Street_Name"], ID, pin, state, country, street)
                cur.execute(query)
                con.commit()
                # print("Ho2")

                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                # info = {}
                ID = int(
                    input("Enter the Customer_ID whose address you want to delete: "))
                pin = int(input("Enter  Pin: "))
                state = input("Enter  State: ")
                country = input("Enter Country: ")
                street = input("Enter Street Name: ")

                query = "DELETE FROM Customer_Address WHERE Customer_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    ID, pin, state, country, street)
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def customer_phonenumber(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Customer_Phone_Number;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["Phone_Number"] = int(input("Phone_Number : "))
                query = "INSERT INTO Customer_Phone_Number(Customer_ID, Phone_Number) VALUES('%d', '%s')" % (
                    info["Customer_ID"], info["Phone_Number"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Customer_ID to modify: "))
                query = "SELECT * FROM Customer where Customer_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Customer_ID: ")
                if info["ID"] != "":
                    row["Customer_ID"] = int(info["ID"])
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                # 	row["First_Name"], row["Last_Name"] = info["name"].split(' ')
                # info["DOB"] = input("DOB (YYYY-MM-DD): ")
                # if info["DOB"] != "":
                # 	row["DOB"] = info["DOB"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                # 	row["Gender"] = info["Gender"]
                info["Phone_Number"] = input("Phone_Number : ")
                if info["Phone_Number"] != "":
                    row["Phone_Number"] = int(info["Phone_Number"])
                query = "UPDATE Customer_Phone_Number SET Customer_ID = '%d',  Phone_Number = '%d' WHERE Customer_ID = '%d'" % (
                    row["Customer_ID"], row["Phone_Number"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Customer_ID whose phone number you want to delete: "))
                query = "DELETE FROM Customer_Phone_Number WHERE Customer_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def employee(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Employee;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Employee_ID"] = int(input("Employee_ID: "))
                info["First_Name"], info["Last_Name"] = (
                    input("Name (First_Name Last_Name): ")).split(' ')
                info["Email"] = input("Email: ")
                info["Supervisor_ID"] = int(input("Supervisor_ID: "))
                info["Department_Name"] = input("Department_Name: ")
                info["Salary"] = int(input("Salary: "))
                info["DOB"] = input("DOB (YYYY-MM-DD): ")
                info["Employment_Status"] = bool(input("Employment_Status: "))
                info["Joining_Date"] = input("Joining_Date (YYYY-MM-DD): ")
                info["Gender"] = input("Gender (Male, Female, Others): ")
                # something wrong in next line
                query = "INSERT INTO Employee(Employee_ID, First_Name, Last_Name,Email,Supervisor_ID,Department_Name,Salary,DOB,Employment_Status,Joining_Date,Gender) VALUES('%d', '%s', '%s', '%s', '%d', '%s','%d','%s','%d', '%s', '%s')" % (
                    info["Employee_ID"], info["First_Name"], info["Last_Name"], info["Email"], info["Supervisor_ID"], info["Department_Name"], info["Salary"], info["DOB"], info["Employment_Status"], info["Joining_Date"], info["Gender"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Employee_ID to modify: "))
                query = "SELECT * FROM Employee where Employee_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Employee_ID: ")
                if info["ID"] != "":
                    row["Employee_ID"] = int(info["ID"])
                info["name"] = input("Name (First_Name Last_Name): ")
                if info["name"] != "":
                    row["First_Name"], row["Last_Name"] = info["name"].split(
                        ' ')
                info["Email"] = input("Email : ")
                if info["Email"] != "":
                    row["Email"] = info["Email"]
                info["Supervisor_ID"] = input("Supervisor_ID : ")
                if info["Supervisor_ID"] != "":
                    row["Supervisor_ID"] = int(info["Supervisor_ID"])
                info["Department_Name"] = input("Department_Name : ")
                if info["Department_Name"] != "":
                    row["Department_Name"] = info["Department_Name"]
                info["Salary"] = input("Salary : ")
                if info["Salary"] != "":
                    row["Salary"] = int(info["Salary"])
                info["DOB"] = input("DOB (YYYY-MM-DD): ")
                if info["DOB"] != "":
                    row["DOB"] = info["DOB"]
                info["Employment_Status"] = input("Employment_Status : ")
                if info["Employment_Status"] != "":
                    row["Employment_Status"] = bool(info["Employment_Status"])
                info["Joining_Date"] = input("Joining_Date : ")
                if info["Joining_Date"] != "":
                    row["Joining_Date"] = info["Joining_Date"]
                info["Gender"] = input("Gender (Male, Female, Others): ")
                if info["Gender"] != "":
                    row["Gender"] = info["Gender"]

                query = "UPDATE Employee SET Employee_ID='%d', First_Name='%s', Last_Name='%s',Email='%s',Supervisor_ID='%d',Department_Name='%s',Salary='%d',DOB='%s',Employment_Status='%d',Joining_Date='%s',Gender='%s' WHERE Employee_ID = '%d'" % (
                    row["Employee_ID"], row["First_Name"], row["Last_Name"], row["Email"], row["Supervisor_ID"], row["Department_Name"], row["Salary"], row["DOB"], row["Employment_Status"], row["Joining_Date"], row["Gender"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Employee_ID you want to delete: "))
                query = "DELETE FROM Employee WHERE Employee_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def employee_phonenumber(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Employee_Phone_Number;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Employee_ID"] = int(input("Employee_ID: "))
                # info["First_Name"], info["Last_Name"] = (input("Name (First_Name Last_Name): ")).split(' ')
                # info["DOB"] = input("DOB (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                info["Phone_Number"] = int(input("Phone_Number : "))
                query = "INSERT INTO Employee_Phone_Number(Employee_ID, Phone_Number) VALUES('%d', '%s')" % (
                    info["Employee_ID"], info["Phone_Number"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Employee_ID to modify: "))
                query = "SELECT * FROM Employee where Employee_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Employee_ID: ")
                if info["ID"] != "":
                    row["Employee_ID"] = int(info["ID"])
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                # 	row["First_Name"], row["Last_Name"] = info["name"].split(' ')
                # info["DOB"] = input("DOB (YYYY-MM-DD): ")
                # if info["DOB"] != "":
                # 	row["DOB"] = info["DOB"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                # 	row["Gender"] = info["Gender"]
                info["Phone_Number"] = input("Phone_Number : ")
                if info["Phone_Number"] != "":
                    row["Phone_Number"] = int(info["Phone_Number"])
                query = "UPDATE Employee_Phone_Number SET Employee_ID = '%d',  Phone_Number = '%d' WHERE Employee_ID = '%d'" % (
                    row["Employee_ID"], row["Phone_Number"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Employee_ID whose phone number you want to delete: "))
                query = "DELETE FROM Employee_Phone_Number WHERE Employee_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def employee_address(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Employee_Address;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Employee_ID"] = int(input("Employee_ID: "))
                info["Pin"] = int(input("Pin : "))
                info["State"] = input("State: ")
                info["Country"] = input("Country: ")
                info["Street_Name"] = input("Street_Name: ")
                query = "INSERT INTO Employee_Address(Employee_ID, Pin, State, Country, Street_Name) VALUES('%d', '%d', '%s', '%s', '%s')" % (
                    info["Employee_ID"], info["Pin"], info["State"], info["Country"], info["Street_Name"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Employee_ID to modify: "))
                pin = int(input("Enter Current Pin: "))
                state = input("Enter Current State: ")
                country = input("Enter Current Country: ")
                street = input("Enter Current Street Name: ")

                query = "SELECT * FROM Employee_Address where Employee_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    ID, pin, state, country, street)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Employee_ID"] = input("Employee_ID: ")
                if info["Employee_ID"] != "":
                    row["Employee_ID"] = int(info["Employee_ID"])
                info["Pin"] = input("Pin: ")
                if info["Pin"] != "":
                    row["Pin"] = int(info["Pin"])
                info["State"] = input("State: ")
                if info["State"] != "":
                    row["State"] = info["State"]
                info["Country"] = input("Country: ")
                if info["Country"] != "":
                    row["Country"] = (info["Country"])
                info["Street_Name"] = input("Street_Name: ")
                if info["Street_Name"] != "":
                    row["Street_Name"] = (info["Street_Name"])
                query = "UPDATE Employee_Address SET Employee_ID = '%d', Pin = '%d', State = '%s', Country = '%s', Street_Name = '%s' WHERE Employee_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    row["Employee_ID"], row["Pin"], row["State"], row["Country"], row["Street_Name"], ID, pin, state, country, street)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                # info = {}
                ID = int(
                    input("Enter the Employee_ID whose address you want to delete: "))
                pin = int(input("Enter  Pin: "))
                state = input("Enter  State: ")
                country = input("Enter Country: ")
                street = input("Enter Street Name: ")

                query = "DELETE FROM Employee_Address WHERE Employee_ID = '%d' AND Pin='%d' AND State = '%s' AND Country = '%s' AND Street_Name = '%s'" % (
                    ID, pin, state, country, street)
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def department(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Department;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Department_Name"] = input("Department_Name: ")
                info["Manager_ID"] = int(input("Manager_ID: "))
                info["Number_Of_Employee"] = int(input(
                    "Number_Of_Employee: "))
                # info["Email"] = input("Email: ")
                # info["First_Name"], info["Last_Name"] = (
                # input("Name (First_Name Last_Name): ")).split(' ')
                # info["Supervisor_ID"] = int(input("Supervisor_ID: "))
                # info["Salary"] = int(input("Salary: "))
                # info["Employment_Status"] = bool(input("Employment_Status: "))
                # info["Joining_Date"] = input("Joining_Date (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")

                query = "INSERT INTO Department(Department_Name,Manager_ID,Number_Of_Employee) VALUES('%s', '%d', '%d')" % (
                    info["Department_Name"], info["Manager_ID"],    info["Number_Of_Employee"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                Name = input("Enter Manager_ID to modify: ")
                query = "SELECT * FROM Department where Department_Name = '%s'" % (
                    Name)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["Name"] = input("Department_Name : ")
                if info["Name"] != "":
                    row["Department_Name"] = info["Name"]
                info["ID"] = input("Manager_ID: ")
                if info["ID"] != "":
                    row["Manager_ID"] = int(info["ID"])
                info["Number_Of_Employee"] = input(
                    "Number_Of_Employee: ")
                if info["Number_Of_Employee"] != "":
                    row["Number_Of_Employee"] = int(info["Number_Of_Employee"])
                # info["Email"] = input("Email : ")
                # if info["Email"] != "":
                #     row["Email"] = info["Email"]
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                #     row["First_Name"], row["Last_Name"] = info["name"].split(
                #         ' ')
                # info["Supervisor_ID"] = input("Supervisor_ID : ")
                # if info["Supervisor_ID"] != "":
                #     row["Supervisor_ID"] = int(info["Supervisor_ID"])
                # info["Salary"] = input("Salary : ")
                # if info["Salary"] != "":
                #     row["Salary"] = int(info["Salary"])
                # info["Employment_Status"] = input("Employment_Status : ")
                # if info["Employment_Status"] != "":
                #     row["Employment_Status"] = bool(info["Employment_Status"])
                # info["Joining_Date"] = input("Joining_Date : ")
                # if info["Joining_Date"] != "":
                #     row["Joining_Date"] = info["Joining_Date"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                #     row["Gender"] = info["Gender"]

                query = "UPDATE Department SET Department_Name='%s',Manager_ID='%d',Number_Of_Employee='%d' WHERE Department_Name = '%s'" % (
                    row["Department_Name"], row["Manager_ID"],  row["Number_Of_Employee"], Name)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            return 1
        else:
            print("Please choose the correct option")


def technician(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Technician;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Employee_ID"] = int(input("Employee_ID: "))
                info["Project_Name"] = input("Project_Name: ")
                # info["Number_Of_Employee"] = int(input(
                #     "Number_Of_Employee: "))
                # info["Email"] = input("Email: ")
                # info["First_Name"], info["Last_Name"] = (
                # input("Name (First_Name Last_Name): ")).split(' ')
                # info["Supervisor_ID"] = int(input("Supervisor_ID: "))
                # info["Salary"] = int(input("Salary: "))
                # info["Employment_Status"] = bool(input("Employment_Status: "))
                # info["Joining_Date"] = input("Joining_Date (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")

                query = "INSERT INTO Technician(Employee_ID,Project_Name) VALUES('%d', '%s')" % (
                    info["Employee_ID"], info["Project_Name"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Employee_ID to modify: "))
                query = "SELECT * FROM Technician where Employee_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Employee_ID: ")
                if info["ID"] != "":
                    row["Employee_ID"] = int(info["ID"])
                info["Project_Name"] = input("Project_Name : ")
                if info["Project_Name"] != "":
                    row["Project_Name"] = info["Project_Name"]
                # info["Number_Of_Employee"] = input(
                #     "Number_Of_Employee: ")
                # if info["Number_Of_Employee"] != "":
                #     row["Number_Of_Employee"] = int(info["Number_Of_Employee"])
                # info["Email"] = input("Email : ")
                # if info["Email"] != "":
                #     row["Email"] = info["Email"]
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                #     row["First_Name"], row["Last_Name"] = info["name"].split(
                #         ' ')
                # info["Supervisor_ID"] = input("Supervisor_ID : ")
                # if info["Supervisor_ID"] != "":
                #     row["Supervisor_ID"] = int(info["Supervisor_ID"])
                # info["Salary"] = input("Salary : ")
                # if info["Salary"] != "":
                #     row["Salary"] = int(info["Salary"])
                # info["Employment_Status"] = input("Employment_Status : ")
                # if info["Employment_Status"] != "":
                #     row["Employment_Status"] = bool(info["Employment_Status"])
                # info["Joining_Date"] = input("Joining_Date : ")
                # if info["Joining_Date"] != "":
                #     row["Joining_Date"] = info["Joining_Date"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                #     row["Gender"] = info["Gender"]

                query = "UPDATE Technician SET Employee_ID='%d',Project_Name='%s' WHERE Employee_ID = '%d'" % (
                    row["Employee_ID"], row["Project_Name"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Employee_ID you want to delete from Technician: "))
                query = "DELETE FROM Technician WHERE Employee_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def security(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Security;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Employee_ID"] = int(input("Employee_ID: "))
                info["Security_Company"] = input("Security_Company: ")
                info["Years_Of_Eperience"] = int(input(
                    "Years_Of_Eperience: "))
                # info["Email"] = input("Email: ")
                # info["First_Name"], info["Last_Name"] = (
                # input("Name (First_Name Last_Name): ")).split(' ')
                # info["Supervisor_ID"] = int(input("Supervisor_ID: "))
                # info["Salary"] = int(input("Salary: "))
                # info["Employment_Status"] = bool(input("Employment_Status: "))
                # info["Joining_Date"] = input("Joining_Date (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")

                query = "INSERT INTO Security(Employee_ID,Security_Company,Years_Of_Eperience) VALUES('%d', '%s', '%d')" % (
                    info["Employee_ID"],   info["Security_Company"], info["Years_Of_Eperience"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Employee_ID to modify: "))
                query = "SELECT * FROM Security where Employee_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Employee_ID: ")
                if info["ID"] != "":
                    row["Employee_ID"] = int(info["ID"])
                info["Security_Company"] = input("Security_Company : ")
                if info["Security_Company"] != "":
                    row["Security_Company"] = info["Security_Company"]
                info["Years_Of_Eperience"] = input(
                    "Years_Of_Eperience : ")
                if info["Years_Of_Eperience"] != "":
                    row["Years_Of_Eperience"] = int(info["Years_Of_Eperience"])
                # info["Email"] = input("Email : ")
                # if info["Email"] != "":
                #     row["Email"] = info["Email"]
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                #     row["First_Name"], row["Last_Name"] = info["name"].split(
                #         ' ')
                # info["Supervisor_ID"] = input("Supervisor_ID : ")
                # if info["Supervisor_ID"] != "":
                #     row["Supervisor_ID"] = int(info["Supervisor_ID"])
                # info["Salary"] = input("Salary : ")
                # if info["Salary"] != "":
                #     row["Salary"] = int(info["Salary"])
                # info["Employment_Status"] = input("Employment_Status : ")
                # if info["Employment_Status"] != "":
                #     row["Employment_Status"] = bool(info["Employment_Status"])
                # info["Joining_Date"] = input("Joining_Date : ")
                # if info["Joining_Date"] != "":
                #     row["Joining_Date"] = info["Joining_Date"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                #     row["Gender"] = info["Gender"]

                query = "UPDATE Security SET Employee_ID='%d',Security_Company='%s',Years_Of_Eperience='%d' WHERE Employee_ID = '%d'" % (
                    row["Employee_ID"], row["Security_Company"], row["Years_Of_Eperience"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Employee_ID you want to delete from security: "))
                query = "DELETE FROM Security WHERE Employee_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def final_price_calculator(cost, discount):
    final = 0
    try:
        final = (1 - (discount/100))*cost
    except Exception as er:
        print("Enter valid values > ")
        print(">>>>>>>>>>", er)
    return final


# def price_after_discount(con, cur):
#     while(True):
#         print("Do you want to:")
#         print("1. See all entries")
#         print("2. Add new entry")
#         print("3. Modify the entry")
#         print("4. Delete the entry")
#         print("5. Go back")
#         ch = int(input("Enter choice> "))
#         if ch == 1:
#             try:
#                 query = 'SELECT * FROM Price_After_Discount;'
#                 cur.execute(query)
#                 rows = cur.fetchall()
#                 for row in rows:
#                     print(row)
#                 print("")
#             except Exception as er:
#                 print("Failed to show entries")
#                 print(">>>>>>>>>", er)
#         elif ch == 2:
#             try:
#                 info = {}
#                 info["Price_Per_Item"] = int(input("Price_Per_Item: "))
#                 info["Discount"] = float(input("Discount: "))


#                 cur.execute(query)
#                 con.commit()
#                 print("Successfully Added\n")
#             except Exception as er:
#                 con.rollback()
#                 print("Failed to insert into database")
#                 print(">>>>>>>>>", er)
#         elif ch == 3:
#             try:
#                 info = {}
#                 Price, Discount = input(
#                     "Enter Price_Per_Item and Discount to modify: ").split(' ')
#                 # check above line print statement
#                 query = "SELECT * FROM Price_After_Discount where Price_Per_Item = '%d' AND Discount = '%f'" % (
#                     Price, Discount)
#                 # check above statement
#                 cur.execute(query)
#                 row = cur.fetchone()
#                 print("Enter the entries you want to modify otherwise press 'ENTER'")
#                 info["Price_Per_Item"] = input("Price_Per_Item: ")
#                 if info["Price_Per_Item"] != "":
#                     row["Price_Per_Item"] = int(info["Price_Per_Item"])
#                 info["Discount"] = int(input("Discount : "))
#                 if info["Discount"] != "":
#                     row["Discount"] = info["Discount"]
#                 info["Final_Price"] = final_price_calculator(row["Price_Per_Item"], row["Discount"])

#                 query = "UPDATE Price_After_Discount SET Price_Per_Item = '%d', Discount = '%f', Final_Price = '%d' WHERE Price_Per_Item = '%d' AND Discount = '%f'" % (
#                     row["Price_Per_Item"], row["Discount"], row["Final_Price"], Price, Discount)
#                 cur.execute(query)
#                 con.commit()
#                 print("Successfully Modified\n")
#             except Exception as er:
#                 con.rollback()
#                 print("Failed to modify in the database")
#                 print(">>>>>>>>>", er)
#         elif ch == 4:
#             try:
#                 info = {}
#                 # info["Price_Per_Item"],info["Discount"] = int(input("Enter the Price_Per_Item and Discount whose Price_After_Discount you want to delete: ").split(' '))
#                 Pric , Disc = input(
#                     "Enter the Price_Per_Item and Discount whose Price_After_Discount you want to delete: ").split(' ')
#                 info["Discount"] = int(Disc)
#                 info["Price_Per_Item"] = int(Pric)
#                 query = "DELETE FROM Price_After_Discount WHERE Price_Per_Item = '%d' AND Discount = '%f'" % (
#                     info["Price_Per_Item"], info["Discount"])
#                 cur.execute(query)
#                 con.commit()
#                 print("Successfully Deleted\n")
#             except Exception as er:
#                 con.rollback()
#                 print("Failed to delete in the database")
#                 print(">>>>>>>>>", er)
#         elif ch == 5:
#             return 1
#         else:
#             print("Please choose the correct option")


def product(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Product;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Product_ID"] = int(input("Product_ID: "))

                info["Product_Name"] = input("Product_Name: ")

                info["Discount"] = float(input(
                    "Discount: "))

                info["Current_Stock"] = int(input(
                    "Current_Stock: "))

                info["Supplier_ID"] = int(input("Supplier_ID: "))

                info["Price_Per_Item"] = int(input(
                    "Price_Per_Item: "))
                info["Final_Price"] = final_price_calculator(
                    info["Price_Per_Item"], info["Discount"])
                # info["Email"] = input("Email: ")
                # info["First_Name"], info["Last_Name"] = (
                # input("Name (First_Name Last_Name): ")).split(' ')
                # info["Supervisor_ID"] = int(input("Supervisor_ID: "))
                # info["Salary"] = int(input("Salary: "))
                # info["Employment_Status"] = bool(input("Employment_Status: "))
                # info["Joining_Date"] = input("Joining_Date (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")

                query = "INSERT INTO Price_After_Discount(Price_Per_Item, Discount, Final_Price) VALUES('%f', '%f', '%f')" % (
                    info["Price_Per_Item"], info["Discount"], info["Final_Price"])
                cur.execute(query)
                con.commit()
                query = "INSERT INTO Product(Product_ID,Product_Name,Discount,Current_Stock,Supplier_ID,Price_Per_Item) VALUES('%d', '%s', '%f', '%d', '%d', '%f')" % (
                    info["Product_ID"], info["Product_Name"], info["Discount"], info["Current_Stock"], info["Supplier_ID"], info["Price_Per_Item"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Product_ID to modify: "))
                query = "SELECT * FROM Product where Product_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                Price = float(row["Price_Per_Item"])
                Discount = float(row["Discount"])
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Product_ID: ")
                if info["ID"] != "":
                    row["Product_ID"] = int(info["ID"])
                info["Product_Name"] = input("Product_Name : ")
                if info["Product_Name"] != "":
                    row["Product_Name"] = info["Product_Name"]
                info["Current_Stock"] = input(
                    "Current_Stock: ")
                if info["Current_Stock"] != "":
                    row["Current_Stock"] = int(info["Current_Stock"])
                info["Supplier_ID"] = input("Supplier_ID: ")
                if info["Supplier_ID"] != "":
                    row["Supplier_ID"] = int(info["Supplier_ID"])

                info["Discount"] = input("Discount: ")
                if info["Discount"] != "":
                    row["Discount"] = float(info["Discount"])
                info["Price_Per_Item"] = input("Price_Per_Item: ")
                if info["Price_Per_Item"] != "":
                    row["Price_Per_Item"] = float(info["Price_Per_Item"])
                # q1 = "SELECT Price_Per_Item FROM Product where Product_ID = '%d'"
                # q2 = "SELECT Discount FROM Product where Product_ID = '%d'"
                query = "SELECT Price_After_Discount.Final_Price FROM Price_After_Discount, Product where Price_After_Discount.Price_Per_Item = Product.Price_Per_Item AND Price_After_Discount.Discount = Product.Discount AND Product.Product_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row1 = cur.fetchone()
                print(row1)
                row1["Final_Price"] = final_price_calculator(
                    row["Price_Per_Item"], row["Discount"])

                query = "UPDATE Price_After_Discount SET Price_Per_Item = '%f', Discount = '%f', Final_Price = '%f' WHERE Price_Per_Item = '%f' AND Discount = '%f'" % (
                    row["Price_Per_Item"], row["Discount"], row1["Final_Price"], Price, Discount)
                # query = "UPDATE Price_After_Discount SET Price_Per_Item = 100, Discount = 100, Final_Price = 0"
                cur.execute(query)
                con.commit()
                query = "UPDATE Product SET Product_ID='%d',Product_Name='%s',Current_Stock='%d',Supplier_ID='%d' WHERE Product_ID = '%d'" % (
                    row["Product_ID"], row["Product_Name"], row["Current_Stock"], row["Supplier_ID"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Product_ID you want to delete from Product: "))
                query = "DELETE FROM Product WHERE Product_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def supplier(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Supplier;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Supplier_ID"] = int(input("Supplier_ID: "))
                info["Email"] = input("Email: ")
                info["Company_Name"] = input("Company_Name: ")
                info["Contract_Date"] = (
                    input("Contract_Date: (YYYY-MM-DD): "))

                query = "INSERT INTO Supplier(Supplier_ID, Email, Company_Name, Contract_Date) VALUES('%d', '%s', '%s', '%s')" % (
                    info["Supplier_ID"], info["Email"], info["Company_Name"], info["Contract_Date"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Supplier_ID to modify: "))
                # check above line print statement
                query = "SELECT * FROM Supplier where Supplier_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Supplier_ID"] = input("Supplier_ID: ")
                if info["Supplier_ID"] != "":
                    row["Supplier_ID"] = int(info["Supplier_ID"])
                info["Email"] = (input("Email : "))
                if info["Email"] != "":
                    row["Email"] = info["Email"]
                info["Company_Name"] = (input("Company_Name : "))
                if info["Company_Name"] != "":
                    row["Company_Name"] = info["Company_Name"]
                info["Contract_Date"] = (input("Contract_Date : "))
                if info["Contract_Date"] != "":
                    row["Contract_Date"] = info["Contract_Date"]
                query = "UPDATE Supplier SET Supplier_ID = '%d', Email = '%s', Company_Name = '%s', Contract_Date = '%s' WHERE Supplier_ID = '%s'" % (
                    row["Supplier_ID"], row["Email"], row["Company_Name"], row["Contract_Date"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Supplier_ID you want to delete: "))
                query = "DELETE FROM Supplier WHERE Supplier_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def supplier_address(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Supplier_Address;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Supplier_ID"] = int(input("Supplier_ID: "))
                info["Address"] = input("Address: ")
                query = "INSERT INTO Supplier_Address(Supplier_ID, Address) VALUES('%d', '%s')" % (
                    info["Supplier_ID"], info["Address"])
                # check other address fucntion this line is wrong Supplier Supplier_Address
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Supplier_ID to modify: "))
                address=input("Enter Current Address: ")
                query = "SELECT * FROM Supplier_Address where Supplier_ID = '%d' AND Address ='%s' " % (
                    ID,address)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Supplier_ID"] = input("Supplier_ID: ")
                if info["Supplier_ID"] != "":
                    row["Supplier_ID"] = int(info["Supplier_ID"])
                info["Address"] = input("Address: ")
                if info["Address"] != "":
                    row["Address"] = (info["Address"])
                query = "UPDATE Supplier_Address SET Supplier_ID = '%d', Address = '%s' WHERE Supplier_ID = '%d' AND Address ='%s' " % (
                    row["Supplier_ID"], row["Address"], ID,address)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Supplier_ID whose address you want to delete: "))
                address=input("Enter  Address: ")
                
                query = "DELETE FROM Supplier_Address WHERE Supplier_ID = '%d' AND Address ='%s'" % (
                    info["ID"],address)
                # check other address fucntion this line is wrong ID Supplier_ID
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def supplier_phonenumber(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Supplier_Phone_Number;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Supplier_ID"] = int(input("Supplier_ID: "))
                # info["First_Name"], info["Last_Name"] = (input("Name (First_Name Last_Name): ")).split(' ')
                # info["DOB"] = input("DOB (YYYY-MM-DD): ")
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                info["Phone_Number"] = int(input("Phone_Number : "))
                query = "INSERT INTO Supplier_Phone_Number(Supplier_ID, Phone_Number) VALUES('%d', '%s')" % (
                    info["Supplier_ID"], info["Phone_Number"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Supplier_ID to modify: "))
                query = "SELECT * FROM Supplier where Supplier_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER' ")
                info["ID"] = input("Supplier_ID: ")
                if info["ID"] != "":
                    row["Supplier_ID"] = int(info["ID"])
                # info["name"] = input("Name (First_Name Last_Name): ")
                # if info["name"] != "":
                # 	row["First_Name"], row["Last_Name"] = info["name"].split(' ')
                # info["DOB"] = input("DOB (YYYY-MM-DD): ")
                # if info["DOB"] != "":
                # 	row["DOB"] = info["DOB"]
                # info["Gender"] = input("Gender (Male, Female, Others): ")
                # if info["Gender"] != "":
                # 	row["Gender"] = info["Gender"]
                info["Phone_Number"] = input("Phone_Number : ")
                if info["Phone_Number"] != "":
                    row["Phone_Number"] = int(info["Phone_Number"])
                query = "UPDATE Supplier_Phone_Number SET Supplier_ID = '%d',  Phone_Number = '%d' WHERE Supplier_ID = '%d'" % (
                    row["Supplier_ID"], row["Phone_Number"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Supplier_ID whose phone number you want to delete: "))
                query = "DELETE FROM Supplier_Phone_Number WHERE Supplier_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def order(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Orders;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["Order_ID"] = int(input("Order_ID: "))
                info["Product_ID"] = int(input("Product_ID: "))
                info["Order_Quantity"] = int(input("Order_Quantity: "))

                query = "INSERT INTO Orders(Customer_ID, Order_ID, Product_ID, Order_Quantity) VALUES('%d', '%d', '%d', '%d')" % (
                    info["Customer_ID"], info["Order_ID"], info["Product_ID"], info["Order_Quantity"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Order_ID to modify: "))
                # check above line print statement
                query = "SELECT * FROM Orders where Order_ID = '%d'" % (ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Customer_ID"] = input("Customer_ID: ")
                if info["Customer_ID"] != "":
                    row["Customer_ID"] = int(info["Customer_ID"])
                info["Order_ID"] = int(input("Order_ID : "))
                if info["Order_ID"] != "":
                    row["Order_ID"] = info["Order_ID"]
                info["Product_ID"] = int(input("Product_ID : "))
                if info["Product_ID"] != "":
                    row["Product_ID"] = info["Product_ID"]
                info["Order_Quantity"] = int(input("Order_Quantity : "))
                if info["Order_Quantity"] != "":
                    row["Order_Quantity"] = info["Order_Quantity"]
                query = "UPDATE Orders SET Customer_ID = '%d', Order_ID = '%d', Product_ID = '%d', Order_Quantity = '%d' WHERE Order_ID = '%d'" % (
                    row["Customer_ID"], row["Order_ID"], row["Product_ID"], row["Order_Quantity"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Order_ID whose Orders you want to delete: "))
                query = "DELETE FROM Orders WHERE Order_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def tracking_detail(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Tracking_Detail;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Order_ID"] = int(input("Order_ID: "))
                info["Agent_ID"] = int(input("Agent_ID: "))
                info["Shipped_From"] = input("Shipped_From: ")
                info["Shipped_To"] = input("Shipped_To: ")
                info["Estimated_Delivery"] = int(input("Estimated_Delivery: "))

                query = "INSERT INTO Tracking_Detail(Order_ID, Agent_ID, Shipped_From, Shipped_To, Estimated_Delivery) VALUES('%d', '%d', '%s', '%s', '%d')" % (
                    info["Order_ID"], info["Agent_ID"], info["Shipped_From"], info["Shipped_To"], info["Estimated_Delivery"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Order_ID to modify: "))
                # check above line print statement
                query = "SELECT * FROM Tracking_Detail where Order_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Order_ID"] = int(input("Order_ID : "))
                if info["Order_ID"] != "":
                    row["Order_ID"] = info["Order_ID"]
                info["Agent_ID"] = input("Agent_ID: ")
                if info["Agent_ID"] != "":
                    row["Agent_ID"] = int(info["Agent_ID"])
                info["Shipped_From"] = (input("Shipped_From : "))
                if info["Shipped_From"] != "":
                    row["Shipped_From"] = info["Shipped_From"]
                info["Shipped_To"] = (input("Shipped_To : "))
                if info["Shipped_To"] != "":
                    row["Shipped_To"] = info["Shipped_To"]
                info["Estimated_Delivery"] = input("Estimated_Delivery : ")
                if info["Estimated_Delivery"] != "":
                    row["Estimated_Delivery"] = int(info["Estimated_Delivery"])
                query = "UPDATE Tracking_Detail SET Order_ID = '%d', Agent_ID = '%d', Shipped_From = '%s', Shipped_To = '%s', Estimated_Delivery = '%d' WHERE Order_ID = '%d'" % (
                    row["Order_ID"], row["Agent_ID"], row["Shipped_From"], row["Shipped_To"], row["Estimated_Delivery"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Order_ID whose Tracking_Detail you want to delete: "))
                query = "DELETE FROM Tracking_Detail WHERE Order_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def delivery_agent(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Delivery_Agent;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Agent_ID"] = int(input("Agent_ID: "))
                info["Agent_Name"] = input("Agent_Name: ")
                query = "INSERT INTO Delivery_Agent(Agent_ID, Agent_Name) VALUES('%d', '%s')" % (
                    info["Agent_ID"], info["Agent_Name"])
                # check other Agent_Name fucntion this line is wrong Supplier Delivery_Agent
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Agent_ID to modify: "))
                query = "SELECT * FROM Delivery_Agent where Agent_ID = '%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Agent_ID"] = input("Agent_ID: ")
                if info["Agent_ID"] != "":
                    row["Agent_ID"] = int(info["Agent_ID"])
                info["Agent_Name"] = input("Agent_Name: ")
                if info["Agent_Name"] != "":
                    row["Agent_Name"] = (info["Agent_Name"])
                query = "UPDATE Delivery_Agent SET Agent_ID = '%d', Agent_Name = '%s' WHERE Agent_ID = '%d'" % (
                    row["Agent_ID"], row["Agent_Name"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Agent_ID whose Delivery_Agent you want to delete: "))
                query = "DELETE FROM Delivery_Agent WHERE Agent_ID = '%d'" % (
                    info["ID"])
                # check other Agent_Name fucntion this line is wrong ID Agent_ID
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def feedback(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Feedback;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Product_ID"] = int(input("Product_ID: "))
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["Comment"] = input("Comment: ")
                info["Rating"] = float(input("Rating: "))

                query = "INSERT INTO Feedback(Product_ID, Customer_ID, Comment, Rating) VALUES('%d', '%d', '%s', '%f')" % (
                    info["Product_ID"], info["Customer_ID"], info["Comment"], info["Rating"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Product_ID to modify: "))
                # check above line print statement
                query = "SELECT * FROM Feedback where Product_ID = '%d'" % (ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Product_ID"] = int(input("Product_ID : "))
                if info["Product_ID"] != "":
                    row["Product_ID"] = info["Product_ID"]
                info["Customer_ID"] = input("Customer_ID: ")
                if info["Customer_ID"] != "":
                    row["Customer_ID"] = int(info["Customer_ID"])
                info["Comment"] = (input("Comment : "))
                if info["Comment"] != "":
                    row["Comment"] = info["Comment"]
                info["Rating"] = input("Rating : ")
                if info["Rating"] != "":
                    row["Rating"] = float(info["Rating"])
                query = "UPDATE Feedback SET Product_ID = '%d', Customer_ID = '%d', Comment = '%s', Rating = '%f' WHERE Product_ID = '%d'" % (
                    row["Product_ID"], row["Customer_ID"], row["Comment"], row["Rating"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Product_ID whose Feedback you want to delete: "))
                query = "DELETE FROM Feedback WHERE Product_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")


def supply(con, cur):
    while(True):
        print("Do you want to:")
        print("1. See all entries")
        print("2. Add new entry")
        print("3. Modify the entry")
        print("4. Delete the entry")
        print("5. Go back")
        ch = int(input("Enter choice> "))
        if ch == 1:
            try:
                query = 'SELECT * FROM Supply;'
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print("")
            except Exception as er:
                print("Failed to show entries")
                print(">>>>>>>>>", er)
        elif ch == 2:
            try:
                info = {}
                info["Customer_ID"] = int(input("Customer_ID: "))
                info["Order_ID"] = int(input("Order_ID: "))
                info["Agent_ID"] = int(input("Agent_ID: "))
                info["Supplier_ID"] = int(input("Supplier_ID: "))

                query = "INSERT INTO Supply(Customer_ID, Order_ID, Agent_ID, Supplier_ID) VALUES('%d', '%d', '%d', '%d')" % (
                    info["Customer_ID"], info["Order_ID"], info["Agent_ID"], info["Supplier_ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Added\n")
            except Exception as er:
                con.rollback()
                print("Failed to insert into database")
                print(">>>>>>>>>", er)
        elif ch == 3:
            try:
                info = {}
                ID = int(input("Enter Customer_ID to modify: "))
                # check above line print statement
                query = "SELECT * FROM Supply where Customer_ID = '%d'" % (ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Enter the entries you want to modify otherwise press 'ENTER'")
                info["Customer_ID"] = input("Customer_ID: ")
                if info["Customer_ID"] != "":
                    row["Customer_ID"] = int(info["Customer_ID"])
                info["Order_ID"] = int(input("Order_ID : "))
                if info["Order_ID"] != "":
                    row["Order_ID"] = info["Order_ID"]
                info["Agent_ID"] = int(input("Agent_ID : "))
                if info["Agent_ID"] != "":
                    row["Agent_ID"] = info["Agent_ID"]
                info["Supplier_ID"] = int(input("Supplier_ID : "))
                if info["Supplier_ID"] != "":
                    row["Supplier_ID"] = info["Supplier_ID"]
                query = "UPDATE Supply SET Customer_ID = '%d', Order_ID = '%d', Agent_ID = '%d', Supplier_ID = '%d' WHERE Customer_ID = '%d'" % (
                    row["Customer_ID"], row["Order_ID"], row["Agent_ID"], row["Supplier_ID"], ID)
                cur.execute(query)
                con.commit()
                print("Successfully Modified\n")
            except Exception as er:
                con.rollback()
                print("Failed to modify in the database")
                print(">>>>>>>>>", er)
        elif ch == 4:
            try:
                info = {}
                info["ID"] = int(
                    input("Enter the Customer_ID whose Supply relation you want to delete: "))
                query = "DELETE FROM Supply WHERE Customer_ID = '%d'" % (
                    info["ID"])
                cur.execute(query)
                con.commit()
                print("Successfully Deleted\n")
            except Exception as er:
                con.rollback()
                print("Failed to delete in the database")
                print(">>>>>>>>>", er)
        elif ch == 5:
            return 1
        else:
            print("Please choose the correct option")
