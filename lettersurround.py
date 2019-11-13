string1=input("Enter a string")
flag=True
c=string1[0]
l=len(string1)
s=string1[l-1]
for i in range(0,l):
    if c>='a' and ch<='z' or(s>='a' and s<='z'):
        flag=False
    else:
        for i in range(1,l-1):
            ch=string1[i]
            if string1[i-1]!='+' and string1[i+1]!='+':
                flag=False
                break
            else:
                flag=True
                
if flag==True:
    print("Yes")
else:
    print("No")
