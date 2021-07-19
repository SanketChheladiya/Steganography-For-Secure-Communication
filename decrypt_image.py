
import cv2
import string

d={}
c={}

p=string.ascii_lowercase

for i in range(26):
    d[p[i]]=i
    c[i]=p[i]
    
#print(c) 
    
x=cv2.imread("encrypted_img_2.jpg")

key=input("Enter key to edit : ")   

kl=0
z=0 #decides plane
n=0 #number of row
m=0 #number of column

decrypt=""

for i in range(12):
    decrypt+=c[x[n,m,z]^d[key[kl]]]
    n=n+1
    m=m+1
    z=(z+1)%3
    kl=(kl+1)%len(key)


print("\nKey Matched. Image Decryption Successfully Completed.")

print("\nEncrypted Text : ",decrypt,end="\n\n-----------------\n\n")




    