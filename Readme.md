# Steps: ##

### 1. Build the packages
```
git clone https://github.com/moste00/SLAM-bam.git
cd SLAM-bam
catkin_make
```
### 2. In a new terminal,
```
roslaunch summit_xl_sim_bringup summit_xls_complete.launch
``` 
### This will run gazebo and rviz simulation

### Run each of the following steps in a new terminal, starting with ##
```
cd SLAM-bam
source devel/setup.sh
```
### in each one.

#


### 3. Run the laser readings merger from `ira_laser_tools` package
```
roslaunch ira_laser_tools laserscan_multi_merger.launch
```

### 4. Run the `merge_sensors.py` script from the `robo` package
```
rosrun robo merge_sensors.py
```

### 5. Show the merged `front_laser` and `rear_laser` sensors readings that are merged by `ira_laser_tools` package and published to `scan_multi` node
```
rostopic echo /scan_multi
```

### 6. Show the merged sensor readings that are published to `/all_readings` node
```
rostopic echo /all_readings
```