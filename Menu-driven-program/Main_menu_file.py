import os
from Team_details import *
from Main_menu_options import *
from local_function_file import *
from remote_functions_file import *

team_details()
a=1
while(a==1):
    print("\t\t\tHello and Welcome to the Menu ")
    choice=input("Enter where you want to perform the opertaions(local/remote):")
    if ("local" in choice.lower()):
        b=1
        while(b==1):
            main_menu_options()
            ch1=int(input("Enter any number from above options"))
            if ch1 == 1:
                basic_operation()
            elif ch1==2:
                package_management()
            elif ch1==3:
                docker_management()
            elif ch1==4:
                networking()
            elif ch1==5:
                aws_management()
            else :
              b=int(input("""You entered wrong number 
                             \t\t\tpress 1 if you want to continue else press 0""")) 
              if(b==0):
                  break              
    elif("remote" in choice.lower()):
        ip_address=input("Enter remote IP address")
        key_generated=input("Have you generated ssh-keygen(yes/no)")
        if("yes" in key_generated.lower()):
            os.system("ssh-copy-id root@{}".format(ip_address))
        elif ("no" in key_generated):
             os.system("ssh-keygen")
             os.system("ssh-copy-id root@{}".format(ip_address))
             print("ssh file generated")
             ab=input("press Enter to continue")
        else :
            print("Choose proper option")
        c=1
        while(c==1):
            main_menu_options()
            ch1=int(input("Enter any number from above options"))
            if ch1 == 1:
               rm_basic_operation(ip_address)
            elif ch1==2:
               rm_package_management(ip_address)
            elif ch1==3:
               rm_docker_management(ip_address)
            elif ch1==4:
               rm_networking(ip_address)
            elif ch1==5:
               rm_aws_management(ip_address)
            else :
              b=int(input("""You entered wrong number 
                             \t\t\tpress 1 if you want to continue else press 0""")) 
              if(b==0):
                  break                 
    else:
        print("please enter correct option")   
    a=int(input("press 1 if you want to continue else press 0"))

    



