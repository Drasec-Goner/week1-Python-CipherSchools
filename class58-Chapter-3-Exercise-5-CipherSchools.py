name=input("")
temp=[]
i=0
while i<len(name):
    if name[i] not in temp:
        print(name[i],name.count(name[i]))
    temp.append(name[i])
    i+=1



