#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Select an option to zip or unzip


# In[ ]:


def zip(output_filename,usr1_input,dir_name):
    import shutil
    shutil.make_archive(output_filename, usr1_input, dir_name)


# In[ ]:


def unzip(filename,extract_dir):
    import shutil
    shutil.unpack_archive(filename, extract_dir)


# In[ ]:


usr_input = input("Select 1 to create zip or tar file \nSelect 2 to unzip or untar from a zipped or tar file: ")
while (usr_input != '1') and (usr_input != '2'):
    usr_input = input("Select 1 to create zip or tar file \nSelect 2 to unzip or untar from a zipped or tar file \n: ")

if usr_input == '1':
    output_filename = input("choose a output_filename: ")
    dir_name = input("choose a dir_name to zip or tar: ")
    usr1_input = input("choose a format (tar or zip): ")
    zip(output_filename,usr1_input,dir_name)
    
elif usr_input == '2':
    filename = input("choose the zip or tar filename: ")
    extract_dir = input("choose a dir_name to zip or tar: ")
    unzip(filename, extract_dir)


# In[ ]:




