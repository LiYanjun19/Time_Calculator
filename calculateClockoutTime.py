import math
class clocktime():
	def __init__(self):
		self.input_time = int(input("input_time: "))
		self.minute = int(self.input_time % 100)
		self.hour = int((self.input_time - self.minute) / 100)
		return
	
	def numberToBase(self, n,b):
		if n == 0:
			return [0]
		digits = []
		while n:
			digits.append(int(n % b))
			n //= b
		return digits[::-1]

def calculateDifference(start_time, end_time):
	start_minute, end_minute = start_time.minute, end_time.minute
	start_hour, end_hour = start_time.hour, end_time.hour
	minute_difference = end_minute - start_minute
	hour_difference = end_hour - start_hour
	if minute_difference < 0:
		hour_difference -= 1
	return [hour_difference, minute_difference]

clockin = clocktime()
lunchstart = clocktime()
lunchend = clocktime()

minutes_left = 60 - calculateDifference(clockin, lunchstart)[1]
hours_left = 8 - calculateDifference(clockin, lunchstart)[0]
if minutes_left >= 60:
	#hours_left -= 1
	minutes_left = minutes_left % 60
print("hours left", hours_left, "minutes left = ", minutes_left)

clockout_minute = minutes_left + lunchend.minute
clockout_hour = hours_left + lunchend.hour
if clockout_minute >= 60:
	clockout_hour += 1
	clockout_minute = clockout_minute % 60

print("clockout at",clockout_hour,":",clockout_minute)
