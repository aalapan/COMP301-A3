import shutil

filename1 = input("Enter source file name:")
file1 = open(filename1, 'rb')

filename2 = input("Enter destination file name:")
file2 = open(filename2, 'wb')

shutil.copyfileobj(file1, file2)