# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mostafa/Desktop/cr_project/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mostafa/Desktop/cr_project/build

# Include any dependencies generated for this target.
include summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/depend.make

# Include the progress variables for this target.
include summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/progress.make

# Include the compile flags for this target's objects.
include summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/flags.make

summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o: summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/flags.make
summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o: /home/mostafa/Desktop/cr_project/src/summit_xl_common/summit_xl_pad/src/summit_xl_pad.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mostafa/Desktop/cr_project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o"
	cd /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o -c /home/mostafa/Desktop/cr_project/src/summit_xl_common/summit_xl_pad/src/summit_xl_pad.cpp

summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.i"
	cd /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mostafa/Desktop/cr_project/src/summit_xl_common/summit_xl_pad/src/summit_xl_pad.cpp > CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.i

summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.s"
	cd /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mostafa/Desktop/cr_project/src/summit_xl_common/summit_xl_pad/src/summit_xl_pad.cpp -o CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.s

# Object files for target summit_xl_pad
summit_xl_pad_OBJECTS = \
"CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o"

# External object files for target summit_xl_pad
summit_xl_pad_EXTERNAL_OBJECTS =

/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/src/summit_xl_pad.cpp.o
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/build.make
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/libdiagnostic_updater.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/libroscpp.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/librosconsole.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/librosconsole_log4cxx.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/librosconsole_backend_interface.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/libxmlrpcpp.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/libroscpp_serialization.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/librostime.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /opt/ros/noetic/lib/libcpp_common.so
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad: summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mostafa/Desktop/cr_project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad"
	cd /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/summit_xl_pad.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/build: /home/mostafa/Desktop/cr_project/devel/lib/summit_xl_pad/summit_xl_pad

.PHONY : summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/build

summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/clean:
	cd /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad && $(CMAKE_COMMAND) -P CMakeFiles/summit_xl_pad.dir/cmake_clean.cmake
.PHONY : summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/clean

summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/depend:
	cd /home/mostafa/Desktop/cr_project/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mostafa/Desktop/cr_project/src /home/mostafa/Desktop/cr_project/src/summit_xl_common/summit_xl_pad /home/mostafa/Desktop/cr_project/build /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad /home/mostafa/Desktop/cr_project/build/summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : summit_xl_common/summit_xl_pad/CMakeFiles/summit_xl_pad.dir/depend
