def prime_checker(num):
	is_prime = True
	for i in range(2, num):
		if num % i == 0:
			is_prime = False
	if is_prime:
		print("Prime Number")
	else:
		print("Not a prime number")


n = int(input("Enter a number: "))
prime_checker(n)
