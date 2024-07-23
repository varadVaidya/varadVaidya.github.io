---
layout: page
title: Trajectory Planning for Mobile Manipulation
description: Trajectory planning and simulation of Kuka youBot in Python
importance: 1
img: assets/img/kuka_youBot.png
category: [control, manipulation]
---
## Description

The trajectory planning for Mobile Manipulation project demonstrates the use on trajectory planning, kinematic simulation and control systems on a wheeled manipulator. This project is the final Capstone assignemnt of the Coursera specialization: Modern Robotics. The wheeled manipulator of choice is the Kuka youBot, with 4 omnidirectional wheels and a 5 DOF robotic manipulator attacehd to the wheel base.

* **Mobile Manipulator Simulation:** The Kuka youBot, comprising a 5 DOF robotic manipulator and a mobile base with 4 omnidirectional wheels, is simulated in Python to replicate its real world behavior. The mobile base is used to to make up for the loss of configuration space of the manipulator alone.

* **Trajectory Planning:** The project involves defining trajectories to guide the youBot's end effector from an initial position to a final position, for pick and place of a small cube. These trajectories are represented as a list of end effector positions in SE(3). This allows for simple control for pick and place activities.

* **Feedforward PI Control:** A feedforward PI control scheme is implemented to track the end effector along the desired trajectory. This generates a _Spatial Twist_ in the space frame which is used to calculate the required joint and wheel velocities using the space frame Jacobian. This ensures that the smoooth tracking of the desired trajectory is achieved. The Python library [```ModernRobotics```](https://github.com/NxRLab/ModernRobotics) is used for generation of the trajectories and in general mathematics of the project.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/youBot_error.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    A plot of the error achieved in one of the simulations. The orientation error stays 0 all throughout, while the positionial error stays close to 0.
</div>

* **Intergration with Coppelia Simulation:** A Coppelia sim tool of the project is utilised as a visualization tool to provide a visual representation of the youBot's motion during the simulation. It allows for an intuitive understanding of the robot's behaviout and assists in the validation and fine tuning of the planning and control algorithms.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/kuka_youBot.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    A frame of the simulation of youBot moving a cube from its initial position to final position.
</div>

## Mathematical Framework

unknown ETA :(. In the mean time visit the [capstone wesbite](https://hades.mech.northwestern.edu/index.php/Mobile_Manipulation_Capstone) for more mathematical details behind the project. Since this was a Capstone project of the Coursera project, the linked page was the main resource consulted.

## Links

* [GitHub Repository](https://github.com/varadVaidya/Capstone2.0)
* [Video Demo](https://www.youtube.com/watch?v=4ChucdYt1sA)
