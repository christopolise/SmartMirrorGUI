from gi import require_version

require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GdkPixbuf, GObject
from datetime import datetime
from mqtt_subscriber import UpdateInfo
from time import sleep

ENABLE_TIMER = True
CUR_KEY = None
STATE = ""
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

# Directions
up_img = "./src/direction/up.svg"
down_img = "./src/direction/down.svg"

# Home Status Bar
message = "./src/homescreen/message.svg"

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

# Navegator Bar
home_helppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(helpimg, -1, 128, True)
home_infopix = GdkPixbuf.Pixbuf.new_from_file_at_scale(infoimg, -1, 128, True)
home_messagespix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 128, True)
home_quotepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(quoteimg, -1, 128, True)
home_timepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(timeimg, -1, 128, True)
home_calendarpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(calendarimg, -1, 128, True)

# Direction arrows
uppix = GdkPixbuf.Pixbuf.new_from_file_at_scale(up_img, -1, 50, True)
downpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(down_img, -1, 50, True)

# Home Screen Status Bar
status_message_sing_pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(message, -1, 50, True)
status_message_plu_pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(messagesimg, -1, 50, True)
status_severepix = GdkPixbuf.Pixbuf.new_from_file_at_scale(severe_img, -1, 50, True)
status_brokencloudspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(broken_clouds_img, -1, 50, True)
status_cleardaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_day_img, -1, 50, True)
status_clearnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clear_night_img, -1, 50, True)
status_cloudsdaypix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_day_img, -1, 50, True)
status_cloudsnightpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(clouds_night_img, -1, 50, True)
status_mistpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(mist_img, -1, 50, True)
status_rainpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(rain_img, -1, 50, True)
status_showerspix = GdkPixbuf.Pixbuf.new_from_file_at_scale(showers_img, -1, 50, True)
status_snowpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(snow_img, -1, 50, True)
status_thunderstormpix = GdkPixbuf.Pixbuf.new_from_file_at_scale(thunderstorm_img, -1, 50, True)


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


class Home(Gtk.VBox):
    def __init__(self, weather, temp,unread, cal_event):
        Gtk.VBox.__init__(self)

        self.weather = weather
        self.temp = temp
        self.unread = unread
        self.cal_event = cal_event

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        weatherbox = Gtk.HBox()
        messagebox = Gtk.HBox()
        status_bar = Gtk.HBox()

        weather_image = Gtk.Image()
        message_image = Gtk.Image()

        weather_image.set_from_pixbuf(self.weather)
        if int(self.unread) == 1:
            message_image.set_from_pixbuf(status_message_sing_pix)
        elif int(self.unread) > 1:
            message_image.set_from_pixbuf(status_message_plu_pix)

        time = str(datetime.now().strftime("%-I:%M %p "))
        date_str = str(datetime.now().strftime("%A %b %d, %Y"))

        time_label = Gtk.Label()
        date_label = Gtk.Label()
        temp_label = Gtk.Label()
        messages_label = Gtk.Label()
        calendar_label = Gtk.Label()

        time_label.set_text(time)
        date_label.set_text(date_str)
        temp_label.set_text("TEMP")
        messages_label.set_text("1")
        calendar_label.set_text("EVENT")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        time_label.override_font(tempdesc)
        time_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_end(time_label, False, True, 0)
        self.add(center)


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

        temperature.set_text(self.temperature.split('.')[0] + "°F")
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
        # self.add(center)


