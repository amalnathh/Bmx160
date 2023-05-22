# BMX160 Imu Calibration Using Pi Pico

## Information
This repo contains method to calibrate the BMX160X imu from bosch sensortec.

## Install & Dependence
- machine
- math
- time

## Dataset Preparation
| Dataset | Download |
| ---     | ---   |
| BMX160 | [download](https://www.mouser.com/pdfdocs/BST-BMX160-DS000-11.pdf) |
| Pi Pico | [download](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) |
| Pi Pico Pinout | [download](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) |

 

## Directory Hierarchy
```
|—— .picowgo
|—— lib
|    |—— bmx160.py
|    |—— deltat.py
|    |—— fusion.py
|    |—— imu.py
|—— main.py
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


