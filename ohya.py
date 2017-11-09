from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
    if pir.motion_detected:
        print("you moved")
    else:
        print("")
'''
    pir.wait_for_motion()
    print("you moved")
    pir.wait_for_no_motion()
'''
