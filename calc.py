#!/usr/bin/env python3

import sys

def calculate(expression):

	# case where the command line argument is an integer
	if(len(expression.split()) == 1):
		try:
			return int(expression.split()[0])
		except:
			print("Invalid Arguments")
			return

	# remove outer parentheses surrounding expression
	expression = expression[1:len(expression)-1]

	# stack used for keeping track of parentheses in nested expressions
	stack = []

	# operator, and operands[] variables used to store the function and sub-expressions
	operator = ''
	operands = ['', '']


	# lParen and rParen variables to represent '(' and ')' characters respectively
	lParen = '('
	rParen = ')'

	# add the characters representing the function to the op variable and concatenate the expression to remove the outer function
	for i in range(0, len(expression) -1):
		if(expression[i] == ' '):
			expression = expression[i+1:len(expression)]
			break

		operator += expression[i]


	# case dealing with nested expressions
	if(expression[0] == lParen):
		stack.append(lParen)
		x=1

		while len(stack) != 0:
			if(expression[x] == lParen):
				stack.append(lParen)
			if(expression[x] == rParen):
				stack.pop()
			x+=1

		operands[0] = expression[0:x]
		expression = expression[x+1:len(expression)]
	# case dealing with non-nested expression
	else: 
		for i in range(0,len(expression)):
			if(expression[i] == ' '):
				expression = expression[i+1:len(expression)]
				break
			operands[0] += expression[i]

	operands[1] = expression

	# evaluate the expression based on the operator type
	if(operator == 'add'):
		return(calculate(operands[0]) + calculate(operands[1]))
	elif(operator == 'multiply'):
		return(calculate(operands[0]) * calculate(operands[1]))
	else:
		print("Not a recognized operator")
	


if __name__ == '__main__':
	try:
		expression = sys.argv[1]
		print(calculate(expression))
	except:
		print("Invalid Arguments")





