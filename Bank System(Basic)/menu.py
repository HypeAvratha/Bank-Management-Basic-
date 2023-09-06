import datetime as dt
import random
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='123456789',database='Bank_Database')
cur = conn.cursor()
conn.autocommit = True
c = 'y'
while c == 'y':
     print("-"*30)
     print("\nWELCOME TO THE BANK")
     print()
     print("-"*30)
     print('\n1.CREATE BANK ACCOUNT')
     print('\n2.TRANSACTION')
     print('\n3.CUSTOMER DETAILS')
     print('\n4.TRANSACTION DETAILS')
     print('\n5.DELETE ACCOUNT')
     print('\n6.QUIT')
     print()
     print("-"*30)
     n=int(input('\nEnter your CHOICE='))
     print()
     print("-"*30)
     c=input("\nDo you want to continue(y/n): ")
     if n == 1:
          print("-"*30)
          acc_no=random.randint(1,1000)*27937
          print(f"Your account number is {acc_no} (Remember it very carefully!!)")
          acc_name=input('\nEnter your ACCOUNT NAME=')
          ph_no=int(input('\nEnter your PHONE NUMBER='))
          add=(input('\nEnter your place='))
          cr_amt=int(input('\nEnter your credit amount='))
          V_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
          cur.execute(V_SQLInsert)
          print('\nAccount Created Succesfully!!!!!')
          print()
          print("-"*30)
          conn.commit()
          c=input("\nDo you want to continue(y/n): ")
    
     if n == 2:
          print("-"*20)
          acct_no=int(input('\nEnter Your Account Number='))
          cur.execute('select * from customer_details where acct_no='+str (acct_no) )
          data=cur.fetchall()
          count=cur.rowcount
          conn.commit()
          if count == 0:
               print('\nAccount Number Invalid Sorry Try Again Later')
               print()
               print("-"*30)
               c=input("\nDo you want to continue(y/n): ")
          else:
               print("-"*30)
               print('\n1.WITHDRAW AMOUNT')
               print('\n2.ADD AMOUNT')
               print()
               print("-"*30)
               print()
               print("-"*30)
               x=int(input('\nEnter your CHOICE='))
               print()
               print("-"*30)
               print()
               if x == 1:
                    print("-"*30)
                    amt=int(input('\nEnter withdrawl amount='))
                    cr_amt=0
                    cur.execute('update customer_details set cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                    V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                    cur.execute(  V_SQLInsert)
                    conn.commit()
                    print('\nAccount Updated Succesfully!!!!!')
                    print()
                    print("-"*30)
                    c=input("\nDo you want to continue(y/n): ")

               if x== 2:
                    print("-"*30)
                    amt=int(input('\nEnter amount to be added='))
                    cr_amt=0
                    cur.execute('update customer_details set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                    V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                    cur.execute(  V_SQLInsert)
                    conn.commit()
                    print('\nAccount Updated Succesfully!!!!!')
                    print()
                    print("-"*30)
                    c=input("\nDo you want to continue(y/n): ")

     if n == 3:
          print("-"*30)
          acct_no=int(input('\nEnter your account number='))
          cur.execute('select * from customer_details where acct_no='+str(acct_no) )
          if cur.fetchone() is  None:
               print('\nInvalid Account number')
               print()
               print("-"*30)
          else:
               cur.execute('select * from customer_details where acct_no='+str(acct_no) )
               data=cur.fetchall()
               for row in data:
                    print('\nACCOUNT NO=',acct_no)
                    print('\nACCOUNT NAME=',row[1])
                    print('\nPHONE NUMBER=',row[2])
                    print('\nADDRESS=',row[3])
                    print('\nDEPOSIT=',row[4])
                    print()
                    print("-"*30)
                    c=input("\nDo you want to continue(y/n): ")

     if n == 4:
          print("-"*30)
          acct_no=int(input('\nEnter your account number='))
          cur.execute('select * from customer_details where acct_no='+str(acct_no) )
          if cur.fetchone() is  None:
               print('\nInvalid Account number')
               print()
               print("-"*30)
               c=input("\nDo you want to continue(y/n): ")               
          else:
               cur.execute('select * from transactions where acct_no='+str(acct_no) )
               data=cur.fetchall()
               for row in data:
                    print('\nACCOUNT NO=',acct_no)
                    print('\nDATE=',row[1])
                    print('\nWITHDRAWAL AMOUNT=',row[2])
                    print('\nAMOUNT ADDED=',row[3])
                    print()
                    print("-"*30)
                    c=input("\nDo you want to continue(y/n): ")
                               
     if n == 5:
          print("-"*30)
          print('\nDELETE YOUR ACCOUNT')
          acct_no=int(input('\nEnter your account number='))
          cur.execute('delete from customer_details where acct_no='+str(acct_no) )
          print('\nACCOUNT DELETED SUCCESFULLY')
          print()
          print("-"*30)
          c=input("\nDo you want to continue(y/n): ")

     if n == 6:
          print("-"*30)
          print('\nDO YO WANT TO EXIT(y/n)')
          c=input ('\nEnter your choice= ')
          print()
          print("-"*30)
          print('\nTHANK YOU PLEASE VISIT AGAIN')
          print()
          print("-"*30)
          quit()