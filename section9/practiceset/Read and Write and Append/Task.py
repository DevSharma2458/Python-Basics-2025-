# f = open("section9/practiceset/Read and Write and Append/tasks.txt","w")
# string = '''
# 1 - Do the tasks said by harry bhaiya
# 2 - Create your own tasks
# 3 - Complete all of them
# '''
# f.write(string)

# f = open("section9/practiceset/Read and Write and Append/tasks.txt","r")
# content = f.read()
# print(content)

# f = open("section9/practiceset/Read and Write and Append/tasks.txt","a")
# string1 = '''
# Tasks Completed
# '''
# f.write(string1)

# f = open("section9/practiceset/Read and Write and Append/tasks.txt","r")
# content1 = f.readlines()
# print(content1)

# Alternative

with open("tasks.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open('tasks.txt', "a") as f:
    f.write(("Task Completed"))

with open("tasks.txt", "r") as f:
    for line in f.readlines():
        print(line)