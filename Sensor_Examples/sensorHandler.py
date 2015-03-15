from BrickPi import * 

def scan():
	result = BrickPiUpdateValues()
	if not(result):
		#gyro = BrickPi.Sensor[PORT_4]
		gyro = 100
		return gyro

def verifyDistance(dist):
	if(dist<=200):
		print("Distance lower")
		return False
	else:
		print("Distance higher")
		return True
		
def addToMap():
	print("added to map")
	
def move(directive):
	if(directive):
		print("turning")
		time.sleep(.5)
		return False
	else:
		print("moving")
		time.sleep(2)
		return True
	
def main():
	BrickPiSetup()   #setting brick interface
	BrickPi.SensorType[PORT_4] = TYPE_SENSOR_EV3_US_M0  #setting sensor type
	BrickPiSetupSensors() #setting sensors
	#mapLength = 2
	addToMap()
	while(True):
		sensorValue = scan()
		result = move(verifyDistance())
		if(result):
			addToMap()
	
main()
	