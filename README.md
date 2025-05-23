# TurtleBot3 Gazebo Fortress Simulation

ROS 2 package for simulating TurtleBot3 in Gazebo Fortress with Ignition Bridge.

## Prerequisites

### System Requirements
- **Ubuntu 22.04** (Recommended)
- **ROS 2 Humble** (Installed and sourced)
- **Gazebo Fortress** (Ignition Gazebo)

### Dependencies Installation

1. Install ROS 2 dependencies:
   ```bash
   sudo apt update
   sudo apt install ros-humble-desktop ros-humble-gazebo-ros-pkgs
   ```
2. CLONE THE PACKAGE
   ```bash
   git clone https://github.com/Diwakar-Saini/turtlebot3.git
   ```
3. DOWNLOAD THIS MODELS
   ```       ```
4. Insert the models inside the turtlebot3_gazebo package
5. NOW INSTALL THIS PACKAGE IT WILL WORK AS BRIDGE
   ``` bash
       sudo apt update && sudo apt install -y ros-humble-ros-ign ros-humble-ros-ign-bridge ros-humble-ros-ign-gazebo ros-humble-ros-ign-gazebo-demos ros-humble-ros-ign-image ignition-fortress
   ```
7. NOW BUILD THE PACKAGE
   ``` bash
       colcon bild
   ```

