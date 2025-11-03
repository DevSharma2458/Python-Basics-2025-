f = open("section9/practiceset/File In-Out Basics/notes.txt", "r")
content = f.read()
print(content)

# Alternative

with open("notes.txt", "w") as f:
    f.write("Learning Python is fun")

with open("notes.txt", "a") as f:
    print(f.read())