from gi import require_version

require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GdkPixbuf, GObject
from datetime import datetime
from mqtt_subscriber import UpdateInfo
from time import sleep

ENABLE_TIMER = True
CUR_KEY = None
black = Gdk.Color(255, 255, 255)

# System Icons
icon = "./src/icon.png"
helpimg = "./src/apps/help.svg"
homeimg = "./src/apps/home.svg"
infoimg = "./src/apps/info.svg"
messagesimg = "./src/apps/messages.svg"
quoteimg = "./src/apps/quote.svg"
timeimg = "./src/apps/time.svg"
calendarimg = "./src/apps/calendar.svg"
logoimg = "./src/BYU.svg"

# Weather Icons
severe_img = "./src/weather/alert-severe.svg"
broken_clouds_img = "./src/weather/broken-clouds.svg"
clear_day_img = "./src/weather/clear-day.svg"
clear_night_img = "./src/weather/clear-night.svg"
clouds_day_img = "./src/weather/clouds-day.svg"
clouds_night_img = "./src/weather/clouds-night.svg"
mist_img = "./src/weather/mist.svg"
rain_img = "./src/weather/rain.svg"
showers_img = "./src/weather/showers.svg"
snow_img = "./src/weather/snow.svg"
thunderstorm_img = "./src/weather/thunderstorm.svg"

# System Images
iconpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(icon, -1, 250, True)
helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 250, True)
homepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(homeimg, -1, 128, True)
infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 250, True)
messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 250, True)
quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 250, True)
timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 250, True)
calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 250, True)
logopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(logoimg, -1, 425, True)

# Weather Images
severepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(severe_img, -1, 250, True)
brokencloudspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(broken_clouds_img, -1, 250, True)
cleardaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 250, True)
clearnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 250, True)
cloudsdaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_day_img, -1, 250, True)
cloudsnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_night_img, -1, 250, True)
mistpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(mist_img, -1, 250, True)
rainpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(rain_img, -1, 250, True)
showerspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(showers_img, -1, 250, True)
snowpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(snow_img, -1, 250, True)
thunderstormpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(thunderstorm_img, -1, 250, True)
sunrisepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 50, True)
sunsetpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 50, True)

home_helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 128, True)
home_infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 128, True)
home_messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 128, True)
home_quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 128, True)
home_timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 128, True)
home_calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 128, True)


