'''
VARIABLE= containers which stores data
DATATYPES= numericals( integers (int)....float...complex....boolean),  strings ""
Type Casting= its a way of converting one data type into another
'''
var1="54"
var2="25"
var3="hello world"
var4=65
'''
print(var3+var4)
this will give error because python cannot contatenate string and numerical data types together. For this we have to use type casting.
print(var3+str(var4))------this will now print helloworld65
print(int(var1)+int(var2))-------this will convert the string to numerical and then give the addition of the two integers
'''

'''
print("enter your 1st number")
n1=input()
print("enter your 2nd number")
n2=input()
print("sum of these numbers is",int(n1)+int(n2))
'''



