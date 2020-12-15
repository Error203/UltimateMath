
# you might need this: ² √ ⋅

def make_discriminant(a, b, c):
	"""
	This function accepts a, b and c params
	and returns discriminant of theese numbers
	also returns way of solution
	"""

	discriminant_way = f"{b}² - 4x{a}x{c}"

	if a != 0:

		solution = b ** 2 - 4 * a * c
		
		if solution < 0:
			print("There is no solutions.")
			return False, False
			# zero solutions

		elif solution == 0:
			return solution, False
			# one solution

		elif solution > 0:
			return solution, True
			# two solutions

	else:
		return False, False

	print(discriminant_way)


def make_general_solution(a, b, D):
	"""
	This function accepts a, b and D(discriminant)
	and returns to you x1 and x2 if
	this is real
	by the way prints to you the way of the solution
	"""
	if D[1]:
		# then 2 solutions
		x1 = ((-b + (D[0] ** 0.5)) / (2 * a))
		x2 = ((-b - (D[0] ** 0.5)) / (2 * a))
		return f"x1 = {x1}\nx2 = {x2}"
	
	elif D[0] == 0:
		# then 1 solution
		x = (-b / (2 * a)) # we can use whatever + or -
		return f"Only one x: {x}"

	else:
		# then game over
		return "Sorry, but there is no solution..."
