#Decimal to octal
num = int(input("Enter number"))
o = oct(num)
print("The octal value of this", num, "is ", o)



#Reversing number
number = int(input("Enter the integer number: "))  
revs_number = 0  
  
while (number > 0):  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  

print("The reverse number is : {}".format(revs_number))


# Displaying the Fibonacci sequence recursively
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


#Finding nth term of Fibonacci sequence
def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
		return b
print(fibonacci(9))

