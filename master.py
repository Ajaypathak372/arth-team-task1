import os
nn_ip = input("Enter the IP of the Hadoop master :- ")
os.system("bash ~/arth-team-task1/hadoop")
nn_dir = input("Enter the directory name for hadoop master :-  ")
os.system("mkdir -p /{}".format(nn_dir))
fin = open("hdfs-site.xml", "rt")
fout = open("/etc/hadoop/hdfs-site.xml", "wt")
for line in fin:
    fout.write(line.replace('path', '{}'.format(nn_dir)))
fin.close()
fout.close()
fin = open("core-site.xml", "rt")
fout = open("/etc/hadoop/core-site.xml", "wt")
for line in fin:
    fout.write(line.replace('ip', '{}'.format(nn_ip)))
fin.close()
fout.close()

os.system("hadoop-daemon.sh start namenode")
print("Hadoop master(NameNode) Setup Successfully")
