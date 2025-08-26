score = float(input('Enter score:\n>>'))
def grade_student(score):
	if 70 <= score <= 100:
		print('A')
	elif 60 <= score <= 69.9:
		print('B')
	elif 50 <= score <= 59.9:
		print('C')
	elif 40 <= score <= 40.9:
		print('D')
	elif 30 <= score <= 39.9:
		print('E')
	elif 0 <= score <= 29.9:
		print('F')
	else:
		print('INVALID SCORE!')


grade_student(score)
