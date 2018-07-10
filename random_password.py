import random
import string
import database
from database import *
#functional Global Varibles
default_password = 'admin'
count =0
def pword_gen():
    length = int(input("Enter How may numners pasword you want\n"))
    special = int(input("Enter How may specil chaarcters you want\n"))
    numbers = int(input("Enter How may numbers  you want\n"))
    capital = int(input("Enter How may capital letters you want\n"))
    small   = int(input("Enter How may small letters you want\n"))
    #counting the length of password and total numer of password length
    total = special + numbers + capital + small
    gen_password =""
    if(length == total):
        spec = string.punctuation
        for num in  range(0,numbers):
           res1 = random.randint(0,9)
           gen_password += str(res1)
        for cap in range(0,capital):
           res2 = chr(random.randint(65,65+25))
           gen_password += str(res2)
        for sm in range(0,small):
           res3 = chr(random.randint(65, 65 + 25)).lower()
           gen_password += res3
        for sp in range(0,special):
            res4 = random.choice(spec)
            gen_password += res4
        #print("Genarated Password:",gen_password,"\n\n")
        new_password=''.join(random.sample(gen_password, len(gen_password)))
        #print(new_password)
        print("Your password genarated sucessfully.....")
        choice = input("Do you want Save your password into database Then Press Y/N\n")
        if (choice.upper() == "Y"):
            purpose = input(" Genated Password Which purpuse your Saving\n")
            print(cur.execute("INSERT INTO password VALUES (?,?)", (new_password,purpose)))
            conn.commit()
            conn.close()
            print(purpose,"Password Is Saved Succesfully In Database...\n")
        else:
            print("Your Password Is Not Saved ............Thank You.....For Visiting....\n")
    else:
        print("Your Entered digits Not Equal to Given password length......")
def ret_password():
    while True:
     print("Hey..!! Are You Rertive Your Password")
     ret = input("Plz Enter Your default Admin Password\n")
     if default_password == ret:
             cur.execute("SELECT * FROM password")
             rows = cur.fetchall()
             print("PassWord", "\t", "Purpose")
             print("--------------------------------------")
             for line in rows:
                 print(str(line[0]), "\t", str(line[1]))
     else:
        global count
        if  count <= 2:
            count=count+1
            ret_password()
        else:
            print("Your Maximum Attemtms Failed Plz Try Ofter Sometime.......")
            break
     break

#-------------Main Method-----------------------

print("\n---------- Welcome To Password-Genarator ------------\n")
print("Select your Choices:")
print("------------------------------------------")
print("1)Password Genarator")
print("2)Password Retrive\n")
choice = int(input("Ente Your Choice Number:\n"))
if (choice == 1):
    pword_gen()
elif(choice == 2):
    ret_password()
else:
    print("Select Your Choice 1 or 2")
