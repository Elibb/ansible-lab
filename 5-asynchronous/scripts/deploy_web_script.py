import time
import datetime

for x in range(12):
	print ("###Deploying WEB part {}###".format(x))
	time.sleep(2)

now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("######WEB deploy completed at {}######".format(now))
