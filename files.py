import os

print("File exists?:",os.path.exists("file.txt"))

f=open("file.txt","w")
f.write("Example\n")
f.write("Programming\n")

print("File exists?:",os.path.exists("file.txt"))

""" f=open("file.txt","a")
f.write("word\n") """

""" f=open("file.txt","r")
print(f.read()) """



""" print(os.remove("file.txt")) """