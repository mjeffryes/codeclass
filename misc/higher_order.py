# higher_order.py

def times2(x):
	""" Accpets a number and returns twice that number"""
	return x * 2

def  plus2(x):
	""" Accepts a number and returns that number plus two"""
	return x + 2

def onIntOrString(fn, x):
	""" Coerces the input x to an integer before calling fn(x) """
	return fn(int(x))

print(onIntOrString(times2, 5))
print(times2('5'))
print(onIntOrString(times2, '5'))

















def twice(fn):
	"""
	  Accepts a one parameter function and returns a new function that applies the input fucntion twice
	"""
	# this is the same as:
	# x2 = lambda i: fn(fn(i))
	def x2(i):
		return fn(fn(i))
	return x2


times2twice = twice(times2)
print(times2twice(5))

plus2twice = twice(plus2)
print(plus2twice(5))

def onIntOrString(fn):
	""" Coerces the input x to an integer before calling fn(x) """
	return lambda x: fn(int(x))

safeTimes2 = onIntOrString(times2)

print(times2('5'))
print(safeTimes2('5'))
