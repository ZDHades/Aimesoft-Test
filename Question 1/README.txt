Solution for Question 1 explained:

To begin, I used a list comprehension to create the list of names for each of the files.

Next, I declare the variable that will store all of the data that is being read as a list.

The first method created was to generate the many numbers that will be written into each of the files.
I arbitrarily chose 100 numbers on each file, each being a random integer between 1 and 1000.

The next method is to create the files. I iterate through the list of file names, and for each I call the 
get_data method to generate a new random set of numbers to write into the file. I use \r as my new line character
since I am working on Windows. 

The next method is for reading each of the files and extracting the data inside them. The data will have to be cleaned
before appending it to the output file because the instrutions require the output file to also be sorted, and since 
each of the files contain strings of int+\r, the sorted method cannot be used on them as it will slightly malfunction due to 
the data type. 

Next we have the clean output method which uses a list comprehension to iterate through the output_file_data list. 
For each value in the original list, I used the .split method to seperate the number from the \r, and we take the 0th index of the 
split method since I am only interested in that. Since the number is still a string, we change the data type to an integer so 
it can be compatiable with the sorted method I used. 

The next method is used to create the output file, which takes the cleaned data gathered from each of the other files and 
appends them each to a new line, again using the \r keyword.

The final method is just used to call all of the previous ones so that the program can be run much easier.

The directory currently contains a working solution file, the test file and this .txt file. To see the solution in action,
run the q1.py file from the folder menu (not via command line in console or command prompt). Doing so will create 1k random .txt files and the output .txt file. If the 
file is run form the command line, all of the files will be created in the parent folder to this one. 


- UNITTEST -

Since I used randomly generated numbers, each iteration of the program would yield different numbers for each file so I 
used unittest to check if the output file produced a set of numbers that were all sorted and if the length of the numbers in the final 
file was equal to the amount of numbers present in all of the files. Both tests run OK with time of .301s

To run the unittest, first make sure the q1.py file has been run. Then CD into the folder that contains test_q1.py and 
run it from the console on either your editor or in command prompt!