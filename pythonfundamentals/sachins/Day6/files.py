#open and manipulate files
my_file = open("my_text.txt")
file_content = my_file.read()
print(file_content)
my_file.close()


#print first line in code
my_file = open("my_text.txt")

first_line = my_file.readline()
print(first_line)

my_file.close()

#read second line
my_file = open("my_text.txt")
my_file.readline()
print(my_file.readline())

#write file
my_file = open("my_file.txt", "w")
my_file.write("New text")
my_file.close()

my_file = open("my_file.txt","r")
print(my_file.read())

#append file content
my_file = open("my_file.txt","a")
my_file.write("New login")
my_file.close()

my_file = open("my_file.txt","r")
print(my_file.read())

#write list items with tab
record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]
my_file = open("register.txt","a")
for l in record_last_session:
    my_file.writelines(l + "\t")
my_file.close()

my_file = open("register.txt","r")
print(my_file.read())

