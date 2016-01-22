def abc(no):
	acc = 0
	for i in range (1,no,2):
		acc = acc + i
	print (acc)


print("This calculator helps you calculate the sum of all the odd numbers up to the number 'n', excluding the number itself")
n = int(input("Enter 'n': "))
abc(n)
