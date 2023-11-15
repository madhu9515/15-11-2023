'''Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second
file'''

file1=input("Enter First Filename : ")
file2=input("Enter Second Filename : ")
# open first file in read mode
fn1 = open(file1, 'r') 

# open second file in write mode for writing first file script
fn2 = open(file2, 'w') 

# read the words line by line
cont = fn1.readlines() 
#getting each character from first file
for i in range(0, len(cont)):
    fn2.write(cont[i]) 

#closing the file after added script to second file
fn2.close() 
print("Content of first file copied to second file ")

# oopen the scond file
fn2 = open(file2, 'r') 
  
# read the content of second file
cont1 = fn2.read() 
  
#print all the script
print("Content of Second file :")
print(cont1) 
  

fn1.close() 
fn2.close() 
