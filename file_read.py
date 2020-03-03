import numpy as np 

def file_read(file_name,nbasis):
#open the file
    input_file=open('s.dat')   #open the file

    file_content=input_file.readlines()# read the content

    input_file.close()            # close the file

    A=np.zeros([nbasis,nbasis])

    for line in file_content:
        V_line=line.rstrip
        V_line=V_line.split() 
        return A


print(file_content)
