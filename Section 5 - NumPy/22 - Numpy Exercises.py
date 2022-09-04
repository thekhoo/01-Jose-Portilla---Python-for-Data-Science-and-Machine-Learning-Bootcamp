from contextlib import AsyncExitStack
import numpy as np

def print_answer(ques_num,ans):
    print(f"Question {ques_num}: {ans}\n")

# Question 1
# Create an Array of 10 zeros
q1_arr = np.zeros(10)
print_answer(1,q1_arr)

# Question 2
# Create an array 10 ones
q2_arr = np.ones(10)
print_answer(2,q2_arr)

# Question 3
# Create an array of 10 fives
q3_arr = np.array([5]* 10)
print_answer(3,q3_arr)

# Question 4
# Create an array of the integers from 10 to 50
q4_arr = np.arange(10,51,1)
print_answer(4,q4_arr)

# Question 5
# Create an array of all the even integers from 10 to 50
q5_arr = np.arange(10,51,2)
print_answer(5,q5_arr)

# Question 6
# Create a 3x3 matrix with values ranging from 0 to 8
q6_arr = np.arange(0,9,1)
q6_arr = q6_arr.reshape(3,3)
print_answer(6,q6_arr)

# Question 7
# Create a 3x3 identity matrix
q7_arr = np.eye(3)
print_answer(7,q7_arr)

# Question 8
# Use NumPy to generate a random number between 0 and 1
q8_arr = np.random.rand(1)
print_answer(8,q8_arr)

# Question 9
# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
q9_arr = np.random.randn(25)
print_answer(9,q9_arr)

# Question 10
# Create the following matrix
q10_arr = np.arange(0.01,1.01,0.01)
q10_arr = q10_arr.reshape(10,10)
print_answer(10,q10_arr)

# Question 11
# Create an array of linearly spaced points between 0 and 1
q11_arr = np.linspace(0,1,20)
print_answer(11,q11_arr)

"""
Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs.

array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
    
"""

mat = np.arange(1,26).reshape(5,5)

# Question 12
q12_mat = mat[2:,1:]
print_answer(12,q12_mat)

# Question 13
q13_mat = mat[3,4]
print_answer(13,q13_mat)

# Question 14
q14_mat = mat[0:3,1]
print_answer(14,q14_mat)

# Question 15
q15_mat = mat[4]
print_answer(15,q15_mat)

# Question 16
q16_mat = mat[3:]
print_answer(16,q16_mat)

# Question 17
q17_ans = mat.sum()
print_answer(17,q17_ans)

# Question 18
q18_ans = mat.std()
print_answer(18,q18_ans)

# Question 19
q19_ans = mat.sum(axis=0)
print_answer(19,q19_ans)




