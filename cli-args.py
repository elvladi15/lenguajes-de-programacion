import sys

print("All arguments: ",sys.argv)

print(f"\nProgram name: {sys.argv[0]}\n")

print(f"My name is: {sys.argv[1]}\n")


a=int(sys.argv[2])
b=int(sys.argv[3])
print(f"{a} + {b} equals: {a+b}")