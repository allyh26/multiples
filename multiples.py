userNumb = input("Tell me a number. ")

userNumb = float(userNumb)

for multiple in range(2,10):
	answer = userNumb * multiple
	print("{} times {} is {}.".format(userNumb, multiple, answer))