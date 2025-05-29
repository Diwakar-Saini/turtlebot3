  # 🐢 TurtleBot3 Gazebo Fortress Simulation

ROS 2 package for simulating TurtleBot3 in Gazebo Fortress with Ignition Bridge.
*"Making robot simulation as easy as blinking!"* 😉
## Prerequisites

### System Requirements
- **Ubuntu 22.04** (Recommended)
- **ROS 2 Humble** (Installed and sourced)
- **Gazebo Fortress** (Ignition Gazebo)

### Dependencies Installation

1. Install ROS 2 dependencies:
   ```bash
   sudo apt update
   sudo apt install ros-humble-desktop 
   ```
2. CLONE THE PACKAGE
   ```bash
   git clone https://github.com/Diwakar-Saini/turtlebot3.git
   ```
3. Download this model folder [model](https://drive.google.com/file/d/1jzBQDj69v0LL9O5XnWncsXz-BuB_d52D/view?usp=sharing)  
4. Insert the extracted models  inside the turtlebot3_gazebo package
   Ensure models are in turtlebot3_gazebo/models/
  #### 📂 Package Structure
   ```bash
          >turtlebot3_gazebo/
          ├── launch/          # Launch configurations
          ├── worlds/          # Simulation environments
          ├── models/          # 3D assets and models
          ├── rviz/            # Visualization configs
          └── config/          # Parameter files
   ```
6. Now please install ros-ign bridge:
   ``` bash
       sudo apt update && sudo apt install -y ros-humble-ros-ign ros-humble-ros-ign-bridge ros-humble-ros-ign-gazebo ros-humble-ros-ign-gazebo-demos ros-humble-ros-ign-image ignition-fortress
   ```
7. Now all setup is done we can build the package now:
   ``` bash
       sudo apt-get install ros-${ROS_DISTRO}-dynamixel-sdk
       rosdep install --from-paths src --ignore-src -r -y
       cd turtlebot3
       colcon build
   ```

{ if u get error like couldn't find turtlebot3_msgs: pls proceed with this commands}
``` bash
        cd turtlebot3
        sudo apt-get install ros-${ROS_DISTRO}-turtlebot3-msgs
        source /opt/ros/${ROS_DISTRO}/setup.bash
        rosdep install --from-paths src --ignore-src -y
        rm -rf build install log
        colcon build
```
    
8. Now we will look it is it really running on our system or not :)
   ```BASH
      source install/setup.bash
      export TURTLEBOT3_MODEL=burger
      ros2 launch turtlebot3_gazebo empty_world.launch.py     
   ```
 
9. for teleop use this cmd
    ```bash
       ros2 run turtlebot3_teleop teleop_keyboard --ros-args --remap /cmd_vel:=/cmd_vel_unstamped
    ```
 {SEE GUYS YOU MAY HAVE A PROBLEM WHILE PUBLISHING TO /cmd_vel INSTEAD OF THAT, PUBLISH ON  /cmd_vel_unstamped }   
 ###  🚨 for any problem you can contact us on whatsapp group 
 ### 🛠️🤖 ENJOY BUILDING and make sure to click on star so you can find it easily 😅
    


