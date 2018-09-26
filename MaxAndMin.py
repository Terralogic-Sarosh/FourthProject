n=input("Enter the five number by providing one space between each number : ")
l=n.split()
print(l)
s=0
l1=[]
for i in range(0,5):
    for j in range(0,5):
        if(i!=j):
            s+=int(l[j])
    l1.append(s)
    s=0
l1.sort()
print(l1[0]," ",l1[4])


