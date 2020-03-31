import time
import datetime

for x in range(6):
	print ("###Deploying DB part {}###".format(x))
	time.sleep(2)

now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("######DB deploy completed at {}######".format(now))