class Loading(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(logopix)

        title = Gtk.Label()
        title.set_text("BYU's Magic Mirror")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 100")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        self.add(center)


class Home(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

    pass


class Weather(Gtk.Layout):
    __gtype_name__ = 'Weather'

    def __init__(self, temp, cond, sunrise, sunset, cloudiness, wind, humidity, image):
        Gtk.Layout.__init__(self)
        self.set_border_width(20)

        self.temperature = temp
        self.condition = cond
        self.sunrise = sunrise
        self.sunset = sunset
        self.cloudiness = cloudiness
        self.wind = wind
        self.humidity = humidity
        self.image = image

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        sunbox = Gtk.HBox()
        cloudbox = Gtk.HBox()

        status_image = Gtk.Image()
        status_image.set_from_pixbuf(self.image)

        sunrise_image = Gtk.Image()
        sunset_image = Gtk.Image()
        sunrise_image.set_from_pixbuf(sunrisepix)
        sunset_image.set_from_pixbuf(sunsetpix)

        temperature = Gtk.Label()
        condition = Gtk.Label()
        sunrise = Gtk.Label()
        sunset = Gtk.Label()
        cloudiness = Gtk.Label()
        wind = Gtk.Label()
        humidity = Gtk.Label()

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 150")
        temperature.override_font(tempdesc)
        temperature.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        conditiondesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        condition.override_font(conditiondesc)
        condition.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        labeldesc = Pango.FontDescription("AnjaliOldLipi Bold 23")

        sunrise.override_font(labeldesc)
        sunrise.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        sunset.override_font(labeldesc)
        sunset.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        cloudiness.override_font(labeldesc)
        cloudiness.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        wind.override_font(labeldesc)
        wind.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        humidity.override_font(labeldesc)
        humidity.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        temperature.set_text(self.temperature)
        condition.set_text(self.condition)
        sunrise.set_text(self.sunrise)
        sunset.set_text(self.sunset)
        cloudiness.set_text("Cloudiness: " + self.cloudiness + '%')
        wind.set_text("Wind Speed: " + self.wind + ' mph')
        humidity.set_text("Humidity: " + self.humidity + '%')

        sunbox.pack_start(sunrise_image, True, False, 0)
        sunbox.pack_start(sunrise, True, True, 0)
        sunbox.pack_start(sunset_image, True, True, 0)
        sunbox.pack_start(sunset, True, True, 0)
        sunbox.pack_start(humidity, True, True, 0)

        cloudbox.pack_start(cloudiness, True, False, 0)
        cloudbox.pack_start(wind, True, False, 0)

        center.pack_start(status_image, True, False, 0)
        center.pack_start(temperature, True, False, 0)
        center.pack_start(condition, True, False, 0)
        center.pack_start(cloudbox, True, False, 0)
        center.pack_start(sunbox, True, False, 0)
        self.put(center, ((Gdk.Screen.width() / 2) - 325), 100)


class TimeDate(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

    pass


class Messages(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(messagespix)

        title = Gtk.Label()
        title.set_text("Messages")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        self.add(center)


class Quote(Gtk.VBox):
    def __init__(self, text, author):
        Gtk.VBox.__init__(self)

        self.text = text
        self.author = author

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(quotepix)

        text = Gtk.Label()
        author = Gtk.Label()
        # text.set_label(self.text)
        text.set_label(self.text)
        author.set_text("~ " + self.author + " ~")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        text.override_font(tempdesc)
        text.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        text.set_line_wrap(True)
        # text.set_justify(Gtk.Justification.CENTER)

        authordesc = Pango.FontDescription("AnjaliOldLipi Bold Italic 20")
        author.override_font(authordesc)
        author.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # author.set_line_wrap(True)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(text, True, False, 0)
        center.pack_start(author, True, False, 0)
        self.add(center)


class Help(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(helppix)

        title = Gtk.Label()
        description = Gtk.Label()
        helptext = Gtk.Label()

        title.set_text("Help")
        description.set_text("BYU's Magic Mirror is an IoT project that depends on the following processes located at "
                             "immerse-iot.byu.edu:\n"
                             "- Quote API [client_location] which refreshes every 10m or upon request\n"
                             "- Message API [client_location] which refreshes every time a message is sent or upon "
                             "request\n"
                             "- Weather API [client_location] which refreshes every 10m or upon request\n"
                             "- Calendar API [client_location] which refreshes every day or upon request\n"
                             "all pushing messages via MQTT publishers and clients to postman.cloudmqtt.com\n")
        helptext.set_text("[h]\t or <equivalent gesture> returns user to Home Screen\n"
                          "[t]\t or <equivalent gesture> shows user time and date\n"
                          "[q]\t or <equivalent gesture> shows a random quote\n"
                          "[m]\t or <equivalent gesture> shows the message queue\n"
                          "[w]\t or <equivalent gesture> shows the weather\n"
                          "[c]\t or <equivalent gesture> shows the calendar events\n"
                          "[F1]\t or <equivalent gesture> shows this help screen\n"
                          "[i]\t or <equivalent gesture> shows the About screen\n"
                          "[m]\t or <equivalent gesture> shows a blank screen for mirror purposes\n"
                          "[Left]\t or <equivalent gesture> cycles through app screens forwards\n"
                          "[Right]\t or <equivalent gesture> cycle through app screens backwards\n"
                          " \n"
                          "For any other technical/development aspect of this project, please refer to the wiki at "
                          "[wiki location]\n")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        descriptdesc = Pango.FontDescription("Ubuntu Mono Italic 20")
        description.override_font(descriptdesc)
        description.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        description.set_line_wrap(True)

        helpdesc = Pango.FontDescription("Ubuntu Mono 20")
        helptext.override_font(helpdesc)
        helptext.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # help.set_line_wrap(True)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(description, True, False, 0)
        center.pack_start(helptext, True, False, 0)
        self.add(center)


class Info(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(infopix)

        title = Gtk.Label()
        description = Gtk.Label()
        creators = Gtk.Label()
        maintainers = Gtk.Label()

        title.set_text("About")
        description.set_text("BYU's Magic Mirror is a project designed to showcase different IoT principles via \n"
                             "mirror apps and possible exterior applications all controlled by this unit.")
        creators.set_text("Written by:\n"
                          "Philip Lundrigan\t\t Mentoring Professor and project architect\n"
                          "Christopher Kitras\t\t Display module and graphical user interface design\n"
                          "Joseph ___\t\t\t Input module\n"
                          "Levi Fleming\t\t\t Calendar and Messenger APIs and hardware design\n"
                          "Max ___\t\t\t\t Quote API and hardware design\n"
                          "Michael Bjerregaard\t\t Weather API and hardware design")
        maintainers.set_text("Maintained by:\n"
                             "[2019-Present] Creators")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        descriptdesc = Pango.FontDescription("AnjaliOldLipi Bold Italic 30")
        description.override_font(descriptdesc)
        description.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        creatorsdesc = Pango.FontDescription("AnjaliOldLipi Mono 30")
        creators.override_font(creatorsdesc)
        creators.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        maintainersdesc = Pango.FontDescription("AnjaliOldLipi Mono 30")
        maintainers.override_font(maintainersdesc)
        maintainers.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(description, True, False, 0)
        center.pack_start(creators, True, False, 0)
        center.pack_start(maintainers, True, False, 0)
        self.add(center)


class Calendar(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(calendarpix)

        title = Gtk.Label()
        title.set_text("Calendar")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        self.add(center)


class Mirror(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Magic Mirror")

        self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.BLANK_CURSOR))
        self.state_list = ["HOME", "WEATHER", "TIME", "MESSAGES", "QUOTE", "CALENDAR", "HELP", "INFO", "MIRROR"]
        self.info = UpdateInfo()

        loading = Loading()
        print("window Size: ", Gdk.Screen.width())
        if self.info.weather_temp is "":
            print("NULL")
        # print(self.info.weather_temp)
        self.add(loading)
        # while self.info.weather_temp is "" or self.info.weather_cond is "" or self.info.weather_sunrise is "" or\
        #         self.info.weather_sunset is "" or self.info.weather_cloudiness is "" or self.info.weather_wind is "" or\
        #         self.info.weather_humidity is "":
        #     # print("LOADING WEATHER")
        #     pass

        # while self.info.quote_author is "" or self.info.quote_text is "":
        #     print("LOADING QUOTE")
        #     pass

        # while self.info.event_date_1 is "" or self.info.event_date_2 is "" or self.info.event_date_3 is "" or\
        #         self.info.event_date_4 is "" or self.info.event_location_1 is "" or self.info.event_location_2 is "" or\
        #         self.info.event_location_3 is "" or self.info.event_location_4 is "" or self.info.event_title_1 is "" or\
        #         self.info.event_title_2 is "" or self.info.event_title_3 is "" or self.info.event_title_4 is "":
        #     print("LOADING EVENT CALENDAR")

        # TODO:
        # Quote of the day queue info loading
        self.remove(loading)
        # self.load_weather()
        # self.load_quote()
        # quote = Quote()
        help = Help()
        info = Info()
        calendar = Calendar()
        messages = Messages()
        mirror = Mirror()
        # self.remove(loading)
        # self.add(loading)
        # self.add(mirror)
        # self.add(quote)
        # self.add(help)
        self.add(info)
        # self.add(calendar)
        # self.add(messages)

        # self.HOME = Gtk.Revealer()
        # self.WEATHER = Gtk.Revealer()
        # self.TIME = Gtk.Revealer()
        # self.MESSAGES = Gtk.Revealer()
        # self.QUOTE = Gtk.Revealer()
        # self.CALENDAR = Gtk.Revealer()
        # self.HELP = Gtk.Revealer()
        # self.INFO = Gtk.Revealer()
        # self.MIRROR = Gtk.Revealer()

        # self.state = self.state_list[0]
        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, black)
        self.set_default_size(500, 500)
        self.set_icon(iconpix)

    def load_weather(self):
        condition = self.get_weather_condition()
        image = self.get_weather_logo()
        weather = Weather(self.info.weather_temp + "°F", condition, self.info.weather_sunrise,
                          self.info.weather_sunset, self.info.weather_cloudiness, self.info.weather_wind,
                          self.info.weather_humidity, image)
        self.add(weather)

    def load_quote(self):
        text = self.info.quote_text
        author = self.info.quote_author
        quote = Quote(text, author)
        self.add(quote)

    def do_key_press_event(self, event):
        global ENABLE_TIMER
        global CUR_KEY
        Gtk.Window.do_key_press_event(self, event)
        CUR_KEY = event.keyval
        # print(CUR_KEY)
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
            # global ENABLE_TIMER
            ENABLE_TIMER = True
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
            ENABLE_TIMER = False
            if self.state_list.index(self.state) != 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) - 1]
                if self.state is "WEATHER":
                    self.get_weather()
                elif self.state is "TIME":
                    ENABLE_TIMER = True
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
            ENABLE_TIMER = False
            if self.state_list.index(self.state) != len(self.state_list) - 1:
                self.state = self.state_list[self.state_list.index(str(self.state)) + 1]
                if self.state == "WEATHER":
                    self.get_weather()
                elif self.state is "TIME":
                    ENABLE_TIMER = True
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

    def go_home(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[0]
        # self.HOME.set_reveal_child(True)
        # self.HOME.set_transition_type(Gtk.RevealerTransitionType.CROSSFADE)
        # self.HOME.add(self.grid)
        # self.add(self.HOME)
        self.title.set_text("HOME")
        self.image.set_from_pixbuf(homepix)
        print(self.state)

    def get_weather_condition(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        condition = ""

        if self.info.weather_cond == "Clouds":
            if 11 <= int(self.info.weather_cloudiness) < 25:
                condition = "Few Clouds"
            elif 25 <= int(self.info.weather_cloudiness) <= 50:
                condition = "Sparse Clouds"
            elif 51 <= int(self.info.weather_cloudiness) <= 84:
                condition = "Broken Clouds"
            elif 85 <= int(self.info.weather_cloudiness) <= 100:
                condition = "Overcast Clouds"
        elif self.info.weather_cond == "Clear":
            condition = "Sky is Clear"
        elif self.info.weather_cond == "Mist":
            condition = "Mist"
        elif self.info.weather_cond == "Smoke":
            condition = "Smoke"
        elif self.info.weather_cond == "Haze":
            condition = "Haze"
        elif self.info.weather_cond == "Dust":
            condition = "DUST"
        elif self.info.weather_cond == "Fog":
            condition = "Fog"
        elif self.info.weather_cond == "Sand":
            condition = "Sand"
        elif self.info.weather_cond == "Ash":
            condition = "Volcanic Ash"
        elif self.info.weather_cond == "Squall":
            condition = "Squalls"
        elif self.info.weather_cond == "Tornado":
            condition = "Tornado"
        elif self.info.weather_cond == "Snow":
            condition = "SNOW"
        elif self.info.weather_cond == "Rain":
            condition = "RAIN"
        elif self.info.weather_cond == "Drizzle":
            condition = "DRIZZLE"
        elif self.info.weather_cond == "Thunderstorm":
            condition = "THUNDERSTORM"
        return condition

    def get_weather_logo(self):
        print(self.info.weather_cond)
        image = logopix
        if self.info.weather_cond == "Clouds":
            if 11 <= int(self.info.weather_cloudiness) < 25:
                if self.info.weather_time_of_day == "day":
                    image = cloudsdaypix
                else:
                    image = cloudsnightpix
            elif 25 <= int(self.info.weather_cloudiness) <= 50:
                if self.info.weather_time_of_day == "day":
                    image = cloudsdaypix
                else:
                    image = cloudsnightpix
            elif 51 <= int(self.info.weather_cloudiness) <= 84:
                image = brokencloudspix
            elif 85 <= int(self.info.weather_cloudiness) <= 100:
                image = brokencloudspix
        elif self.info.weather_cond == "Clear":
            if self.info.weather_time_of_day == "day":
                print("THIS HAPPENED")
                image = cleardaypix
            else:
                image = clearnightpix
        elif self.info.weather_cond == "Mist":
            image = mistpix
        elif self.info.weather_cond == "Smoke":
            image = mistpix
        elif self.info.weather_cond == "Haze":
            image = mistpix
        elif self.info.weather_cond == "Dust":
            image = mistpix
        elif self.info.weather_cond == "Fog":
            image = mistpix
        elif self.info.weather_cond == "Sand":
            image = mistpix
        elif self.info.weather_cond == "Ash":
            image = mistpix
        elif self.info.weather_cond == "Squall":
            image = mistpix
        elif self.info.weather_cond == "Tornado":
            image = mistpix
        elif self.info.weather_cond == "Snow":
            image = snowpix
        elif self.info.weather_cond == "Rain":
            image = rainpix
        elif self.info.weather_cond == "Drizzle":
            image = showerspix
        elif self.info.weather_cond == "Thunderstorm":
            image = thunderstormpix

        return image

    def get_time_date(self):
        global ENABLE_TIMER
        print("ENTERING TIMER")
        # ENABLE_TIMER = True
        # if ENABLE_TIMER:
        self.state = self.state_list[2]
        self.destroy_children()
        fontdesc = Pango.FontDescription("AnjaliOldLipi Bold 150")
        self.title.override_font(fontdesc)
        time = str(datetime.now().strftime("%-I:%M:%S %p "))
        self.title.set_label(time)
        self.image.set_from_pixbuf(timepix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        self.start_clock_timer()
        print(self.state)

    def show_messages(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[3]
        self.destroy_children()
        self.title.set_text("MESSAGES")
        self.image.set_from_pixbuf(messagespix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(self.state)

    def show_quote(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[4]
        self.destroy_children()
        self.title.set_text("QUOTE")
        self.image.set_from_pixbuf(quotepix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(self.state)

    def show_help(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[6]
        self.destroy_children()
        self.title.set_text("HELP")
        self.image.set_from_pixbuf(helppix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(self.state)

    def show_info(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[7]
        self.destroy_children()
        self.title.set_text("INFO")
        self.image.set_from_pixbuf(infopix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(self.state)

    def show_mirror(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[8]
        self.destroy_children()
        print(self.state)

    def show_calendar(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        self.state = self.state_list[5]
        self.destroy_children()
        self.title.set_text("CALENDAR")
        self.image.set_from_pixbuf(calendarpix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(self.state)

    def destroy_children(self):
        for item in self.grid:
            self.grid.remove(item)

    def start_clock_timer(self):
        global ENABLE_TIMER
        global CUR_KEY
        if ENABLE_TIMER:
            GObject.timeout_add(1000, self.get_time_date)
        else:
            # print("Previous state: ", self.state)
            if CUR_KEY == Gdk.KEY_h and self.state is not self.state_list[0]:
                self.go_home()
            elif CUR_KEY == Gdk.KEY_w and self.state is not self.state_list[1]:
                self.get_weather()
            elif CUR_KEY == Gdk.KEY_t and self.state is not self.state_list[2]:
                ENABLE_TIMER = True
                self.get_time_date()
            elif CUR_KEY == Gdk.KEY_m and self.state is not self.state_list[3]:
                self.show_messages()
            elif CUR_KEY == Gdk.KEY_q and self.state is not self.state_list[4]:
                self.show_quote()
            elif CUR_KEY == Gdk.KEY_c and self.state is not self.state_list[5]:
                self.show_calendar()
            elif CUR_KEY == Gdk.KEY_F1 and self.state is not self.state_list[6]:
                self.show_help()
            elif CUR_KEY == Gdk.KEY_i and self.state is not self.state_list[7]:
                self.show_info()
            elif CUR_KEY == Gdk.KEY_n and self.state is not self.state_list[8]:
                self.show_mirror()
            elif CUR_KEY == Gdk.KEY_Left:
                ENABLE_TIMER = False
                self.get_weather()
            elif CUR_KEY == Gdk.KEY_Right:
                ENABLE_TIMER = False
                self.show_messages()


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
