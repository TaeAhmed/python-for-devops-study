#Objective:
#This is a python script to work as bash ls
#uses input() at runtime
#input is paths that are to be listed seperated by space example "/opt /tmp /"
#handle known exceptions
import os
import print_list_textwrap

inputPaths = input("Please input the directories to list sperated by space: ").split()

for path in inputPaths:
    try:
        listdir = os.listdir(path)  #returns files and dirs names in a path as list[str]
    except FileNotFoundError:
        print("Warning: looks like this path doesn't exist:",path,"\n")    
        continue
    except PermissionError:
        print("Warning: looks like you don't have permission to list this path:",path,"\n")    
        continue    

    print(path + ':')
    listdir.sort()
    print_list_textwrap.print_list_textwrap(listdir)
    if path != inputPaths[-1]:
        print()