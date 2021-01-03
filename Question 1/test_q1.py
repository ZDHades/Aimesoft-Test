import unittest
from q1 import Question_1

class test_Question_1(unittest.TestCase):
    def test_sorted(self):
        output = []
        f = open('output.txt')
        for line in f:
            output.append(line)
        f.close()
        test = Question_1.clean_output(output)
        self.assertTrue(all(test[i] <= test[i+1] for i in range(len(test)-1)))

    def test_length(self):
        output = []
        f = open('output.txt')
        for line in f:
            output.append(line)
        f.close()
        self.assertTrue(len(output)==100000)
        

if __name__ == '__main__':
    unittest.main()
