#Bulk Rename Files
import os 

def main():
    i = 0
    path = "path names with front slash instead of backslash"
    for filename in os.listdir(path):
        #basename - .dbf 
        #change to csv 
        #get rid of i ?
        my_dest = "img" + str(i) + ".csv"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main() 
