import time

def turn_right(degree, PBR):
	PBR.SetMotor1(-1)
	PBR.SetMotor2(0)
	time.sleep(degree/90)


def turn_left(degree, PBR):
	PBR.SetMotor1(0)
	PBR.SetMotor2(1)
	time.sleep(degree/90)


def stop(time, PBR):
	PBR.MotorsOff()
	time.sleep(time)

def bypass(PBR):
	#right 45
	PBR.SetMotor1(-1)
	PBR.SetMotor2(0)
	time.sleep(0.5)
	#straight
	PBR.SetMotor1(0.7)
        PBR.SetMotor2(-0.7)
	time.sleep(2)
	#left 90
	PBR.SetMotor1(1)
	PBR.SetMotor2(0)
	time.sleep(0.8)
	#straight
	PBR.SetMotor1(0.7)
        PBR.SetMotor2(-0.7)
	time.sleep(1)
	#right 45
	PBR.SetMotor1(0)
	PBR.SetMotor2(-1)
	time.sleep(0.5)
