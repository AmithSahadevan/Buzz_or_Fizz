n = input("Enter a number: ")
i = int(n)
l = list(n)

if l[len(l)-1] == "7":
	print("Buzz")
elif i % 7 == 0 or i % 10 == 7:
	print("Buzz")
else:
	print("Fizz")