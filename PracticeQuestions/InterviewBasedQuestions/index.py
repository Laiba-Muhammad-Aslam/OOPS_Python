def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

print(is_palindrome_number(121))  
print(is_palindrome_number(123))  


# Hackerrank 

"""
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
Task

Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Output Format
Print the amount of money earned by Raghu.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output: 200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55 + 45 + 40 + 60 = $200


# SOLUTION 

x = int(input())
shoe_sizes = list(map(int, input().split()))
n = int(input())
total = 0

for _ in range(n):
    size, price = map(int, input().split())
    if size in shoe_sizes:
        total+=price
        shoe_sizes.remove(size)

print(total)

"""

"""
Check the status - Python
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.

Examples: 

Input: a = 1, b = -1, flag = False
Output: True
Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.
Input: a = -182, b = -9121, flag = True
Output: True
Explanation: Since both a and b are negative and flag is True, condition 2 holds true, so the function returns True.
Input: a = 5, b = 3, flag = True
Output: False
Explanation: Neither condition 1 nor condition 2 holds, so the function returns False.
Constraints:
-10 <= a, b <= 10
flag ∈ {True, False} 
"""

#Solution:

class Solution:
    def checkStatus(self, a, b, flag):
        if(flag == False and ((a >= 0 and b < 0) or (a < 0 and b >= 0))):
            return True
        elif(flag == True and a < 0 and b < 0):
            return False
        else:
            return False