---
title: "Trajectory Planning for Mobile Manipulation"
date: 2021-01-01
description: "Trajectory planning and simulation of Kuka youBot in Python"
image: "/img/kuka_youBot.png"
tags: ["control", "manipulation", "robotics"]
---

## Description

The trajectory planning for Mobile Manipulation project demonstrates the use of trajectory planning, kinematic simulation and control systems on a wheeled manipulator. This project is the final Capstone assignment of the Coursera specialization: Modern Robotics. The wheeled manipulator of choice is the Kuka youBot, with 4 omnidirectional wheels and a 5 DOF robotic manipulator attached to the wheel base.

- **Mobile Manipulator Simulation:** The Kuka youBot, comprising a 5 DOF robotic manipulator and a mobile base with 4 omnidirectional wheels, is simulated in Python to replicate its real world behavior. The mobile base is used to make up for the loss of configuration space of the manipulator alone.

- **Trajectory Planning:** The project involves defining trajectories to guide the youBot's end effector from an initial position to a final position, for pick and place of a small cube. These trajectories are represented as a list of end effector positions in SE(3). This allows for simple control for pick and place activities.

- **Feedforward PI Control:** A feedforward PI control scheme is implemented to track the end effector along the desired trajectory. This generates a *Spatial Twist* in the space frame which is used to calculate the required joint and wheel velocities using the space frame Jacobian. This ensures that the smooth tracking of the desired trajectory is achieved. The Python library [`ModernRobotics`](https://github.com/NxRLab/ModernRobotics) is used for generation of the trajectories and in general mathematics of the project.

![Error plot from simulation](/img/youBot_error.png)
*A plot of the error achieved in one of the simulations. The orientation error stays 0 all throughout, while the positional error stays close to 0.*

- **Integration with Coppelia Simulation:** A Coppelia sim tool of the project is utilized as a visualization tool to provide a visual representation of the youBot's motion during the simulation. It allows for an intuitive understanding of the robot's behavior and assists in the validation and fine tuning of the planning and control algorithms.

![Kuka youBot simulation](/img/kuka_youBot.png)
*A frame of the simulation of youBot moving a cube from its initial position to final position.*

## Mathematical Framework

Unknown ETA. In the mean time visit the [capstone website](https://hades.mech.northwestern.edu/index.php/Mobile_Manipulation_Capstone) for more mathematical details behind the project. Since this was a Capstone project of the Coursera project, the linked page was the main resource consulted.

## Links

- [GitHub Repository](https://github.com/varadVaidya/Capstone2.0)
- [Video Demo](https://www.youtube.com/watch?v=4ChucdYt1sA)
