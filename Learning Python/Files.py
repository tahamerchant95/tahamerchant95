# Working with files is essential when you need to quickly make changes 
# need to open the file
# read the file 
# write changes to file
# use seek function to start going through file 
# readlines function to read the lines
# finally close the file 
# we are going to create a sample text file 
# using w or w+ will erase contents from file when writing some new changes 
# using a+ will append text at the end 
# using windows use \\ when defining path since python will treat it as escape character 
# using linux use / 



example_file=open('add your path here', 'a+')

example_file.write("this is some more new text") #writing text to file 

example_file.write("\nNeed to add more text for testing purposes") # adding more lines

example_file.write("\nadding some more text ")

example_file.seek(0) #setting cursor to start of file 

print(example_file.read()) #checking whether files have been written 

example_file.close() # closing the file 
