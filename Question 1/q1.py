# Question 1:
# -  Create manually 1000 text files in a directory, each text file contains many numbers, each number on a line, arranged in ascending order. 
# Then write a multithreaded Java or Python program that merges 1000 files in ascending order. Restrict use of the libraries.
# - Write the unittest to make sure the program runs properly.

import random as r

class Question_1:
    # Using list comprehension to create names for each of the files
    file_names = [x for x in range(1, 1001)]
    # file_names = [1,2,3]
    output_file_data = []

    # Creating a method to generate a list of random numbers that can be called for each file
    @classmethod
    def get_data(self):
        return sorted([r.randint(1,1000) for x in range(100)])
    
    # Creating the 1000 files and filling them with the randomly generated data
    @classmethod
    def create_files(self):
        for name in self.file_names:
            f = open(f"{name}.txt","w+")
            data = self.get_data()
            for line in data:
                f.write(f"{line}\r")
            f.close()

    # Creating a method that can read each of the files
    @classmethod
    def read_files(self):
        for name in self.file_names:
            f = open(f'{name}.txt')
            for line in f:
                self.output_file_data.append(line)
            f.close()
    
    # Creating a method to clean the output data
    @classmethod
    def clean_output(self, y):
        return sorted([int(x.split()[0]) for x in y])

    # Creating a method that will create the output file and write the gathered data
    @classmethod
    def create_output_file(self):
        output = self.clean_output(self.output_file_data)
        f = open("output.txt", "w+")
        for line in output:
            f.write(f"{line}\r")
        f.close()

    # Creating a method where all of the previous can be run to get the solution
    @classmethod
    def solution(self):
        self.create_files()
        self.read_files()
        self.create_output_file()

Question_1.solution()
