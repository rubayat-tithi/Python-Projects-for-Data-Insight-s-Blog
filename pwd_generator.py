#Author
#Mst. Rubayat Yasmin


#import the necessary modules!
import random
import string

print('Hello! \n Welcome to Password generator!')

#input the length of password
pwd_length = int(input('\nEnter your preffered passward length: '))                      

#define data
pwd_lower = string.ascii_lowercase
pwd_upper = string.ascii_uppercase
pwd_num = string.digits
pwd_symbols = string.punctuation
#string.ascii_letters

#combine the data
all = pwd_lower + pwd_upper + pwd_num + pwd_symbols

#use random 
cal = random.sample(all,pwd_length)

#create the password 
password = "".join(cal)

#print the password
print(password)
