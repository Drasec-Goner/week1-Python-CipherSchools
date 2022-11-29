name = "Madara"
age = 333
print("hello "+name+" your age is "+str(age))#ugly synatx and tiring to write
#python 3 method
print("hello {} your age is {}".format(name,age+2)) #calculations also allowed
#3.6 method (best)
print(f"hello {name} your age is {age+2}")