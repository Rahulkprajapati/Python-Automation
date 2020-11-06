import os

while True:
    os.system("clear")
    if int(cmd) == 2:
        print("""
        \n
            Press 1 : To Configure Namenode 
            Press 2 : To Configure Datanode
            Press 3 : To Configure Client      
        
        """)
        h = int(input("Want to Configure:   "))
        if h == 1:
            print("Configuring Namenode")
            print("\n\n")
            ip = input("Enter the IP of Namenode:  ")
            print("Install java-jdk and hadoop software")
            os.system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
            print("Successfully installed all required softwares")
            print("\n\n")
            print("Configure HDFS file")
            os.system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
            os.system("scp /hadoop/namenode/hdfs-site.xml {}:/etc/hadoop".format(ip))
            print("\n\n")
            print("Configure core file")
            os.system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
            os.system("scp /hadoop/namenode/core-site.xml {}:/etc/hadoop".format(ip))
            print("\n\n")
            print("Setting up dir for Connecting with datanodes")
            os.system("ssh {} mkdir /nn".format(ip))
            print("Directory successfully created")
            print("\n\n")
            print("Format the Namenode")
            print("hadoop namenode -format")
            os.system("ssh {} hadoop namenode -format".format(ip))
            print("Successfully formated the Namenode")
            print("\n\n")
            print("Start the Namenode")
            print("hadoop-daemon.sh start namenode")
            os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
            print("\n\n")
            print("Status of Namenode")
            print("jps")
            os.system("ssh {} jps".format(ip))
            print("Running Succesfully")
            print("\n\n")
        
        elif h == 2:
            print("Configuring Datanode")
            print("\n\n")
            ip = input("Enter the IP of Datanode:  ")
            print("Install java-jdk and hadoop software")
            os.system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
            print("Successfully installed all required softwares")
            print("\n\n")
            print("Configure HDFS file")
            os.system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
            os.system("scp /hadoop/datanode/hdfs-site.xml {}:/etc/hadoop".format(ip))
            print("\n\n")
            print("Configure core file")
            os.system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
            os.system("scp /hadoop/datanode/core-site.xml {}:/etc/hadoop".format(ip))
            print("\n\n")
            print("Setting up dir for datanode")
            os.system("ssh {} mkdir /dn1".format(ip))
            print("Directory successfully created")
            print("\n\n")
            print("Start the Datanode")
            print("hadoop-daemon.sh start datanode")
            os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
            print("\n\n")
            print("Status of Datanode")
            print("jps")
            os.system("ssh {} jps".format(ip))
            print("Running Succesfully")
            print("\n\n")
        
        elif h == 3:
            print("Configuring Client")
            ip = input("Enter the IP of Client:  ")
            print("Install java-jdk and hadoop software")
            os.system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
            print("Successfully installed all required softwares")
            print("\n\n")
            print("Configure HDFS file")
            os.system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
            os.system("scp /hadoop/client/hdfs-site.xml {}:/etc/hadoop".format(ip))
            print("\n\n")
            print("Configure core file")
            os.system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
            os.system("scp /hadoop/client/core-site.xml {}:/etc/hadoop".format(ip))
            print("Configured successfully")
            print("\n\n")

        else:
            exit()

            




        
       

