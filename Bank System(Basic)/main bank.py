import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='123456789',database='Bank_Database')
cur = conn.cursor()
query=("SELECT username FROM user_table")
cur.execute(query)
rows=cur.fetchall()

def begin():
     global n
     print('=========================WELCOME TO BANK============================================================')
     import datetime as dt
     print(dt.datetime.now())
     print("-"*30)
     print('\n1.REGISTER')
     print('\n2.LOGIN')
     print("\n3.EXIT")
     print()
     print("-"*30)
     n=(input('\n>>Enter your choice='))

def sqlinsert():
     V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print('\nUSER created succesfully')
     import menu

def sqlselect():
     V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print('\n>>Invalid username or password')
          begin()
     else:
          print()
          print(">>Login Successful")
          import menu

n=''

while n!=8:
     begin()
     if n== '1':
          name=input('\n>>Enter a Username=')
          passwd=int(input('\n>>Enter a 4 DIGIT Password='))
          insert=("INSERT INTO customer_details (name) values("")")
          print()
          sqlinsert()
          
     if  n=='2':
          name=input('\n>>Enter your Username=')
          passwd=int(input('\nEnter your 4 DIGIT Password='))
          sqlselect()
     
     if n=='3':
          print("Thank You for Banking with us!!")
          quit()

     else:
          print("Choose from the above only")
          n=input("Press Enter")