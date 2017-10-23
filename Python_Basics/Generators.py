# Generators a way to apply functions to a loop
# Below is example for looping over a value 
"""
def counter():
	i=0
	while True:
		i+=1
		return i
a = counter()
print a
type(a)

# In the above function, no matter what, it always returns only when, and type of the value is int.
"""
# But generator store the value of previous execution thus saving the memory/cpu memory
# type of the object is also shown as generator

def counter():
	i = 0
        while True:
		i+=1
		yield i ## yield will be used when you want it make the return value as generator ##
a = counter()
for n in range(1,10):
	print next(a)
