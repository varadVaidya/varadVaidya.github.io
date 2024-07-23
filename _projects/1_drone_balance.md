---
layout: page
title: Two-Arm Quadcopter Balance System
description: Two-arm quadcopter balance system with PID control and sensor estimation.
importance: 1
img: assets/img/2armPID.png
category: drone 
---
## Description

This project involved the design, manufacturing, and testing of a two-arm quadcopter balance system that utilized PID control for stable flight. The system was composed of two arms, each of which was attached to a BLDC motor. The motors were controlled by an Arduino Uno, which received input from an MPU 9250 IMU. The IMU provided data on the system's orientation, which was used by the Arduino Uno to calculate the necessary PWM signals to keep the system balanced.

A complementary filter was implemented to obtain accurate pitch estimates of the system. This filter utilized data from the MPU 9250 IMU to obtain accurate pitch estimates of the quadcopter system. By combining accelerometer and gyroscope measurements, the complementary filter provided reliable pitch information for effective balancing and control.

<!-- Insert image of 2armPID in assets/img -->
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/2armPID.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Challenges

The prototype that was designed, was made up of construction wood and threaded metal rods. This was done to keep the costs of the project low, and faster iterations between prototypes. All of these design imperfections meant that vibrations from the BLDC motors to affect the attitude measurments quite significantly.

Further work on this project was halted due to COVID-19 pandemic.

## Links

* [GitHub Repository](https://github.com/rajesh3699/2ArmPid)
* [Video Demo](https://www.youtube.com/watch?v=0rf5-bUTrOY)
