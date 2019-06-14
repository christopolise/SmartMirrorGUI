import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GdkPixbuf


black = Gdk.Color(255, 255, 255)

helpimg = "./src/apps/help.svg"
homeimg = "./src/apps/home.svg"
infoimg = "./src/apps/info.svg"
messagesimg = "./src/apps/messages.svg"
quoteimg = "./src/apps/quote.svg"
timeimg = "./src/apps/time.svg"
calendarimg = "./src/apps/calendar.svg"

helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 250, True)
homepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(homeimg, -1, 128, True)
infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 250, True)
messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 250, True)
quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 250, True)
timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 250, True)
calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 250, True)

home_helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 128, True)
home_infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 128, True)
home_messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 128, True)
home_quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 128, True)
home_timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 128, True)
home_calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 128, True)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Magic Mirror")

        self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.BLANK_CURSOR))
        self.state_list = ["HOME", "WEATHER", "TIME", "MESSAGES", "QUOTE", "CALENDAR", "HELP", "INFO", "MIRROR"]

        self.HOME = Gtk.Revealer()
        self.WEATHER = Gtk.Revealer()
        self.TIME = Gtk.Revealer()
        self.MESSAGES = Gtk.Revealer()
        self.QUOTE = Gtk.Revealer()
        self.CALENDAR = Gtk.Revealer()
        self.HELP = Gtk.Revealer()
        self.INFO = Gtk.Revealer()
        self.MIRROR = Gtk.Revealer()

        self.state = self.state_list[0]
        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, black)
        self.set_default_size(500, 500)

        self.grid = Gtk.Grid()
        self.picbox = Gtk.Box()
        self.textbox = Gtk.Box()

        self.image = Gtk.Image()
        self.image.set_from_pixbuf(homepix)

        self.label = Gtk.Label()

        fontdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        self.label.override_font(fontdesc)
        self.label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # self.label.foreground_color(labelcolor)

        self.picbox.add(self.image)
        self.textbox.add(self.label)

        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        # self.add(self.grid)
        self.HOME.set_reveal_child(False)
        self.HOME.set_transition_type(Gtk.RevealerTransitionType.CROSSFADE)
        self.HOME.add(self.grid)
        self.add(self.HOME)
        self.HOME.set_reveal_child(not self.HOME.get_reveal_child())
        self.go_home()

    def do_key_press_event(self, event):
        Gtk.Window.do_key_press_event(self, event)
        if event.keyval == Gdk.KEY_Escape:
            self.unfullscreen()
            self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
        elif event.keyval == Gdk.KEY_F11:
            self.fullscreen()
        elif event.keyval == Gdk.KEY_h and self.state is not self.state_list[0]:
            # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
            self.go_home()
        elif event.keyval == Gdk.KEY_w and self.state is not self.state_list[1]:
            self.get_weather()
        elif event.keyval == Gdk.KEY_t and self.state is not self.state_list[2]:
            self.get_time_date()
        elif event.keyval == Gdk.KEY_m and self.state is not self.state_list[3]:
            self.show_messages()
        elif event.keyval == Gdk.KEY_q and self.state is not self.state_list[4]:
            self.show_quote()
        elif event.keyval == Gdk.KEY_c and self.state is not self.state_list[5]:
            self.show_calendar()
        elif event.keyval == Gdk.KEY_F1 and self.state is not self.state_list[6]:
            self.show_help()
        elif event.keyval == Gdk.KEY_i and self.state is not self.state_list[7]:
            self.show_info()
        elif event.keyval == Gdk.KEY_n and self.state is not self.state_list[8]:
            self.show_mirror()
        elif event.keyval == Gdk.KEY_Left:
            if self.state_list.index(self.state) != 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) - 1]
                if self.state is "WEATHER":
                    self.get_weather()
                elif self.state is "TIME":
                    self.get_time_date()
                elif self.state is "MESSAGES":
                    self.show_messages()
                elif self.state is "QUOTE":
                    self.show_quote()
                elif self.state is "CALENDAR":
                    self.show_calendar()
                elif self.state is "HELP":
                    self.show_help()
                elif self.state is "INFO":
                    self.show_info()
                elif self.state == "MIRROR":
                    self.show_mirror()
            elif self.state_list.index(self.state) == 1:
                self.state = self.state_list[len(self.state_list) - 1]
                self.show_mirror()
        elif event.keyval == Gdk.KEY_Right:
            if self.state_list.index(self.state) != len(self.state_list) - 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) + 1]
                if self.state == "WEATHER":
                    self.get_weather()
                elif self.state is "TIME":
                    self.get_time_date()
                elif self.state is "MESSAGES":
                    self.show_messages()
                elif self.state is "QUOTE":
                    self.show_quote()
                elif self.state is "CALENDAR":
                    self.show_calendar()
                elif self.state is "HELP":
                    self.show_help()
                elif self.state is "INFO":
                    self.show_info()
                elif self.state is "MIRROR":
                    self.show_mirror()
            elif self.state_list.index(self.state) == len(self.state_list) - 1:
                self.state = self.state_list[1]
                self.get_weather()
        # elif event.keyval == Gdk.KEY_x:
        #     self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW)) and exit(0)
        #     self.quit()
        #     exit(0)
        return False

    def go_home(self):
        self.state = self.state_list[0]
        # self.HOME.set_reveal_child(True)
        # self.HOME.set_transition_type(Gtk.RevealerTransitionType.CROSSFADE)
        # self.HOME.add(self.grid)
        # self.add(self.HOME)
        self.label.set_text("HOME")
        self.image.set_from_pixbuf(homepix)
        print("HOME PANEL")

    def get_weather(self):
        self.state = self.state_list[1]
        self.destroy_children()
        self.label.set_text("WEATHER")
        self.image.set_from_pixbuf(homepix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("GET WEATHER")

    def get_time_date(self):
        self.state = self.state_list[2]
        self.destroy_children()
        self.label.set_text("TIME AND DATE")
        self.image.set_from_pixbuf(timepix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("TIME AND DATE")

    def show_messages(self):
        self.state = self.state_list[3]
        self.destroy_children()
        self.label.set_text("MESSAGES")
        self.image.set_from_pixbuf(messagespix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("GET MESSAGES")

    def show_quote(self):
        self.state = self.state_list[4]
        self.destroy_children()
        self.label.set_text("QUOTE")
        self.image.set_from_pixbuf(quotepix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("GET QUOTE")

    def show_help(self):
        self.state = self.state_list[6]
        self.destroy_children()
        self.label.set_text("HELP")
        self.image.set_from_pixbuf(helppix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("HELP")

    def show_info(self):
        self.state = self.state_list[7]
        self.destroy_children()
        self.label.set_text("INFO")
        self.image.set_from_pixbuf(infopix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print("INFO")

    def show_mirror(self):
        self.state = self.state_list[8]
        self.destroy_children()

    def show_calendar(self):
        self.state = self.state_list[5]
        self.destroy_children()
        self.label.set_text("CALENDAR")
        self.image.set_from_pixbuf(calendarpix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)

    def destroy_children(self):
        for item in self.grid:
            self.grid.remove(item)

    # def quit(self):
    #     # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.WATCH))
    #     Gtk.main_quit
    #     # exit(0)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
