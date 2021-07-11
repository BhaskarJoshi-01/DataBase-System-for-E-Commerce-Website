-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: TEST1
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Customer`
--


drop database if exists E_COMM;                      
create database E_COMM;                              
use E_COMM;                                           

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `Customer_ID` int unsigned NOT NULL,
  `First_Name` varchar(30) NOT NULL,
  `Last_Name` varchar(30) NOT NULL,
  `Email` varchar(300) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(10) NOT NULL,
  PRIMARY KEY (`Customer_ID`),
  CONSTRAINT `aCustomer_ID` CHECK ((length(cast(`Customer_ID` as char charset utf8mb4)) = 7)),
  CONSTRAINT `aEmail` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `aGender` CHECK (((`Gender` = _utf8mb4'Male') or (`Gender` = _utf8mb4'Female') or (`Gender` = _utf8mb4'Others'))),
  CONSTRAINT `aName` CHECK (((not((`First_Name` like _utf8mb4'%[^a-Z]%'))) and (not((`Last_Name` like _utf8mb4'%[^a-z]%')))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1234567,'Ayush','Roy','abc@gmail.com','2002-12-10','Male'),(1234589,'Riya','Roy','xyz@gmail.com','2003-11-10','Female');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Address`
--

DROP TABLE IF EXISTS `Customer_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Address` (
  `Customer_ID` int unsigned NOT NULL,
  `Pin` int unsigned NOT NULL,
  `State` varchar(30) NOT NULL,
  `Country` varchar(30) NOT NULL,
  `Street_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Pin`,`State`,`Country`,`Street_Name`),
  CONSTRAINT `Customer_Address_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aCountry` CHECK ((not((`Country` like _utf8mb4'%[^a-Z]%')))),
  CONSTRAINT `aPin` CHECK ((length(cast(`Pin` as char charset utf8mb4)) = 6)),
  CONSTRAINT `aState` CHECK ((not((`State` like _utf8mb4'%[^a-Z]%'))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Address`
--

LOCK TABLES `Customer_Address` WRITE;
/*!40000 ALTER TABLE `Customer_Address` DISABLE KEYS */;
INSERT INTO `Customer_Address` VALUES (1234567,123456,'Goa','India','B-1'),(1234589,223456,'Goa','India','A-2');
/*!40000 ALTER TABLE `Customer_Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Phone_Number`
--

DROP TABLE IF EXISTS `Customer_Phone_Number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Phone_Number` (
  `Customer_ID` int unsigned NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  PRIMARY KEY (`Phone_Number`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `Customer_Phone_Number_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aPhone_Number` CHECK (((length(`Phone_Number`) = 10) and (not((`Phone_Number` like _utf8mb4'%[^0-9]%')))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Phone_Number`
--

LOCK TABLES `Customer_Phone_Number` WRITE;
/*!40000 ALTER TABLE `Customer_Phone_Number` DISABLE KEYS */;
INSERT INTO `Customer_Phone_Number` VALUES (1234567,'9181716151'),(1234589,'7181716151');
/*!40000 ALTER TABLE `Customer_Phone_Number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Delivery_Agent`
--

DROP TABLE IF EXISTS `Delivery_Agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Delivery_Agent` (
  `Agent_ID` int unsigned NOT NULL,
  `Agent_Name` varchar(31) NOT NULL,
  PRIMARY KEY (`Agent_ID`),
  CONSTRAINT `aAgent_ID` CHECK ((length(cast(`Agent_ID` as char charset utf8mb4)) = 7)),
  CONSTRAINT `aAgent_Name` CHECK ((length(`Agent_Name`) < 31))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Delivery_Agent`
--

LOCK TABLES `Delivery_Agent` WRITE;
/*!40000 ALTER TABLE `Delivery_Agent` DISABLE KEYS */;
INSERT INTO `Delivery_Agent` VALUES (2222222,'Rahul'),(2223334,'Raman');
/*!40000 ALTER TABLE `Delivery_Agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `Department_Name` varchar(30) NOT NULL,
  `Manager_ID` int unsigned NOT NULL,
  `Number_Of_Employee` int unsigned NOT NULL,
  PRIMARY KEY (`Department_Name`),
  KEY `Manager_ID` (`Manager_ID`),
  CONSTRAINT `Department_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `Employee` (`Employee_ID`),
  CONSTRAINT `aDepartment_Name` CHECK ((not((`Department_Name` like _utf8mb4'%[^a-Z]%')))),
  CONSTRAINT `aNumber_Of_Employee` CHECK ((`Number_Of_Employee` < 1000000)),
  CONSTRAINT `bDepartment_Name` CHECK ((length(`Department_Name`) <= 100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES ('Security',1234589,4),('Technician',1234567,4);
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `Employee_ID` int unsigned NOT NULL,
  `First_Name` varchar(30) NOT NULL,
  `Last_Name` varchar(30) NOT NULL,
  `Email` varchar(300) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Supervisor_ID` int unsigned NOT NULL,
  `Department_Name` varchar(30) NOT NULL,
  `Salary` int unsigned NOT NULL,
  `Employment_Status` bool NOT NULL,
  `Joining_Date` date NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  KEY `Supervisor_ID` (`Supervisor_ID`),
  KEY `Department_Name` (`Department_Name`),
  CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`Supervisor_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Employee_ibfk_2` FOREIGN KEY (`Department_Name`) REFERENCES `Department` (`Department_Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aEEmail` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `aeGender` CHECK (((`Gender` = _utf8mb4'Male') or (`Gender` = _utf8mb4'Female') or (`Gender` = _utf8mb4'Others'))),
  CONSTRAINT `aEmployee_ID` CHECK ((length(cast(`Employee_ID` as char charset utf8mb4)) = 7)),
  CONSTRAINT `aEmployment_Status` CHECK (((`Employment_Status` = 0) or (`Employment_Status` = 1))),
  CONSTRAINT `aeName` CHECK (((not((`First_Name` like _utf8mb4'%[^a-Z]%'))) and (not((`Last_Name` like _utf8mb4'%[^a-z]%'))))),
  CONSTRAINT `aSalary` CHECK ((length(cast(`Salary` as char charset utf8mb4)) <= 7))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (1234567,'Aman','Roy','aman@gmail.com','2002-12-10','Male',1234567,'Technician',23000,1,'2019-12-23'),(1234589,'Riyaz','Roy','r@gmail.com','2002-01-02','Male',1234589,'Security',30000,1,'2018-12-23');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Address`
--

DROP TABLE IF EXISTS `Employee_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Address` (
  `Employee_ID` int unsigned NOT NULL,
  `Pin` int unsigned NOT NULL,
  `State` varchar(30) NOT NULL,
  `Country` varchar(30) NOT NULL,
  `Street_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Pin`,`State`,`Country`,`Street_Name`),
  CONSTRAINT `Employee_Address_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aECountry` CHECK ((not((`Country` like _utf8mb4'%[^a-Z]%')))),
  CONSTRAINT `aEPin` CHECK ((length(cast(`Pin` as char charset utf8mb4)) = 6)),
  CONSTRAINT `aEState` CHECK ((not((`State` like _utf8mb4'%[^a-Z]%'))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Address`
--

LOCK TABLES `Employee_Address` WRITE;
/*!40000 ALTER TABLE `Employee_Address` DISABLE KEYS */;
INSERT INTO `Employee_Address` VALUES (1234567,333456,'Goa','India','Z-1'),(1234589,443456,'Goa','India','A-7');
/*!40000 ALTER TABLE `Employee_Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Phone_Number`
--

DROP TABLE IF EXISTS `Employee_Phone_Number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Phone_Number` (
  `Employee_ID` int unsigned NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  PRIMARY KEY (`Phone_Number`),
  KEY `Employee_ID` (`Employee_ID`),
  CONSTRAINT `Employee_Phone_Number_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aEPhone_Number` CHECK (((length(`Phone_Number`) = 10) and (not((`Phone_Number` like _utf8mb4'%[^0-9]%')))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Phone_Number`
--

LOCK TABLES `Employee_Phone_Number` WRITE;
/*!40000 ALTER TABLE `Employee_Phone_Number` DISABLE KEYS */;
INSERT INTO `Employee_Phone_Number` VALUES (1234567,'9181799151'),(1234589,'7181777151');
/*!40000 ALTER TABLE `Employee_Phone_Number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Feedback`
--

DROP TABLE IF EXISTS `Feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Feedback` (
  `Product_ID` int unsigned NOT NULL,
  `Customer_ID` int unsigned NOT NULL,
  `Rating` float NOT NULL,
  `Comment` varchar(251) NOT NULL,
  PRIMARY KEY (`Product_ID`,`Customer_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `Feedback_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Feedback_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`Product_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aComment` CHECK ((length(`Comment`) < 251)),
  CONSTRAINT `aRating` CHECK (((`Rating` > 0) and (`Rating` <= 10)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feedback`
--

LOCK TABLES `Feedback` WRITE;
/*!40000 ALTER TABLE `Feedback` DISABLE KEYS */;
INSERT INTO `Feedback` VALUES (1111111,1234567,4.8,'Bakwass...'),(1111112,1234589,9.8,'Maja hi aa gya');
/*!40000 ALTER TABLE `Feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `Order_ID` int unsigned NOT NULL,
  `Customer_ID` int unsigned NOT NULL,
  `Product_ID` int unsigned NOT NULL,
  `Order_Quantity` int unsigned NOT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  -- KEY `Product_ID` (`Product_ID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`Product_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aOrder_ID` CHECK ((length(cast(`Order_ID` as char charset utf8mb4)) = 7)),
  CONSTRAINT `aOrder_Quantity` CHECK ((length(cast(`Order_Quantity` as char charset utf8mb4)) <= 4))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1212121,1234567,1111111,3),(1212122,1234589,1111112,4);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Price_After_Discount`
--

DROP TABLE IF EXISTS `Price_After_Discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Price_After_Discount` (
  `Price_Per_Item` float NOT NULL,
  `Discount` float NOT NULL,
  `Final_Price` float NOT NULL,
  PRIMARY KEY (`Price_Per_Item`,`Discount`),
  CONSTRAINT `aDiscount` CHECK (((`Discount` <= 100) and (`Discount` >= 0))),
  -- CONSTRAINT `aFinal_Price` CHECK ((`Final_Price` = ((1 - (`Discount` / 100)) * `Price_Per_Item`))),
  CONSTRAINT `aPrice_Per_Item` CHECK ((`Price_Per_Item` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Price_After_Discount`
--

LOCK TABLES `Price_After_Discount` WRITE;
/*!40000 ALTER TABLE `Price_After_Discount` DISABLE KEYS */;
INSERT INTO `Price_After_Discount` VALUES (199,0,199),(299,0,299),(399,0,399);
/*!40000 ALTER TABLE `Price_After_Discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `Product_ID` int unsigned NOT NULL,
  `Supplier_ID` int unsigned NOT NULL,
  `Product_Name` varchar(102) NOT NULL,
  `Price_Per_Item` float NOT NULL,
  `Discount` float NOT NULL,
  `Current_Stock` int unsigned NOT NULL,
  PRIMARY KEY (`Product_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  KEY `Price_Per_Item` (`Price_Per_Item`,`Discount`),
  CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Product_ibfk_2` FOREIGN KEY (`Price_Per_Item`, `Discount`) REFERENCES `Price_After_Discount` (`Price_Per_Item`, `Discount`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aProduct_ID` CHECK ((length(cast(`Product_ID` as char charset utf8mb4)) = 7)),
  CONSTRAINT `aProduct_Name` CHECK ((length(`Product_Name`) < 101))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (1111111,1111111,'Pizza',299,0,100),(1111112,1111111,'Burger',399,0,200),(1111113,1111112,'Puff',199,0,100);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Security`
--

DROP TABLE IF EXISTS `Security`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Security` (
  `Employee_ID` int unsigned NOT NULL,
  `Security_Company` varchar(102) NOT NULL,
  `Years_Of_Eperience` float NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  CONSTRAINT `Security_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aExperience` CHECK ((`Years_Of_Eperience` < 100)),
  CONSTRAINT `aSecurity_Company` CHECK ((length(`Security_Company`) < 101))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Security`
--

LOCK TABLES `Security` WRITE;
/*!40000 ALTER TABLE `Security` DISABLE KEYS */;
INSERT INTO `Security` VALUES (1234589,'Amazon',2);
/*!40000 ALTER TABLE `Security` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier`
--

DROP TABLE IF EXISTS `Supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier` (
  `Supplier_ID` int unsigned NOT NULL,
  `Contract_Date` date NOT NULL,
  `Company_Name` varchar(102) NOT NULL,
  `Email` varchar(300) NOT NULL,
  PRIMARY KEY (`Supplier_ID`),
  CONSTRAINT `aCompany_Name` CHECK ((length(`Company_Name`) < 101)),
  CONSTRAINT `aSEmail` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `aSupplier_ID` CHECK ((length(cast(`Supplier_ID` as char charset utf8mb4)) = 7))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier`
--

LOCK TABLES `Supplier` WRITE;
/*!40000 ALTER TABLE `Supplier` DISABLE KEYS */;
INSERT INTO `Supplier` VALUES (1111111,'2015-12-10','FoodPanda','food@gmail.com'),(1111112,'2016-12-10','Zomato','zomato@gmail.com');
/*!40000 ALTER TABLE `Supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier_Address`
--

DROP TABLE IF EXISTS `Supplier_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier_Address` (
  `Supplier_ID` int unsigned NOT NULL,
  `Address` varchar(101) NOT NULL,
  PRIMARY KEY (`Supplier_ID`,`Address`),
  CONSTRAINT `Supplier_Address_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aSAddress` CHECK ((not((`Address` like _utf8mb4'%[^,-a-Z]%'))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier_Address`
--

LOCK TABLES `Supplier_Address` WRITE;
/*!40000 ALTER TABLE `Supplier_Address` DISABLE KEYS */;
INSERT INTO `Supplier_Address` VALUES (1111111,'Goa,India'),(1111112,'Goa,India');
/*!40000 ALTER TABLE `Supplier_Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier_Phone_Number`
--

DROP TABLE IF EXISTS `Supplier_Phone_Number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier_Phone_Number` (
  `Supplier_ID` int unsigned NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  PRIMARY KEY (`Phone_Number`),
  KEY `Supplier_ID` (`Supplier_ID`),
  CONSTRAINT `Supplier_Phone_Number_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aSPhone_Number` CHECK (((length(`Phone_Number`) = 10) and (not((`Phone_Number` like _utf8mb4'%[^0-9]%')))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier_Phone_Number`
--

LOCK TABLES `Supplier_Phone_Number` WRITE;
/*!40000 ALTER TABLE `Supplier_Phone_Number` DISABLE KEYS */;
INSERT INTO `Supplier_Phone_Number` VALUES (1111111,'2319241822'),(1111112,'2319241834');
/*!40000 ALTER TABLE `Supplier_Phone_Number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supply`
--

DROP TABLE IF EXISTS `Supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supply` (
  `Customer_ID` int unsigned NOT NULL,
  `Agent_ID` int unsigned NOT NULL,
  `Order_ID` int unsigned NOT NULL,
  `Supplier_ID` int unsigned NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Agent_ID`,`Order_ID`,`Supplier_ID`),
  KEY `Agent_ID` (`Agent_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  KEY `Order_ID` (`Order_ID`),
  CONSTRAINT `Supply_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`Customer_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Supply_ibfk_2` FOREIGN KEY (`Agent_ID`) REFERENCES `Delivery_Agent` (`Agent_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Supply_ibfk_3` FOREIGN KEY (`Supplier_ID`) REFERENCES `Supplier` (`Supplier_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Supply_ibfk_4` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`Order_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supply`
--

LOCK TABLES `Supply` WRITE;
/*!40000 ALTER TABLE `Supply` DISABLE KEYS */;
INSERT INTO `Supply` VALUES (1234567,2222222,1212121,1111111),(1234589,2222222,1212122,1111111);
/*!40000 ALTER TABLE `Supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Technician`
--

DROP TABLE IF EXISTS `Technician`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Technician` (
  `Employee_ID` int unsigned NOT NULL,
  `Project_Name` varchar(102) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  CONSTRAINT `Technician_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aProject_Name` CHECK ((length(`Project_Name`) < 101))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Technician`
--

LOCK TABLES `Technician` WRITE;
/*!40000 ALTER TABLE `Technician` DISABLE KEYS */;
INSERT INTO `Technician` VALUES (1234567,'Netflix Project');
/*!40000 ALTER TABLE `Technician` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tracking_Detail`
--

DROP TABLE IF EXISTS `Tracking_Detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tracking_Detail` (
  `Order_ID` int unsigned NOT NULL,
  `Agent_ID` int unsigned NOT NULL,
  `Estimated_Delivery` int unsigned NOT NULL,
  `Shipped_From` varchar(101) NOT NULL,
  `Shipped_To` varchar(101) NOT NULL,
  PRIMARY KEY (`Order_ID`),
  -- KEY `Agent_ID` (`Agent_ID`),
  CONSTRAINT `Tracking_Detail_ibfk_1` FOREIGN KEY (`Agent_ID`) REFERENCES `Delivery_Agent` (`Agent_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Tracking_Detail_ibfk_2` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`Order_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aShipped_From` CHECK ((length(`Shipped_From`) < 101)),
  CONSTRAINT `aShipped_to` CHECK ((length(`Shipped_to`) < 101))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tracking_Detail`
--

LOCK TABLES `Tracking_Detail` WRITE;
/*!40000 ALTER TABLE `Tracking_Detail` DISABLE KEYS */;
INSERT INTO `Tracking_Detail` VALUES (1212121,2222222,5,'Mumbai','Goa'),(1212122,2222222,6,'Mumbai','Goa');
/*!40000 ALTER TABLE `Tracking_Detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-04 19:14:29
