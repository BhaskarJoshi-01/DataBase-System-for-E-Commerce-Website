These are the instructions for running the e-commerce database . This is the final assignment of Data And Application (Phase 4) 
done by the team "Int Elligence" . The contributing members are ```Utkarsh Upadhyay (2019101010)``` , ```Bhaskar Joshi(2019111002)``` and ```Ayush Sharma(2019101004)```.

*INSTRUCTIONS*

### MySQL

To install MySQL server on Ubuntu, run the following commands

```
sudo apt-get update
sudo apt-get install mysql-server
```

When installing the MySQL server for the first time, it will prompt for a root password that you can later login with. 

The start command is
```
mysql -u <user_name> -p <password>
```

If for some reason, you aren't asked for the password during installation, try prepending the start command with sudo and provide your root password. You can now set a root password or create a new user. 


To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```


It is also possible to grant a new user access to only one database or some tables of a database. If your application involves different user types with different access clearences, you may use this feature.

```
source e_comm_db.sql;
```

### PyMySQL

PyMySQL is an interface for connection to the MySQL server from Python.

To install PyMySQL, you can use one of the two routes  
**Pip**
```
pip install PyMySQL
```
**Conda**
```
conda install -c anaconda pymysql
```

### Generating Database
<!-- ```sh
    # $ mysql -u username -p password 
```
```sh    
    # $ mysql> CREATE DATABASE E_COMM;
``` -->
<!-- Now exit from mysql environment (by using quit command) and then -->

Run the following command to import the database.
```sh
    $ mysql -u username -p  < e_comm_db.sql
```
Now you need to enter your password

### To Run
To run this database , you will need to login with a username and password (your MYSQL username and password) which has access to the COMPANY database.

```sh
    $ python3 e_com.py
```

This will prompt for you to enter your username and password.

### UI Interface
Now you will see the following CLI :

```
1. Customer 
2. Customer Address
3. Customer Phone Number
4. Employee 
5. Employee Address
6. Employe Phone Number
7. Department
8. Technician
9. Security 
10. Product
11. Supplier
12. Supplier Address
13. Supplier Phone Number
14. Order
15. Tracking Detail
16. Delivery Agent
17. Feedback
18. Supply
19. Print Final bill
20. Product Name search
21. History
22. Avg rating
23. Logout
Enter Choice > 

```

### Note
Only those entries are considered valid which satisfy all the given constraints.
If database named E_COMM already exists then drop the database using command 
```sh
    $ mysql> DROP DATABASE E_COMM ;
```
Here we have assumed that all users act as admin (i.e, have all the permissions).
