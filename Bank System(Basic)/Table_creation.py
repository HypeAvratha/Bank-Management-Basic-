#To create respective tables run this program.
#A database named Bank_Database is need to be created before-hand.
#To create a database run CREATE DATABASE Bank_Database

#To create the customer_details table :
import  mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='123456789')
crea = con.cursor()
crea.execute("Create database if not exists Bank_Database")
conn=sql.connect(host='localhost',user='root',password='123456789',database='Bank_Database')
cur=conn.cursor()
cur.execute('create table customer_details(acct_no int primary key,acct_holder varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')
      
#To create transaction_table :
cur.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')

#To create user_table :
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')