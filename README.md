# BMX160 Imu Calibration Using Pi Pico

## Information
This repo contains method to calibrate the BMX160X imu from bosch sensortec.

## Install & Dependence in pico
- machine
- math
- time

## Datasheets
| Datasheet | Download |
| ---     | ---   |
| BMX160 | [download](https://www.mouser.com/pdfdocs/BST-BMX160-DS000-11.pdf) |
| Pi Pico | [download](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) |
| Pi Pico Pinout | [download](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) |


## Directory Hierarchy
```
|—— AccelerometerCalibration
|    |—— acceldata.txt
|    |—— magneto12.exe
|    |—— plot-calibration-data.py
|    |—— record-data.py
|—— LICENSE
|—— MagnetometerCalibration
|    |—— log-mag-readings.py
|    |—— mag-readings.txt
|    |—— magneto12.exe
|    |—— plot-calibration-data.py
|    |—— README.md
|—— PiPico
|    |—— .picowgo
|    |—— lib
|        |—— bmx160.py
|        |—— deltat.py
|        |—— fusion.py
|        |—— imu.py
|        |—— OnBoardComputer.code-workspace
|    |—— main.py
```

## Code Details
### Tested Platform
- software
  ```
  Python: 3.8.5 (anaconda)
  Micropython
  ```
- hardware
  ```
  Pi Pico H
  ```
 
## References
- [Accelerometer Calibration - Code](https://github.com/michaelwro/accelerometer-calibration)
- [Sensor Fusion Calibration - Code](https://github.com/micropython-IMU/micropython-fusion) 
  
## License
- [MIT License](/LICENSE)