#include <dbus/dbus.h>
#include <iostream>
#include <string>

class MediaPlayer {
public:
    MediaPlayer(const std::string& bus_name, const std::string& object_path)
        : bus_name(bus_name), object_path(object_path) {}

    void sendCommand(const std::string& command) {
        DBusError err;
        DBusConnection* conn;
        DBusMessage* msg;

        dbus_error_init(&err);

        conn = dbus_bus_get(DBUS_BUS_SYSTEM, &err);
        if (dbus_error_is_set(&err)) {
            std::cerr << "Connection Error: " << err.message << std::endl;
            dbus_error_free(&err);
        }
        if (!conn) {
            std::cerr << "Connection Null" << std::endl;
            return;
        }

        msg = dbus_message_new_method_call(
            bus_name.c_str(),
            object_path.c_str(),
            "org.bluez.MediaPlayer1",
            command.c_str()
        );
        if (!msg) {
            std::cerr << "Message Null" << std::endl;
            return;
        }

        dbus_connection_send(conn, msg, nullptr);
        dbus_connection_flush(conn);
        dbus_message_unref(msg);
    }

    void play() {
        sendCommand("Play");
    }

    void pause() {
        sendCommand("Pause");
    }

    void next() {
        sendCommand("Next");
    }

    void previous() {
        sendCommand("Previous");
    }

private:
    std::string bus_name;
    std::string object_path;
};

std::string formatDevicePath(const std::string& mac) {
    std::string path = "/org/bluez/hci0/dev_" + mac;
    for (char& c : path) {
        if (c == ':') {
            c = '_';
        }
    }
    return path + "/player0";
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <command>" << std::endl;
        return 1;
    }

    const std::string device_mac = "F8:71:0C:F3:FE:6A";
    std::string player_path = formatDevicePath(device_mac);

    MediaPlayer player("org.bluez", player_path);

    std::string command(argv[1]);

    if (command == "play") {
        player.play();
    } else if (command == "pause") {
        player.pause();
    } else if (command == "next") {
        player.next();
    } else if (command == "previous") {
        player.previous();
    } else {
        std::cerr << "Unknown command: " << command << std::endl;
        return 1;
    }

    return 0;
}
