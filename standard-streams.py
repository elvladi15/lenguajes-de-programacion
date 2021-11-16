import sys

print("Enter a message:")
message=sys.stdin.readline()

sys.stdout.write(f"Message: {message}\n")

sys.stderr.write("This is an error message.")