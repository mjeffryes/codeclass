# add_list.py
print('loaded add_list')

# add_list: Sum a list of integers
def add_list(L):
  """
  Accepts: a list of integers and returns an integer representing the sum
  If the list is empty returns 0
  """
  # base case
  if L == []:
  	return 0

  # recursive step
  return L[0] + add_list(L[1:])


# factorial: Given a positive number return it's factorial
def factorial(n):
   """ 
   Accepts: a positive integer and returns an integer representing the the factorial of its input
   """
   # base case
   if n == 0:
   	   return 1

   # recursive step
   return n * factorial(n-1)



