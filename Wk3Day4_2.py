# Henry Rybolt

from numpy import *

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))

if Hours < 40:
	pay = RPH*Hours 
else:
	# if the number of hours is greater than 40, the overtime hours
	# will be payed at 1.5 times the normal hourly rate
	pay = RPH*40 + 1.5*(Hours - 40)

print 'Your pay is:', pay
