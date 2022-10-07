import os

# get directory you are currently in
print(os.getcwd())

# create a new directory
os.mkdir('new_dir')

# change to a new directory
# os.chdir('new_dir')

# remove/delete a directory
# only removes empty directory
os.rmdir("new_dir")

# get a list of all files and sub-directories in directory
# first get the absolute path to the directory
print(os.path.abspath('shecoders_website'))
print(os.listdir('/home/sav/shecoders_website'))


# a script to return all the files and folders contained in a website directory
dir = '/home/sav/shecoders_website'
for name in os.listdir(dir):
    # the join function lets you be independent of the os
    # here you join the file name and the directory name to get the fullname of the file or the sub-directory
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