class TimeDate(Gtk.VBox):
    title = Gtk.Label()
    date_text = Gtk.Label()

    def __init__(self):
        Gtk.VBox.__init__(self)
        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(timepix)

        time = str(datetime.now().strftime("%-I:%M:%S %p "))
        date_str = str(datetime.now().strftime("%A %b %d, %Y"))

        self.title.set_text(time)
        self.date_text.set_text(date_str)

        timedesc = Pango.FontDescription("AnjaliOldLipi Bold 150")
        self.title.override_font(timedesc)
        self.title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        datedesc = Pango.FontDescription("AnjaliOldLipi Bold 60")
        self.date_text.override_font(datedesc)
        self.date_text.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(self.title, True, False, 0)
        center.pack_start(self.date_text, True, False, 0)

        self.add(center)

    def update_clock(self):
        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(timepix)

        time = str(datetime.now().strftime("%-I:%M:%S %p "))
        date_str = str(datetime.now().strftime("%A %b %d, %Y"))

        self.title.set_text(time)
        self.date_text.set_text(date_str)
        return True


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
                          "[Up]\t or <equivalent gesture> cycle through calendar events\n"
                          "[Down]\t or <equivalent gesture> cycle through calendar events\n"
                          " \n"
                          "For any other technical/development aspect of this project, please refer to the wiki at\n "
                          "http://immerse.byu.edu/InteractiveDisplays/dokuwiki/doku.php?id=demo_info:iot:start\n")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        descriptdesc = Pango.FontDescription("Ubuntu Mono Italic 18")
        description.override_font(descriptdesc)
        description.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        description.set_line_wrap(True)

        helpdesc = Pango.FontDescription("Ubuntu Mono 18")
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
                          "Joseph Miera\t\t\t Input module\n"
                          "Levi Fleming\t\t\t Calendar and Messenger APIs and hardware design\n"
                          "Max Warner\t\t\t Quote API and hardware design\n"
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
    def __init__(self, t1, t2, t3, t4, d1, d2, d3, d4, l1, l2, l3, l4):
        Gtk.VBox.__init__(self)

        self.title_1 = t1
        self.title_2 = t2
        self.title_3 = t3
        self.title_4 = t4

        self.date_1 = d1
        self.date_2 = d2
        self.date_3 = d3
        self.date_4 = d4

        self.loc_1 = l1
        self.loc_2 = l2
        self.loc_3 = l3
        self.loc_4 = l4

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        event_space = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(calendarpix)

        up_image = Gtk.Image()
        down_image = Gtk.Image()
        up_image.set_from_pixbuf(uppix)
        down_image.set_from_pixbuf(downpix)

        title = Gtk.Label()
        title.set_text("Calendar")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        title.override_font(tempdesc)
        title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        event_title = Gtk.Label()
        event_date = Gtk.Label()
        event_location = Gtk.Label()

        titledesc = Pango.FontDescription("AnjaliOldLipi Bold 35")
        event_title.override_font(titledesc)
        event_title.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        datedesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        event_date.override_font(datedesc)
        event_date.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        locdesc = Pango.FontDescription("AnjaliOldLipi Bold 25")
        event_location.override_font(locdesc)
        event_location.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        event_title.set_text(self.title_1)
        event_date.set_text(self.date_1)
        event_location.set_text("@ " + self.loc_1)

        event_space.pack_start(event_title, True, False, 0)
        event_space.pack_start(event_date, True, False, 0)
        event_space.pack_start(event_location, True, False, 0)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(title, True, False, 0)
        center.pack_start(up_image, True, False, 0)
        center.pack_start(event_space, True, False, 0)
        center.pack_start(down_image, True, False, 0)
        self.add(center)

    def on_key(self, event):
        if event.keyval == Gdk.KEY_Up:
            print("banana")


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

        while self.info.weather_temp is "" or self.info.weather_cond is "" or self.info.weather_sunrise is "" or\
                self.info.weather_sunset is "" or self.info.weather_cloudiness is "" or self.info.weather_wind is "" or\
                self.info.weather_humidity is "" or self.info.weather_gid is "":
            print("LOADING WEATHER")


        # while self.info.quote_author is "" or self.info.quote_text is "":
        #     print("LOADING QUOTE")
        #     pass

        # while self.info.event_date_1 is "" or self.info.event_date_2 is "" or self.info.event_date_3 is "" or\
        #         self.info.event_date_4 is "" or self.info.event_location_1 is "" or self.info.event_location_2 is "" or\
        #         self.info.event_location_3 is "" or self.info.event_location_4 is "" or self.info.event_title_1 is "" or\
        #         self.info.event_title_2 is "" or self.info.event_title_3 is "" or self.info.event_title_4 is "":
        #     print("-" * 60)
        #     print(self.info.event_title_1)
        #     print(self.info.event_title_2)
        #     print(self.info.event_title_3)
        #     print(self.info.event_title_4)
        #     print(self.info.event_date_1)
        #     print(self.info.event_date_2)
        #     print(self.info.event_date_3)
        #     print(self.info.event_date_4)
        #     print(self.info.event_location_1)
        #     print(self.info.event_location_2)
        #     print(self.info.event_location_3)
        #     print(self.info.event_location_4)
        #     print("LOADING EVENT CALENDAR")

        # TODO:
        # Quote of the day queue info loading
        self.remove(loading)
        # self.load_weather()
        # self.load_quote()
        # quote = Quote()
        help = Help()
        info = Info()
        calendar = Calendar(self.info.event_title_1, self.info.event_title_2, self.info.event_title_3,
                            self.info.event_title_4, self.info.event_date_1, self.info.event_date_2,
                            self.info.event_date_3, self.info.event_date_4, self.info.event_location_1,
                            self.info.event_location_2, self.info.event_location_3, self.info.event_location_4)
        messages = Messages()
        mirror = Mirror()
        home = Home()
        self.add(home)
        # self.time = TimeDate()
        # self.remove(loading)
        # self.add(loading)
        # self.add(mirror)
        # self.add(help)
        # self.add(info)
        # self.add(self.time)
        # self.start_time()
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

        # STATE = self.state_list[0]
        self.fullscreen()
        self.modify_bg(Gtk.StateType.NORMAL, black)
        self.set_default_size(500, 500)
        self.set_icon(iconpix)

    def load_weather(self):
        condition = self.get_weather_condition()
        image = self.get_weather_logo()
        weather = Weather(self.info.weather_temp, condition, self.info.weather_sunrise,
                          self.info.weather_sunset, self.info.weather_cloudiness, self.info.weather_wind,
                          self.info.weather_humidity, image)
        self.add(weather)

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
            if self.info.weather_gid == "731":
                condition = "Sand/Dust Whirls"
            elif self.info.weather_gid == "761":
                condition = "Dust"
            else:
                condition = "Not Recognized"
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
            if self.info.weather_gid == "622":
                condition = "Heavy Shower Snow"
            elif self.info.weather_gid == "600":
                condition = "Light Snow"
            elif self.info.weather_gid == "601":
                condition = "Snow"
            elif self.info.weather_gid == "602":
                condition = "Heavy Snow"
            elif self.info.weather_gid == "611":
                condition = "Sleet"
            elif self.info.weather_gid == "612":
                condition = "Light Shower Sleet"
            elif self.info.weather_gid == "613":
                condition = "Shower Sleet"
            elif self.info.weather_gid == "615":
                condition = "Light Rain and Snow"
            elif self.info.weather_gid == "616":
                condition = "Rain and Snow"
            elif self.info.weather_gid == "620":
                condition = "Light Shower Snow"
            elif self.info.weather_gid == "621":
                condition = "Shower Snow"
            else:
                condition = "Not Recognized"
        elif self.info.weather_cond == "Rain":
            if self.info.weather_gid == "500":
                condition = "Light Rain"
            elif self.info.weather_gid == "501":
                condition = "Moderate Rain"
            elif self.info.weather_gid == "502":
                condition = "Heavy Intensity Rain"
            elif self.info.weather_gid == "503":
                condition = "Very Heavy Rain"
            elif self.info.weather_gid == "504":
                condition = "Extreme Rain"
            elif self.info.weather_gid == "511":
                condition = "Freezing Rain"
            elif self.info.weather_gid == "520":
                condition = "Light Intensity Shower Rain"
            elif self.info.weather_gid == "521":
                condition = "Shower Rain"
            elif self.info.weather_gid == "522":
                condition = "Heavy Intensity Shower Rain"
            elif self.info.weather_gid == "531":
                condition = "Ragged Shower Rain"
            else:
                condition = "Not Recognized"
        elif self.info.weather_cond == "Drizzle":
            if self.info.weather_gid == "300":
                condition = "Light Intensity Drizzle"
            elif self.info.weather_cond == "301":
                condition = "Drizzle"
            elif self.info.weather_cond == "302":
                condition = "Heavy Intensity Drizzle"
            elif self.info.weather_cond == "310":
                condition = "Light Intensity Drizzle Rain"
            elif self.info.weather_cond == "311":
                condition = "Drizzle Rain"
            elif self.info.weather_cond == "312":
                condition = "Heavy Intensity Drizzle Rain"
            elif self.info.weather_cond == "313":
                condition = "Shower Rain and Drizzle"
            elif self.info.weather_cond == "314":
                condition = "Heavy Shower Rain and Drizzle"
            elif self.info.weather_cond == "321":
                condition = "Shower Drizzle"
            else:
                condition = "Not Recognized"
        elif self.info.weather_cond == "Thunderstorm":
            if self.info.weather_gid == "200":
                condition = "Thunderstorm with Light Rain"
            elif self.info.weather_gid == "201":
                condition = "Thunderstorm with Rain"
            elif self.info.weather_gid == "202":
                condition = "Thunderstorm with Heavy Rain"
            elif self.info.weather_gid == "210":
                condition = "Light Thunderstorm"
            elif self.info.weather_gid == "211":
                condition = "Thunderstorm"
            elif self.info.weather_gid == "212":
                condition = "Heavy Thunderstorm"
            elif self.info.weather_gid == "221":
                condition = "Ragged Thunderstorm"
            elif self.info.weather_gid == "230":
                condition = "Thunderstorm with Light Drizzle"
            elif self.info.weather_gid == "231":
                condition = "Thunderstorm with Drizzle"
            elif self.info.weather_gid == "232":
                condition = "Thunderstorm with Heavy Drizzle"
            else:
                "Not Recognized"
        return condition

    def get_weather_logo(self):
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

    def load_quote(self):
        text = self.info.quote_text
        author = self.info.quote_author
        quote = Quote(text, author)
        self.add(quote)

    def do_key_press_event(self, event):
        global ENABLE_TIMER
        global CUR_KEY
        global STATE
        Gtk.Window.do_key_press_event(self, event)
        CUR_KEY = event.keyval
        # print(CUR_KEY)
        if event.keyval == Gdk.KEY_Escape:
            self.unfullscreen()
            self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
        elif event.keyval == Gdk.KEY_F11:
            self.fullscreen()
        elif event.keyval == Gdk.KEY_h and STATE is not self.state_list[0]:
            # self.get_root_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
            self.go_home()
        elif event.keyval == Gdk.KEY_w and STATE is not self.state_list[1]:
            self.get_weather()
        elif event.keyval == Gdk.KEY_t and STATE is not self.state_list[2]:
            # global ENABLE_TIMER
            ENABLE_TIMER = True
            self.get_time_date()
        elif event.keyval == Gdk.KEY_m and STATE is not self.state_list[3]:
            self.show_messages()
        elif event.keyval == Gdk.KEY_q and STATE is not self.state_list[4]:
            self.show_quote()
        elif event.keyval == Gdk.KEY_c and STATE is not self.state_list[5]:
            self.show_calendar()
        elif event.keyval == Gdk.KEY_F1 and STATE is not self.state_list[6]:
            self.show_help()
        elif event.keyval == Gdk.KEY_i and STATE is not self.state_list[7]:
            self.show_info()
        elif event.keyval == Gdk.KEY_n and STATE is not self.state_list[8]:
            self.show_mirror()
        elif event.keyval == Gdk.KEY_Left:
            ENABLE_TIMER = False
            if self.state_list.index(STATE) != 1:
                STATE = self.state_list[self.state_list.index(str(STATE)) - 1]
                if STATE is "WEATHER":
                    self.get_weather()
                elif STATE is "TIME":
                    ENABLE_TIMER = True
                    self.get_time_date()
                elif STATE is "MESSAGES":
                    self.show_messages()
                elif STATE is "QUOTE":
                    self.show_quote()
                elif STATE is "CALENDAR":
                    self.show_calendar()
                elif STATE is "HELP":
                    self.show_help()
                elif STATE is "INFO":
                    self.show_info()
                elif STATE == "MIRROR":
                    self.show_mirror()
            elif self.state_list.index(STATE) == 1:
                STATE = self.state_list[len(self.state_list) - 1]
                self.show_mirror()
        elif event.keyval == Gdk.KEY_Right:
            ENABLE_TIMER = False
            if self.state_list.index(STATE) != len(self.state_list) - 1:
                STATE = self.state_list[self.state_list.index(str(STATE)) + 1]
                if STATE == "WEATHER":
                    self.get_weather()
                elif STATE is "TIME":
                    ENABLE_TIMER = True
                    self.get_time_date()
                elif STATE is "MESSAGES":
                    self.show_messages()
                elif STATE is "QUOTE":
                    self.show_quote()
                elif STATE is "CALENDAR":
                    self.show_calendar()
                elif STATE is "HELP":
                    self.show_help()
                elif STATE is "INFO":
                    self.show_info()
                elif STATE is "MIRROR":
                    self.show_mirror()
            elif self.state_list.index(STATE) == len(self.state_list) - 1:
                STATE = self.state_list[1]
                self.get_weather()
        elif (event.keyval == Gdk.KEY_Up) and (STATE is "CALENDAR"):
            print("derpaflerp")

    def go_home(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        STATE = self.state_list[0]
        # self.HOME.set_reveal_child(True)
        # self.HOME.set_transition_type(Gtk.RevealerTransitionType.CROSSFADE)
        # self.HOME.add(self.grid)
        # self.add(self.HOME)
        self.title.set_text("HOME")
        self.image.set_from_pixbuf(homepix)
        print(STATE)

    def start_time(self):
        GObject.timeout_add(1000, self.time.update_clock)

    def show_messages(self):
        global ENABLE_TIMER
        ENABLE_TIMER = False
        STATE = self.state_list[3]
        self.destroy_children()
        self.title.set_text("MESSAGES")
        self.image.set_from_pixbuf(messagespix)
        self.grid.add(self.picbox)
        self.grid.attach_next_to(self.titlebox, self.picbox, Gtk.PositionType.BOTTOM, 1, 2)
        print(STATE)

    def destroy_children(self):
        for item in self.grid:
            self.grid.remove(item)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
