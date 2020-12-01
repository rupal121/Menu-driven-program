import os
def rm_docker_management(ip_address):
    while (1) :
        print("*******************************************Docker Management*********************************** ")
        print("""

                    \t 1 To download Docker 
                    \t 2 To Start Services Of Docker
                    \t 3 To Check Status Of Docker
                    \t 4 To check Docker Images In your System
                    \t 5 To remove a Docker Container 
                    \t 6 To remove All Running Docker Container 
                    \t 7 To Stop Services Of Docker
                    \t 8 Launch  Docker Container
                    \t 9 To return to main menu

        """)
        print("***********************************************************************************************")
        ch1_docker=int(input("Please select any option from the above options :"))
        if ch1_docker==1:
            docker_cmd_download = os.system("ssh {} rpm -q docker-ce".format(ip_address))
            if docker_cmd_download != 0 :

                docker_repo = os.system("ssh {} dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo".format(ip_address))
                if docker_repo != 0 :
                    print("Please Check Your Internet Connection And Try Again")
                else :
                    print("please wait till docker-repo creates in your system !! ")
                    install_docker = os.system("ssh {} dnf install docker-ce --nobest -y".format(ip_address))
                    if install_docker != 0 :
                        print("Some Problem Occur Please Try Agian")
                    else :
                        os.system("ssh {} firewall-cmd  --permanent --zone=public --add-masquerade".format(ip_address))
                        os.system("ssh {} firewall-cmd --reload".format(ip_address))
                        print("Docker is successfully Installed in your system")
        elif ch1_docker==2:
            os.system("ssh {} systemctl start docker".format(ip_address))
        elif ch1_docker==3:
            os.system("ssh {} systemctl status docker".format(ip_address))
        elif ch1_docker==4:
            os.system("ssh {} docker images".format(ip_address))
        elif ch1_docker==5:
            docker_name = input("Enter the container name or ID that you want to remove ")
            os.system("ssh {} docker rm -f {}".format(ip_address,docker_name))
        elif ch1_docker==6:
           os.system("ssh {} docker rm -f $(docker ps -aq)".format(ip_address))
        elif ch1_docker==7:
            os.system("ssh {} systemctl stop docker".format(ip_address))
        elif ch1_docker==8:
            docker_name = input("Enter name you want to give :- ")
            image_name = input("Enter image name :- ")
            tag = input("Enter Image tag :- ")
            os.system("ssh {} docker run -dit --name {} {}:{}".format(ip_address,docker_name,image_name,tag))
        elif ch1_docker==9:
            break
        else :
            print("please enter correct option")
def rm_networking(ip_address):
    while(1):
        print("""
                            \tpress a:to stop firewall
                            \tpress b:to start firewall
                            \tpress c:to install httpd
                            \tpress d:to configure web server
                            \tpress e:to see your page
                            \tpress f:to stop services of webserver
                            \tpress g:to check ip address
                            \tpress h:to go to main menu 
                  """)
        op=input("Please enter your choices:")
        if op=='a':
            os.system("ssh {} systemctl stop firewalld".format(ip_address))
        elif op=='b':
            os.system("ssh {} systemctl start firewalld".format(ip_address))
        elif op=='c':
            os.system("ssh {} yum install httpd".format(ip_address))
        elif op=='d':
            os.system("ssh {} systemctl start httpd".format(ip_address))
            os.system("ssh {} cd /var/www/html/".format(ip_address))
            os.system("ssh {} vi index.html".format(ip_address))
        elif op=='e':
            os.system("ssh {} firefox index.html".format(ip_address))
        elif op=='f':
            os.system("ssh {} systemctl status httpd".format(ip_address)) 
        elif op=='g':
            os.system("ssh {} ifconfig enp0s3".format(ip_address))     
        elif op=='h':
            break
        else :
            os.system("Enter correct option")
