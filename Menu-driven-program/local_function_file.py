import os
def docker_management():
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
        ch1_docker=int(input("please select any option number from the above options :"))
        if ch1_docker==1:
            docker_cmd_download = os.system("rpm -q docker-ce")
            if docker_cmd_download != 0 :

                docker_repo = os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                if docker_repo != 0 :
                    print("Please Check Your Internet Connection And Try Again")
                else :
                    print("please wait till docker-repo creates in your system !! ")
                    install_docker = os.system("dnf install docker-ce --nobest -y")
                    if install_docker != 0 :
                        print("Some Problem Occur Please Try Agian")
                    else :
                        os.system("firewall-cmd  --permanent --zone=public --add-masquerade")
                        os.system("firewall-cmd --reload")
                        os.system("systemctl restart docker")
                        print("Docker is successfully installed in your system")
        elif ch1_docker==2:
            os.system("systemctl start docker")
        elif ch1_docker==3:
            os.system("systemctl status docker")
        elif ch1_docker==4:
            os.system("docker images")
        elif ch1_docker==5:
            docker_name = input("Enter the container name or ID of that you want to remove ")
            os.system("docker rm -f {}".format(docker_name))
        elif ch1_docker==6:
           os.system("docker rm -f $(docker ps -aq)")
        elif ch1_docker==7:
            os.system("systemctl stop docker")
        elif ch1_docker==8:    
            docker_name = input("Enter name which you want to give :- ")
            image_name = input("Enter image name :- ")
            tag = input("Enter Image tag :- ")
            os.system("docker run -dit --name {} {}:{}".format(docker_name,image_name,tag))
        elif ch1_docker==9:
            break
        else :
            print("please enter correct option")
def networking():
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
            os.system("systemctl stop firewalld")
        elif op=='b':
            os.system("systemctl start firewalld")
        elif op=='c':
            os.system("yum install httpd")
        elif op=='d':
            os.system("systemctl start httpd")
            os.system("cd /var/www/html/")
            os.system("vi page.html")
        elif op=='e':
            os.system("firefox page.html")
        elif op=='f':
            os.system("systemctl status httpd") 
        elif op=='g':
            os.system("ifconfig enp0s3")     
        elif op=='h':
            break
        else :
            os.system("Enter correct option")
def package_management():
    while(1):
        print("*******************************************Package Management*********************************** ")
        print("""

                    \t 1 To check package install or not
                    \t 2 To install package
                    \t 3 To remove package
                    \t 4 To return to main menu

        """)
        print("***********************************************************************************************")
        ch1_pkg=int(input("please select any option number from the above options :"))
        if ch1_pkg==1:
            package = input("Enter Package Name Which you Want To Check : ")
            os.system("rpm -q {}".format(package))
        elif ch1_pkg==2:
            pack1=input("Enter Package Name Which you  Want To install : ")
            check_pack = os.system("rpm -q {}".format(pack1))
            if check_pack != 0 :
                print(" The package {} is not installed in your system  ".format(check_pack))
                print("wait it is downlaoding")
                os.system("dnf install {} -y".format(check_pack))
            else : 
                print("{} already in our system".format(check_pack))
        elif ch1_pkg ==3:
            pack2=input("Enter Package Name Which that you  Want To remove : ")
            check_pack1 = os.system("rpm -q {}".format(pack2))
            if check_pack1 != 0 :
                print(" The package {} not installed in your system  ".format(check_pack1))
                print("wait till it is remove")
                os.system("dnf remove {} -y".format(check_pack1))
            else:
                print("you does not have {} in your system".format(check_pack1))

        elif ch1_pkg==4:
            break
        else :
            os.system("Enter correct option")     
def basic_operation():
    while True:
        input("Enter To Continue...")
        os.system("clear")
        print("""
        \n
        Press 1: Today's Date
        Press 2: Calender
        Press 3: Check Current User
        Press 4: Create User
        Press 5: Check User 
        Press 6: Delete Created User
        Press 7: Jobs Status
        Press 8: Ping to Google
        Press 9: Exit to main menu
        """)
    
        ch = input("Enter your choice :- ")
        print(ch)
  


    
        if int(ch) == 1:
                    os.system("date")
        elif int(ch) == 2:
                    os.system("cal")
        elif int(ch)==3:
                    #os.system("whoami")
                    print("Currently running user is :- ")
                    os.system("whoami")
        elif int(ch)==4:
                    print("Enter user name which you want to create:")
                    createUser =input()
                    os.system("useradd {}" . format(createUser))
                    print("{} User is created successfully".format(createUser))
        elif int(ch)==5:
                    os.system("cat /etc/passwd")
        elif int(ch)==6:
                   print("Enter user name which you want to delete")
                   delete_user = input()
                   os.system("userdel {}" . format(delete_user))
                   print("{} User deleted successfully".format(delete_user))
        elif int(ch)==7:
                   os.system("jobs")
        elif int(ch)==8:
                  os.system("ping www.google.com")
        elif int(ch)==9:
                  break
    else:
        print("Invalid menu Option, Try Again ")
        input("Enter To conti..")
def aws_management():
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
            os.system("aws configure ")
        elif int(ch)==2:
            key_name=input(" Enter the key name:   ")
            os.system(" aws ec2 create-key-pair --key-name {}".format(key_name))
        elif int(ch)==3:
            sg_name=input(" Enter the name for security group :  ")
            sg_desc=input(" Enter the description for security group:  ")
            os.system(" aws ec2 create-security-group --group-name {} --description {}".format(sg_name,sg_desc))
        elif int(ch)== 4:
            key_name=input(" Enter the key name:   ")
            sg_name=input(" Enter the ID for security group :  ")
            subnet_id=(" Enter the subnet id: ")
            os.system(" aws ec2 run-instances  --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --key-name {} --security-group-ids {} --subnet-id {}".format(key_name,sg_name,subnet_id))
        elif int(ch)==5:
            aws_vol=int(input("Enter Storage size(GB):Ex : 1"))
            os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {}".format(aws_vol))
        elif int(ch)==6:
            break
        else:
            print("invalid choice")          
