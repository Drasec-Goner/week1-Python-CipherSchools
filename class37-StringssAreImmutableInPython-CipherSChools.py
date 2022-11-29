#strings are immutable

string="String"
# string[1]="T"  throws an error

newString=string.replace("t","T")
print(newString)