def rm_package_management(ip_address):
    while(1):
        print("*******************************************Package Management*********************************** ")
        print("""

                    \t 1 To check package install or not
                    \t 2 To install package
                    \t 3 To remove package
                    \t 4 To return to main menu

        """)
        print("***********************************************************************************************")
        ch1_pkg=int(input("please select any option from above options :"))
        if ch1_pkg==1:
            package = input("Enter Package Name Which you Want To Check : ")
            os.system("ssh {} rpm -q {}".format(ip_address,package))
        elif ch1_pkg ==2 :
            pack1=input("Enter Package Name Which you  Want To install : ")
            check_pack = os.system("ssh {} rpm -q {}".format(ip_address,pack1))
            if check_pack != 0 :
                print(" The package {} is not installed in your system  ".format(check_pack))
                print("wait it is downlaoding")
                os.system("ssh {} dnf install {} -y".format(ip_address,check_pack))
            else : 
                print("{} already in our system".format(check_pack))
        elif ch1_pkg ==3:
            pack2=input("Enter Package Name Which you  Want To remove : ")
            check_pack1 = os.system("ssh {} rpm -q {}".format(ip_address,pack2))
            if check_pack1 != 0 :
                print(" The package {} not installed in your system  ".format(check_pack1))
                print("wait till it is remove")
                os.system("ssh {} dnf remove {} -y".format(ip_address,check_pack1))
            else:
                print("you do not have {} in your system".format(check_pack1))

        elif ch1_pkg==4:
            break
        else :
            os.system("Enter correct option")    
def rm_basic_operation(ip_address):
    while True:
        input("Enter To Continue...")
        os.system("clear")
        print("""
        \n
        Press 1: Today's Date
        Press 2: Month Calender
        Press 3: Configure Appache Web Server
        Press 4: Create User
        Press 5: Delete Created User
        Press 6: IP
        Press 7: Exit to main menu
        """)
        
        ch = input("Enter your choice :- ")
        print(ch)
    

        
        
        if int(ch)==1:
                    os.system("ssh {} date". format(ip_address))
        elif int(ch)==2:
                    os.system("ssh {} cal". format(ip_address))

        elif int(ch)==3:
                    os.system("ssh {} yum install httpd". format(ip_address))
        elif int(ch)==4:
                    print("Enter user name which you want to create:")
                    createUser =input()
                    os.system("ssh {} useradd {}" . format(ip_address,createUser))
                    print("{} User is created successffuly".format(createUser))
        elif int(ch)==5:
                    print("Enter user name which you want to delete")
                    delete_user = input()
                    os.system("ssh {} userdel {}" . format(ip_address,delete_user))
                    print("{} User deleted successfully".format(delete_user))
        elif int(ch)==6:
                    os.system("ssh {} ifconfig". format(ip_address))
        elif int(ch)==7:
                    break

    else:
        print("Invalid menu Option, Try Again ")
        input("Enter To continue.. ")
def rm_aws_management(ip_address):
    while(1):
        print("   ------- Welcome to AWS services -------  ")
        print("""/n

        	\t Press 1: To configure aws services
        	\t Press 2: To Create a key-pair
       	    \t Press 3: To create security-group
        	\t Press 4: To launch an instance
        	\t Press 5: To create a volume
        	\t Press 6: To exit this menu
        """)
        ch=input(" Enter your choice:  ")
        if int(ch)==1:
            os.system("ssh {} aws configure ".format(ip_address))
        elif int(ch)==2:
            key_name=input(" Enter the key name:   ")
            os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(ip_address,key_name))
        elif int(ch)==3:
            sg_name=input(" Enter the name for security group :  ")
            sg_desc=input(" Enter the description for security group:  ")
            os.system("ssh {} aws ec2 create-security-group --group-name {} --description {}".format(ip_address,sg_name,sg_desc))
        elif int(ch)== 4:
            key_name=input(" Enter the key name:   ")
            sg_name=input(" Enter the ID for security group :  ")
            subnet_id=(" Enter the subnet id: ")
            os.system("ssh {} aws ec2 run-instances  --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --key-name {} --security-group-ids {} --subnet-id {}".format(ip_address,key_name,sg_name,subnet_id))
        elif int(ch)==5:
            aws_vol=int(input("Enter Storage size(GB):Ex : 1"))
            os.system("ssh {} aws ec2 create-volume --availability-zone ap-south-1a --size {}".format(ip_address,aws_vol))
        elif int(ch)==6:
            break
        else:
            print("invalid choice")       

