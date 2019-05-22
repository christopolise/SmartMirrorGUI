import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GdkPixbuf

black = Gdk.Color(255, 255, 255)

helpimg = "./src/help.svg"
homeimg = "./src/home.svg"
infoimg = "./src/info.svg"
messagesimg = "./src/messages.svg"
quoteimg = "./src/quote.svg"
timeimg = "./src/time.svg"

helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 128, True)
homepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(homeimg, 128, 128, True)
infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 128, True)
messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 128, True)
quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 128, True)
timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 128, True)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Banana")
        self.state = "HOME"
        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, black)
        self.set_default_size(500, 500)

        self.grid = Gtk.Grid()
        self.picbox = Gtk.Box()
        self.textbox = Gtk.Box()

        self.image = Gtk.Image()
        self.image.set_from_pixbuf(homepix)
        self.label = Gtk.Label()
        self.picbox.add(self.image)
        self.textbox.add(self.label)

        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        self.add(self.grid)

        self.go_home()

    def do_key_press_event(self, event):
        Gtk.Window.do_key_press_event(self, event)
        if event.keyval == Gdk.KEY_Escape:
            self.unfullscreen()
        elif event.keyval == Gdk.KEY_F11:
            self.fullscreen()
        elif event.keyval == Gdk.KEY_h and self.state is not "HOME":
            self.go_home()
        elif event.keyval == Gdk.KEY_w and self.state is not "WEATHER":
            self.get_weather()
        elif event.keyval == Gdk.KEY_t and self.state is not "TIME":
            self.get_time_date()
        elif event.keyval == Gdk.KEY_m and self.state is not "MESSAGES":
            self.show_messages()
        elif event.keyval == Gdk.KEY_q and self.state is not "QUOTE":
            self.show_quote()
        elif event.keyval == Gdk.KEY_F1 and self.state is not "HELP":
            self.show_help()
        elif event.keyval == Gdk.KEY_i and self.state is not "INFO":
            self.show_info()
        elif event.keyval == Gdk.KEY_x:
            exit(0)
        return False

    def go_home(self):
        self.state = "HOME"
        # self.grid = Gtk.Grid()
        # self.picbox = Gtk.Box()
        # self.textbox = Gtk.Box()
        self.label.set_text("HOME")
        self.image.set_from_pixbuf(homepix)
        # self.picbox.add(self.image)
        # self.textbox.add(self.label)
        # self.grid.add(self.picbox)
        # self.grid.attach_next_to(self.textbox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        self.add(self.grid)

        print("HOME PANEL")

    def get_weather(self):
        self.state = "WEATHER"
        self.destroy_children()
        self.label.set_text("WEATHER")
        self.image.set_from_pixbuf(homepix)
        print("GET WEATHER")

    def get_time_date(self):
        self.state = "TIME"
        self.destroy_children()
        self.label.set_text("TIME AND DATE")
        self.image.set_from_pixbuf(timepix)
        print("TIME AND DATE")

    def show_messages(self):
        self.state = "MESSAGES"
        self.destroy_children()
        self.label.set_text("MESSAGES")
        self.image.set_from_pixbuf(messagespix)
        print("GET MESSAGES")

    def show_quote(self):
        self.state = "QUOTE"
        self.destroy_children()
        self.label.set_text("QUOTE")
        self.image.set_from_pixbuf(quotepix)
        print("GET QUOTE")

    def show_help(self):
        self.state = "HELP"
        self.destroy_children()
        self.label.set_text("HELP")
        self.image.set_from_pixbuf(helppix)
        print("HELP")

    def show_info(self):
        self.state = "INFO"
        self.destroy_children()
        self.label.set_text("INFO")
        self.image.set_from_pixbuf(infopix)
        print("INFO")

    def destroy_children(self):
        self.remove(self.grid)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
