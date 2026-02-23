#File Handling 
# Storing The data in the disk not in the ram 
# In variable  data is store , for a temporary purpose.
#We create a file to store some data 

#here we read & write the data also creates the file and apppend the data.

#lifecycle of file handling 
#file open hogii

#mode: r:read, w:write,a:append,x:create

#syntax
#open(filename,mode)

#file use hogii
#file close hogii



# f=open("demo.txt",'a')#//here 'a', 'w','r','x'

# f.write("This is New Line")

# f.close()

# with open("demo.txt",'r') as file:
#     print(file.readlines()[1])

#Read()
#Readline()one line read only  for the that specific text file
#Readlines() and in this we will read many in one list ["" ,""]


#API : hit dat and Time mil jaye in my log file. suppose kyse 
# from datetime import datetime
# def log_message(message):
#     with open('app.log','a') as file:
#         file.write(f"{datetime.now()}-{message}\n")

# # log_message("data Accessed")

# # log_message("Payment request")
# log_message("payment Done")


# r+ : read and write only if file exists,
# w+ : it also read and writes the data , moremover it also creates the file if not exists,
# a+ : it used to append the dta tin the file and also creates the file if not exists .

# with open("demo1.txt",'w+')as file:
#     file.write("This is new file ")
# with open("demo.txt",'r+')as file:
#     file.write("\n This is new file ")

#CSV 
# import csv
# data = [
# ["shivang",24],
# ["Shub",22],
# ["shivan",25],
# ]
# with open("data.csv",'w')as file:
#     writer=csv.writer(file)
#     writer.writerows(data) #createing csv file and also writeing its data 

# with open("data.csv",'r')as file:
#     writer=csv.reader(file)
#     for row in writer:
#         print(row)    # Reading 









