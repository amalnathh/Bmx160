import time  
from fusion import Fusion
from imu import CalibrateIMU
from machine import Pin

led = Pin(25, Pin.OUT)
 

fuse = Fusion() 
imu = CalibrateIMU()
imu.begin()
init_fusion = True
(mag,gyro,accel) = imu.getAllDataCalibrated()

Timing = True 
if Timing: 
    start = time.ticks_us()  # Measure computation time only
    fuse.update(accel, gyro, mag) # 1.97mS on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (mS):", t/1000)

def initFuseDelay():
    print("Fuse initializing for first time")
    i = 0
    global init_fusion 
    init_fusion = False
    while i < 100:
        fuse.update(accel, gyro, mag) # Note blocking mag read
        i += 1 
        time.sleep_ms(51)

while True: 
    (mag,gyro,accel) = imu.getAllDataCalibrated() 
    led.toggle()
    if(init_fusion):
        initFuseDelay()


    # formatted_mag = tuple("{:.3f}".format(val) for val in mag)
    # print(str(formatted_mag[0])+","+str(formatted_mag[1])+","+str(formatted_mag[2]))

    fuse.update(accel, gyro, mag) 
    print(str(fuse.heading)+","+str(fuse.pitch)+","+str(fuse.roll))
    
    time.sleep_ms(100) 

