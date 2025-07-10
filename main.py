#Writing to a file.
file = open("filetest.txt", "w")
file.write("Hello, World!\n")
file.write("Writing to a file")
file.close()
#Reading to a file.
file = open("filetest.txt", "r")
content = file.read()
print(content)
file.close()
#Reading file line by line.
file = open("filetest.txt", "r")
for line in file:
    print(line.strip())
file.close()
#Append to a file.
file = open("filetest.txt", "a")
file.write("\nAppend Line")
file.close()
#Handling files not found.
try:
    file = open("nonexisting.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("The file does not exist.")
#Read, Replace, Write
with open("filetest.txt", "r")as file:
    content = file.read()
    updated_content = content.replace("Hello","Hi")
    with open("filetest.txt", "w")as file:
        file.write(updated_content)
        print(updated_content)
    file.close()
file = open("allaboutcambourne.txt", "w")
file.close()
with open("allaboutcambourne.txt", "r")as file:
    content = file.read()
    updated_content = content.replace("Cambourne","Town")
    updated_content = updated_content.replace("development","construction")
    with open("allaboutcambourne.txt", "w")as file:
        file.write(updated_content)
        print(updated_content)
        file.close()
