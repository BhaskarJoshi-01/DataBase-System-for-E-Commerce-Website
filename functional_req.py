import pymysql
import datetime


def get_product_his(con, cur):
    print("Welcome to Purchase History Tracking Detail Section ")
    while(True):
        print("Enter 0 to Quit")
        ID = int(input("Enter Customer_ID > "))
        if ID != 0:
            try:
                query = "SELECT Product_ID, Order_Quantity FROM Orders where Customer_ID='%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchall()
                for rows in row:
                    print(rows)
                print("")
            except Exception as er:
                con.rollback()
                print("Failed to show data")
                print("Enter Valid Customer_ID")
                print(">>>>>>>>>>", er)
        else:
            return 1


def avg_rating(con, cur):
    print("Welcome to the average rating viewer")
    while(True):
        print("Enter 0 to Quit")
        ID = int(input("Enter Customer_ID > "))
        if ID != 0:
            try:
                query = "SELECT AVG(Rating) FROM Feedback where Customer_ID='%d'" % (
                    ID)
                cur.execute(query)
                row = cur.fetchone()
                print("Average rating given by this Customer is: ")
                print(row)
                print("")
            except Exception as er:
                con.rollback()
                print("Failed to show data")
                print("Enter Valid Customer_ID")
                print(">>>>>>>>>>", er)
        else:
            return 1


def product_search(con, cur):
    print("Welcome to the product search page")
    while(True):
        print("Enter 0 to Quit")
        Name = input("Enter Product Name for search > ")
        if Name != "0":
            try:
                query = "SELECT Product_Name FROM Product where Product_Name LIKE %s"
                word = "%"+Name+"%"
                cur.execute(query, word)
                rows = cur.fetchall()
                print("The products are: ")
                for row in rows:
                    print(row)
                    print("")
            except Exception as er:
                con.rollback()
                print("No such product found")
                print(">>>>>>>>>>", er)
        else:
            return 1


def final_bill(con, cur):
    print("Welcome to the order bill page")
    while(True):
        print("Enter 0 to Quit")
        ID = int(input("Enter Order_ID > "))
        if ID != 0:
            try:
                query = "SELECT Price_After_Discount.Final_Price*Orders.Order_Quantity as Order_Bill FROM Orders,Product,Price_After_Discount where Orders.Order_ID='%d' AND Orders.Product_ID = Product.Product_ID AND Product.Price_Per_Item = Price_After_Discount.Price_Per_Item AND Product.Discount = Price_After_Discount.Discount" % (
                    ID)
                cur.execute(query)
                row = cur.fetchall()
                print(row)
                print("")
            except Exception as er:
                con.rollback()
                print("Failed to retrieve data")
                print("Enter Valid Order_ID")
                print(">>>>>>>>>>", er)
        else:
            return 1
