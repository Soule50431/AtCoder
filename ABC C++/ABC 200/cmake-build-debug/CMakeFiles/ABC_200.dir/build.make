# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2021.1.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2021.1.1\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "D:\Documents\AtCoder\ABC C++\ABC 200"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/ABC_200.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/ABC_200.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ABC_200.dir/flags.make

CMakeFiles/ABC_200.dir/main.cpp.obj: CMakeFiles/ABC_200.dir/flags.make
CMakeFiles/ABC_200.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ABC_200.dir/main.cpp.obj"
	D:\Downloads\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\ABC_200.dir\main.cpp.obj -c "D:\Documents\AtCoder\ABC C++\ABC 200\main.cpp"

CMakeFiles/ABC_200.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ABC_200.dir/main.cpp.i"
	D:\Downloads\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "D:\Documents\AtCoder\ABC C++\ABC 200\main.cpp" > CMakeFiles\ABC_200.dir\main.cpp.i

CMakeFiles/ABC_200.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ABC_200.dir/main.cpp.s"
	D:\Downloads\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "D:\Documents\AtCoder\ABC C++\ABC 200\main.cpp" -o CMakeFiles\ABC_200.dir\main.cpp.s

# Object files for target ABC_200
ABC_200_OBJECTS = \
"CMakeFiles/ABC_200.dir/main.cpp.obj"

# External object files for target ABC_200
ABC_200_EXTERNAL_OBJECTS =

ABC_200.exe: CMakeFiles/ABC_200.dir/main.cpp.obj
ABC_200.exe: CMakeFiles/ABC_200.dir/build.make
ABC_200.exe: CMakeFiles/ABC_200.dir/linklibs.rsp
ABC_200.exe: CMakeFiles/ABC_200.dir/objects1.rsp
ABC_200.exe: CMakeFiles/ABC_200.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ABC_200.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\ABC_200.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ABC_200.dir/build: ABC_200.exe

.PHONY : CMakeFiles/ABC_200.dir/build

CMakeFiles/ABC_200.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\ABC_200.dir\cmake_clean.cmake
.PHONY : CMakeFiles/ABC_200.dir/clean

CMakeFiles/ABC_200.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "D:\Documents\AtCoder\ABC C++\ABC 200" "D:\Documents\AtCoder\ABC C++\ABC 200" "D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug" "D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug" "D:\Documents\AtCoder\ABC C++\ABC 200\cmake-build-debug\CMakeFiles\ABC_200.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/ABC_200.dir/depend

