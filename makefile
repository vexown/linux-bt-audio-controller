CXX = g++
CXXFLAGS = -std=c++11 -Wall

# Adjust include paths for ARM architecture
DBUS_CXX_INCLUDES = -I/usr/lib/aarch64-linux-gnu/dbus-1.0/include -I/usr/include/dbus-1.0

# Adjust library linking flags for ARM architecture
LIBS = -L/usr/lib/aarch64-linux-gnu -ldbus-1

# Target executable
TARGET = btDriver

all: $(TARGET)

$(TARGET): btDriver.cpp
	$(CXX) $(CXXFLAGS) $(DBUS_CXX_INCLUDES) -o $(TARGET) btDriver.cpp $(LIBS)

clean:
	rm -f $(TARGET)

