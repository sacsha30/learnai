#
def open_read(myfile1):
    my_file = open(myfile1, "r")
    return my_file.read()

#
def overwrite(myfile2):
    my_file = open(myfile2, "w")
    my_file.write("content deleted")
    my_file.close()

#
def log_error(myfile3):
    my_file = open(myfile3, "a")
    my_file.write("an execution error has been registered")
    my_file.close()