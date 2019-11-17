#import os

#print(os.getcwd())

#os.chdir('/home')
#print(os.getcwd())

#os.mkdir('new_dir')
#print(os.listdir())

#os.rename('new_dir', 'r_new_dir')
#print(os.listdir())

#os.remove('text.txt') # remove file
#print(os.listdir())

#os.rmdir('r_new_dir') # remove directory
#print(os.listdir())


'''remove a non-empty directory'''
#import shutil

#shutil.rmtree('example')
#print(os.listdir())