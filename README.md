# Checkpoint 18: Mobile Robot Path Planning
---

This package implement a custom path planning algorithm based on Dijkstra's algorithm.

## Instalation
---

### prerequisites

 - ROS2 Galactic or higher      
 - Neobotix simulated robot     

### Install

 1- Clone the repository inside your workspace:  
`git clone https://github.com/maxime-cognie/path_planning_chec-kpoint.git`  

 2- Build and setup the environment:
Navigate to the root of your workspace, then use the following command:  
```bash
colcon build
source install/setup.bash
```

## Test the pathplanner
---

To test the planner:    
1. Launch the simulation    

2. Launch Rviz + Nav2:      
`ros2 launch neo_nav2 neo_nav2_full.launch.xml`     

or if you want to visualize the output from the planner,    
launch rviz and the Nav2 nodes in different terminal as Rviz output is really verbose   

 - Rviz     
 `ros2 launch neo_nav2 neo_nav2_rviz.launch.xml`     
 - Nav2     
 `ros2 launch neo_nav2neo_nav2_full_no_rviz.launch.xml`     