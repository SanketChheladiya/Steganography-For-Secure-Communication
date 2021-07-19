
import cv2
import string
import os
import math
d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
  
  
#print(c)

x=cv2.imread("2.jpg")

p=x.shape[0]
q=x.shape[1]
print(p,q)

key=input("Enter key to edit(Security Key) : ")
text=input("Enter text to hide : ")

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    m=(m+1)%q
    if m==(q-1):
        n=n+1
    z=(z+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    kl=(kl+1)%len(key)
    
cv2.imwrite("encrypted_img_2.jpg",x) 
os.startfile("encrypted_img_2.jpg")
print("Data Hiding in Image completed successfully.",end="\n\n-----------------\n\n")
#x=cv2.imread(“encrypted_img.jpg")
    

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

ch = int(input("\nEnter 1 to extract data from Image : "))

if ch == 1:
    key1=input("\n\nRe enter key to extract text : ")
    decrypt=""

    if key == key1 :
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            m=(m+1)%q
            if m==(q-1):
                n=n+1
            z=(z+1)%3   
            kl=(kl+1)%len(key)
        print("Encrypted text was : ",decrypt,end="\n\n-----------------\n\n")
    else:
        print("Key doesn't matched.",end="\n\n-----------------\n\n")
else:
    print("Thank you. EXITING.",end="\n\n-----------------\n\n")
   

    
    
 
    
    
    