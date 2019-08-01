from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GdkPixbuf, GObject

from datetime import datetime
from dateutil import tz
from time import sleep, time
from Calendar import Calendar
from Help import Help
from Home import Home
from Info import Info
from Loading import Loading
from Messages import Messages
from Mirror import Mirror
from Quote import Quote
from TimeDate import TimeDate
from WeatherData import WeatherData, Weather
import threading
import subscriber
import Images as IMG


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Magic Mirror")

        self.state_list = ["HOME", "WEATHER", "TIME", "MESSAGES", "QUOTE", "CALENDAR", "HELP", "INFO", "MIRROR"]

        # Data classes which update from subscriber
        weather_data = WeatherData()

        # Screen objects that are cycled in the window
        # home_screen = Home()
        weather_screen = Weather(weather_data)
        time_screen = TimeDate()
        message_screen = Messages()
        # quote_screen = Quote()
        # calendar_screen = Calendar()
        help_screen = Help()
        info_screen = Info()
        mirror_screen = Mirror()

        # Starts the MQTT subscriber
        data_thread = threading.Thread(target=subscriber.run, args=([weather_data],))
        data_thread.start()

        # Updates the value on the screens in separate threads
        GObject.timeout_add(1000, weather_screen.update_weather)
        GObject.timeout_add(1000, time_screen.update_clock)

        # Meant to add the default screen
        self.add(time_screen)

        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(255, 255, 255))
        self.set_default_size(500, 500)
        self.set_icon(IMG.iconpix)

    def do_key_press_event(self, event):
        Gtk.Window.do_key_press_event(self, event)
        CUR_KEY = event.keyval
        # print(CUR_KEY)
        if event.keyval == Gdk.KEY_Escape:
            self.unfullscreen()
            # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
        elif event.keyval == Gdk.KEY_F11:
            # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.BLANK_CURSOR))
            self.fullscreen()
        # elif event.keyval == Gdk.KEY_h and STATE is not self.state_list[0]:
            # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
            # self.go_home()
        # elif event.keyval == Gdk.KEY_w and STATE is not self.state_list[1]:
            # self.get_weather()
        # elif event.keyval == Gdk.KEY_t and STATE is not self.state_list[2]:
            # global ENABLE_TIMER
            # ENABLE_TIMER = True
            # self.get_time_date()
        # elif event.keyval == Gdk.KEY_m and STATE is not self.state_list[3]:
            # self.show_messages()
        # elif event.keyval == Gdk.KEY_q and STATE is not self.state_list[4]:
            # self.show_quote()
        # elif event.keyval == Gdk.KEY_c and STATE is not self.state_list[5]:
            # self.show_calendar()
        # elif event.keyval == Gdk.KEY_F1 and STATE is not self.state_list[6]:
            # self.show_help()
        # elif event.keyval == Gdk.KEY_i and STATE is not self.state_list[7]:
            # self.show_info()
        # elif event.keyval == Gdk.KEY_n and STATE is not self.state_list[8]:
            # self.show_mirror()
        # elif event.keyval == Gdk.KEY_Left:
            # ENABLE_TIMER = False
            # if self.state_list.index(STATE) != 1:
                # STATE = self.state_list[self.state_list.index(str(STATE)) - 1]
                # if STATE is "WEATHER":
                    # self.get_weather()
                # elif STATE is "TIME":
                    # ENABLE_TIMER = True
                    # self.get_time_date()
                # elif STATE is "MESSAGES":
                    # self.show_messages()
                # elif STATE is "QUOTE":
                    # self.show_quote()
                # elif STATE is "CALENDAR":
                    # self.show_calendar()
                # elif STATE is "HELP":
                    # self.show_help()
                # elif STATE is "INFO":
                    # self.show_info()
                # elif STATE == "MIRROR":
                    # self.show_mirror()
            # elif self.state_list.index(STATE) == 1:
                # STATE = self.state_list[len(self.state_list) - 1]
                # self.show_mirror()
        # elif event.keyval == Gdk.KEY_Right:
            # ENABLE_TIMER = False
            # if self.state_list.index(STATE) != len(self.state_list) - 1:
                # STATE = self.state_list[self.state_list.index(str(STATE)) + 1]
                # if STATE == "WEATHER":
                    # self.get_weather()
                # elif STATE is "TIME":
                    # ENABLE_TIMER = True
                    # self.get_time_date()
                # elif STATE is "MESSAGES":
                    # self.show_messages()
                # elif STATE is "QUOTE":
                    # self.show_quote()
                # elif STATE is "CALENDAR":
                    # self.show_calendar()
                # elif STATE is "HELP":
                    # self.show_help()
                # elif STATE is "INFO":
                    # self.show_info()
                # elif STATE is "MIRROR":
                    # self.show_mirror()
            # elif self.state_list.index(STATE) == len(self.state_list) - 1:
                # STATE = self.state_list[1]
                # self.get_weather()
        # elif (event.keyval == Gdk.KEY_Up) and (STATE is "CALENDAR"):
            # print("derpaflerp")


def main():
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    cursor = Gdk.Cursor.new(Gdk.CursorType.BLANK_CURSOR)
    window.get_window().set_cursor(cursor)
    Gtk.main()


if __name__ == '__main__':
    main()
