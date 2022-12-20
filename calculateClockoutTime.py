

def numberToBase(n,b):
	if n == 0:
		return [0]
	digits = []
	while n:
		digits.append(int(n % b))
		n //= b
	return digits[::-1]

print(numberToBase(480+30,60))
class clocktime():
	def __init__(self, hour, minute):
		self.hour = hour
		self.minute = minute

def calculateDifference(start_time, end_time):
	start_minute, end_minute = start_time.minute, end_time.minute
	start_hour, end_hour = start_time.hour, end_time.hour
	minute_difference = end_minute - start_minute
	hour_difference = end_hour - start_hour
	if minute_difference < 0:
		hour_difference -= 1
		minute_difference *= -1
	return hour_difference, minute_difference

clockin = clocktime(hour=6,minute=30)
lunchstart = clocktime(hour=11,minute=00)
print(calculateDifference(clockin, lunchstart))
