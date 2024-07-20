CXX = g++
CXXFLAGS = -std=c++11 -Wall

# DBus C flags
DBUS_INCLUDES = -I/usr/include/dbus-1.0 -I/usr/lib/x86_64-linux-gnu/dbus-1.0/include

# Adjust library linking flags as per your system
LIBS = -ldbus-1

# Target executable
TARGET = btDriver

all: $(TARGET)

$(TARGET): btDriver.cpp
	$(CXX) $(CXXFLAGS) $(DBUS_INCLUDES) -o $(TARGET) btDriver.cpp $(LIBS)

clean:
	rm -f $(TARGET)
