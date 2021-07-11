import subprocess as sp
import pymysql
import pymysql.cursors
from functions import *
from functional_req import *


def funct():
    print("Atleast something is working")


def dispatch(ch,con,cur):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        customer(con,cur)
    elif(ch == 2):
        customer_address(con,cur)
    elif(ch == 3):
        customer_phonenumber(con,cur)
    elif(ch == 4):
        employee(con, cur)
    elif(ch == 5):
        employee_address(con,cur)
    elif(ch == 6):
        employee_phonenumber(con,cur)
    elif(ch == 7):
        department(con,cur)
    elif(ch == 8):
        technician(con,cur)
    elif(ch == 9):
        security(con,cur)
    elif(ch == 10):
        product(con,cur)
    elif(ch == 11):
        supplier(con,cur)
    elif(ch == 12):
        supplier_address(con,cur)
    elif(ch == 13):
        supplier_phonenumber(con,cur)
    elif(ch == 14):
        order(con,cur)
    elif(ch == 15):
        tracking_detail(con,cur)
    elif(ch == 16):
        delivery_agent(con,cur)
    elif(ch == 17):
        feedback(con,cur)
    elif(ch == 18):
        supply(con,cur)
    elif(ch == 19):
        final_bill(con,cur)
    elif(ch==20):
        product_search(con,cur)
    elif(ch==21):
        get_product_his(con,cur)
    elif(ch==22):
        avg_rating(con,cur)
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='E_COMM',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Customer ")
                print("2. Customer Address")
                print("3. Customer Phone Number")
                print("4. Employee ")
                print("5. Employee Address")
                print("6. Employe Phone Number")
                print("7. Department")
                print("8. Technician")
                print("9. Security ")
                print("10. Product")
                print("11. Supplier")
                print("12. Supplier Address")
                print("13. Supplier Phone Number")
                print("14. Order")
                print("15. Tracking Detail")
                print("16. Delivery Agent")
                print("17. Feedback")
                print("18. Supply")
                # functional requirements
                print("19. Print Final bill")
                print("20. Product Name search")
                print("21. History")
                print("22. Avg rating")
                print("23. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 23:
                    break
                else:
                    dispatch(ch,con,cur)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")