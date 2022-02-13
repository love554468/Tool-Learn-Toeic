def my_add_fn():
   print ("SUM:%s"%sum(map(int,input("Enter 2 numbers seperated by a space").split())))

def my_quit_fn():
   raise SystemExit

def invalid():
   print ("INVALID CHOICE!")

menu = {"1":("Sum",my_add_fn),
        "2":("Quit",my_quit_fn)
       }
for key in sorted(menu.keys()):
     print( key+":" + menu[key][0])

ans = input("Make A Choice")
menu.get(ans,[None,invalid])[1]()

# ans=True
# while ans:
#     print ("""
#     1.Add a Student
#     2.Delete a Student
#     3.Look Up Student Record
#     4.Exit/Quit
#     """)
#     ans= input("What would you like to do? ") 
#     if ans=="1": 
#       print("\n Student Added") 
#     elif ans=="2":
#       print("\n Student Deleted") 
#     elif ans=="3":
#       print("\n Student Record Found") 
#     elif ans=="4":
#       print("\n Goodbye") 
#     elif ans !="":
#       print("\n Not Valid Choice Try again") 