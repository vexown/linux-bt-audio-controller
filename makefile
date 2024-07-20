CXX = g++
CXXFLAGS = -std=c++11 -Wall

# Retrieve include flags from pkg-config for dbus-c++-1
DBUS_CXX_INCLUDES = $(shell pkg-config --cflags dbus-c++-1)

# Adjust library linking flags as per your system
LIBS = $(shell pkg-config --libs dbus-c++-1) -ldbus-1

# Target executable
TARGET = btDriver

all: $(TARGET)

$(TARGET): btDriver.cpp
	$(CXX) $(CXXFLAGS) $(DBUS_CXX_INCLUDES) -o $(TARGET) btDriver.cpp $(LIBS)

clean:
	rm -f $(TARGET)



