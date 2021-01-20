file = open("C:\\Users\\ankita upadhyay\\Documents\\Notepad\\lol.txt","r")
counter=0

content = file.read()
clist = content.split("\n")

for i in clist:
    if i:
        counter=counter+1
print("Number of lines in file: ")
print(counter)
