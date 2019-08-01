from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GObject
from datetime import datetime
from dateutil import tz
from time import sleep, time
import Images as IMG


class WeatherData:
    def __init__(self):
        self.count = 0
        self.temperature = "TEMPERATURE"
        self.condition = "CONDITION"
        print("This was reassigned")
        self.sunrise = "SUNRISE"
        self.sunset = "SUNSET"
        self.cloudiness = "CLOUDINESS"
        self.wind = "WIND"
        self.humidity = "HUMIDITY"
        self.image = IMG.logopix
        self.gid = "GID"
        self.time_of_day = "DAY"

    def datetime_from_utc_to_local(self, utc_datetime):
        now_timestamp = time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        return utc_datetime + offset

    def time_field_get(self, time_event):
        certain_time = time_event.split(':')
        hour = ""
        minute_day = ""
        minute = ""
        time_of_day = ""
        for item in range(len(certain_time)):
            if item == 0:
                hour = certain_time[item]
            elif item == 1:
                minute_day = certain_time[item]
        minute_day = minute_day.split()
        for item in range(len(minute_day)):
            if item == 0:
                minute = minute_day[item]
            elif item == 1:
                time_of_day = minute_day[item]
        if time_of_day == "PM":
            hour = int(hour) + 12

        return hour, minute

    def update(self, topic, payload):
        self.count += 1
        topic = str(topic).split('/')
        if topic[1] == "Weather":
            print("Incoming from Weather")
            if topic[2] == "Temp":
                self.temperature = payload.decode("utf-8")
                print("GID: ", self.gid)
            elif topic[2] == "Condition":
                update_cond = str(payload.decode("utf-8"))
                print("Condition ", update_cond)
                if update_cond == "Clouds":
                    if 11 <= int(self.cloudiness) < 25:
                        self.condition = "Few Clouds"
                    elif 25 <= int(self.cloudiness) <= 50:
                        self.condition = "Sparse Clouds"
                    elif 51 <= int(self.cloudiness) <= 84:
                        self.condition = "Broken Clouds"
                    elif 85 <= int(self.cloudiness) <= 100:
                        self.condition = "Overcast Clouds"
                elif update_cond == "Clear":
                    self.condition = "Sky is Clear"
                elif update_cond == "Mist":
                    self.condition = "Mist"
                elif update_cond == "Smoke":
                    self.condition = "Smoke"
                elif update_cond == "Haze":
                    self.condition = "Haze"
                elif update_cond == "Dust":
                    if self.gid == "731":
                        self.condition = "Sand/Dust Whirls"
                    elif self.gid == "761":
                        self.condition = "Dust"
                    else:
                        self.condition = "Not Recognized, 5"
                elif update_cond == "Fog":
                    self.condition = "Fog"
                elif update_cond == "Sand":
                    self.condition = "Sand"
                elif update_cond == "Ash":
                    self.condition = "Volcanic Ash"
                elif update_cond == "Squall":
                    self.condition = "Squalls"
                elif update_cond == "Tornado":
                    self.condition = "Tornado"
                elif update_cond == "Snow":
                    if self.gid == "622":
                        self.condition = "Heavy Shower Snow"
                    elif self.gid == "600":
                        self.condition = "Light Snow"
                    elif self.gid == "601":
                        self.condition = "Snow"
                    elif self.gid == "602":
                        self.condition = "Heavy Snow"
                    elif self.gid == "611":
                        self.condition = "Sleet"
                    elif self.gid == "612":
                        self.condition = "Light Shower Sleet"
                    elif self.gid == "613":
                        self.condition = "Shower Sleet"
                    elif self.gid == "615":
                        self.condition = "Light Rain and Snow"
                    elif self.gid == "616":
                        self.condition = "Rain and Snow"
                    elif self.gid == "620":
                        self.condition = "Light Shower Snow"
                    elif self.gid == "621":
                        self.condition = "Shower Snow"
                    else:
                        self.condition = "Not Recognized, 4"
                elif update_cond == "Rain":
                    print("THIS PART WAS REACHED")
                    if self.gid == "500":
                        self.condition = "Light Rain"
                    elif self.gid == "501":
                        self.condition = "Moderate Rain"
                    elif self.gid == "502":
                        self.condition = "Heavy Intensity Rain"
                    elif self.gid == "503":
                        self.condition = "Very Heavy Rain"
                    elif self.gid == "504":
                        self.condition = "Extreme Rain"
                    elif self.gid == "511":
                        self.condition = "Freezing Rain"
                    elif self.gid == "520":
                        self.condition = "Light Intensity Shower Rain"
                    elif self.gid == "521":
                        self.condition = "Shower Rain"
                    elif self.gid == "522":
                        self.condition = "Heavy Intensity Shower Rain"
                    elif self.gid == "531":
                        self.condition = "Ragged Shower Rain"
                    else:
                        self.condition = "Not Recognized, 3" + str(self.gid)

                elif update_cond == "Drizzle":
                    if self.gid == "300":
                        self.condition = "Light Intensity Drizzle"
                    elif self.gid == "301":
                        self.condition = "Drizzle"
                    elif self.gid == "302":
                        self.condition = "Heavy Intensity Drizzle"
                    elif self.gid == "310":
                        self.condition = "Light Intensity Drizzle Rain"
                    elif self.gid == "311":
                        self.condition = "Drizzle Rain"
                    elif self.gid == "312":
                        self.condition = "Heavy Intensity Drizzle Rain"
                    elif self.gid == "313":
                        self.condition = "Shower Rain and Drizzle"
                    elif self.gid == "314":
                        self.condition = "Heavy Shower Rain and Drizzle"
                    elif self.gid == "321":
                        self.condition = "Shower Drizzle"
                    else:
                        self.condition = "Not Recognized, 2"
                elif update_cond == "Thunderstorm":
                    if self.gid == "200":
                        self.condition = "Thunderstorm with Light Rain"
                    elif self.gid == "201":
                        self.condition = "Thunderstorm with Rain"
                    elif self.gid == "202":
                        self.condition = "Thunderstorm with Heavy Rain"
                    elif self.gid == "210":
                        self.condition = "Light Thunderstorm"
                    elif self.gid == "211":
                        self.condition = "Thunderstorm"
                    elif self.gid == "212":
                        self.condition = "Heavy Thunderstorm"
                    elif self.gid == "221":
                        self.condition = "Ragged Thunderstorm"
                    elif self.gid == "230":
                        self.condition = "Thunderstorm with Light Drizzle"
                    elif self.gid == "231":
                        self.condition = "Thunderstorm with Drizzle"
                    elif self.gid == "232":
                        self.condition = "Thunderstorm with Heavy Drizzle"
                    else:
                        self.condition = "Not Recognized, 0"
                        print("Disguy")
                print("GID: ", self.gid)
            elif topic[2] == "Sunrise":
                sunrise = self.datetime_from_utc_to_local(datetime.utcfromtimestamp(float(payload.decode("utf-8"))))
                self.sunrise = sunrise.strftime("%-I:%M %p ")
                print("GID: ", self.gid)
            elif topic[2] == "Sunset":
                sunset = self.datetime_from_utc_to_local(datetime.utcfromtimestamp(float(payload.decode("utf-8"))))
                self.sunset = sunset.strftime("%-I:%M %p ")
                print("GID: ", self.gid)
            elif topic[2] == "Clouds":
                self.cloudiness = str(payload.decode("utf-8"))
                print("GID: ", self.gid)
            elif topic[2] == "Wind_Speed":
                self.wind = str(payload.decode("utf-8"))
                print("GID: ", self.gid)
            elif topic[2] == "Humidity":
                self.humidity = str(payload.decode("utf-8"))
                print("GID: ", self.gid)
            elif topic[2] == "GID":
                self.gid = str(payload.decode("utf-8"))
                print("GID: ", self.gid)
            else:
                print("Unrecognized weather val: ", topic[2])

        now = datetime.now()
        hour, minute = self.time_field_get(self.sunrise)
        sunrise = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
        hour, minute = self.time_field_get(self.sunset)
        sunset = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)

        if sunrise <= now < sunset:
            self.time_of_day = "day"
        else:
            self.time_of_day = "night"

        # if update_cond == "Clouds":
        #     if 11 <= int(self.cloudiness) < 25:
        #         self.condition = "Few Clouds"
        #     elif 25 <= int(self.cloudiness) <= 50:
        #         self.condition = "Sparse Clouds"
        #     elif 51 <= int(self.cloudiness) <= 84:
        #         self.condition = "Broken Clouds"
        #     elif 85 <= int(self.cloudiness) <= 100:
        #         self.condition = "Overcast Clouds"
        # elif update_cond == "Clear":
        #     self.condition = "Sky is Clear"
        # elif update_cond == "Mist":
        #     self.condition = "Mist"
        # elif update_cond == "Smoke":
        #     self.condition = "Smoke"
        # elif update_cond == "Haze":
        #     self.condition = "Haze"
        # elif update_cond == "Dust":
        #     if self.gid == "731":
        #         self.condition = "Sand/Dust Whirls"
        #     elif self.gid == "761":
        #         self.condition = "Dust"
        #     else:
        #         self.condition = "Not Recognized"
        # elif update_cond == "Fog":
        #     self.condition = "Fog"
        # elif update_cond == "Sand":
        #     self.condition = "Sand"
        # elif update_cond == "Ash":
        #     self.condition = "Volcanic Ash"
        # elif update_cond == "Squall":
        #     self.condition = "Squalls"
        # elif update_cond == "Tornado":
        #     self.condition = "Tornado"
        # elif update_cond == "Snow":
        #     if self.gid == "622":
        #         self.condition = "Heavy Shower Snow"
        #     elif self.gid == "600":
        #         self.condition = "Light Snow"
        #     elif self.gid == "601":
        #         self.condition = "Snow"
        #     elif self.gid == "602":
        #         self.condition = "Heavy Snow"
        #     elif self.gid == "611":
        #         self.condition = "Sleet"
        #     elif self.gid == "612":
        #         self.condition = "Light Shower Sleet"
        #     elif self.gid == "613":
        #         self.condition = "Shower Sleet"
        #     elif self.gid == "615":
        #         self.condition = "Light Rain and Snow"
        #     elif self.gid == "616":
        #         self.condition = "Rain and Snow"
        #     elif self.gid == "620":
        #         self.condition = "Light Shower Snow"
        #     elif self.gid == "621":
        #         self.condition = "Shower Snow"
        #     else:
        #         self.condition = "Not Recognized"
        # elif update_cond == "Rain":
        #     print("THIS PART WAS REACHED")
        #     if self.gid == "500":
        #         self.condition = "Light Rain"
        #     elif self.gid == "501":
        #         self.condition = "Moderate Rain"
        #     elif self.gid == "502":
        #         self.condition = "Heavy Intensity Rain"
        #     elif self.gid == "503":
        #         self.condition = "Very Heavy Rain"
        #     elif self.gid == "504":
        #         self.condition = "Extreme Rain"
        #     elif self.gid == "511":
        #         self.condition = "Freezing Rain"
        #     elif self.gid == "520":
        #         self.condition = "Light Intensity Shower Rain"
        #     elif self.gid == "521":
        #         self.condition = "Shower Rain"
        #     elif self.gid == "522":
        #         self.condition = "Heavy Intensity Shower Rain"
        #     elif self.gid == "531":
        #         self.condition = "Ragged Shower Rain"
        #     else:
        #         self.condition = "Not Recognized"
        # elif update_cond == "Drizzle":
        #     if self.gid == "300":
        #         self.condition = "Light Intensity Drizzle"
        #     elif self.gid == "301":
        #         self.condition = "Drizzle"
        #     elif self.gid == "302":
        #         self.condition = "Heavy Intensity Drizzle"
        #     elif self.gid == "310":
        #         self.condition = "Light Intensity Drizzle Rain"
        #     elif self.gid == "311":
        #         self.condition = "Drizzle Rain"
        #     elif self.gid == "312":
        #         self.condition = "Heavy Intensity Drizzle Rain"
        #     elif self.gid == "313":
        #         self.condition = "Shower Rain and Drizzle"
        #     elif self.gid == "314":
        #         self.condition = "Heavy Shower Rain and Drizzle"
        #     elif self.gid == "321":
        #         self.condition = "Shower Drizzle"
        #     else:
        #         self.condition = "Not Recognized"
        # elif update_cond == "Thunderstorm":
        #     if self.gid == "200":
        #         self.condition = "Thunderstorm with Light Rain"
        #     elif self.gid == "201":
        #         self.condition = "Thunderstorm with Rain"
        #     elif self.gid == "202":
        #         self.condition = "Thunderstorm with Heavy Rain"
        #     elif self.gid == "210":
        #         self.condition = "Light Thunderstorm"
        #     elif self.gid == "211":
        #         self.condition = "Thunderstorm"
        #     elif self.gid == "212":
        #         self.condition = "Heavy Thunderstorm"
        #     elif self.gid == "221":
        #         self.condition = "Ragged Thunderstorm"
        #     elif self.gid == "230":
        #         self.condition = "Thunderstorm with Light Drizzle"
        #     elif self.gid == "231":
        #         self.condition = "Thunderstorm with Drizzle"
        #     elif self.gid == "232":
        #         self.condition = "Thunderstorm with Heavy Drizzle"
        #     else:
        #         "Not Recognized"

        # now = datetime.now()
        # hour, minute = self.time_field_get(self.sunrise)
        # sunrise = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
        # hour, minute = self.time_field_get(self.sunset)
        # sunset = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
        #
        # if sunrise <= now < sunset:
        #     self.time_of_day = "day"
        # else:
        #     self.time_of_day = "night"

        if update_cond == "Clouds":
            if 11 <= int(self.cloudiness) < 25:
                if self.time_of_day == "day":
                    self.image = IMG.cloudsdaypix
                else:
                    self.image = IMG.cloudsnightpix
            elif 25 <= int(self.cloudiness) <= 50:
                if self.time_of_day == "day":
                    self.image = IMG.cloudsdaypix
                else:
                    self.image = IMG.cloudsnightpix
            elif 51 <= int(self.cloudiness) <= 84:
                self.image = IMG.brokencloudspix
            elif 85 <= int(self.cloudiness) <= 100:
                self.image = IMG.brokencloudspix
        elif update_cond == "Clear":
            if self.time_of_day == "day":
                self.image = IMG.cleardaypix
            else:
                self.image = IMG.clearnightpix
        elif update_cond == "Mist":
            self.image = IMG.mistpix
        elif update_cond == "Smoke":
            self.image = IMG.mistpix
        elif update_cond == "Haze":
            self.image = IMG.mistpix
        elif update_cond == "Dust":
            self.image = IMG.mistpix
        elif update_cond == "Fog":
            self.image = IMG.mistpix
        elif update_cond == "Sand":
            self.image = IMG.mistpix
        elif update_cond == "Ash":
            self.image = IMG.mistpix
        elif update_cond == "Squall":
            self.image = IMG.mistpix
        elif update_cond == "Tornado":
            self.image = IMG.mistpix
        elif update_cond == "Snow":
            self.image = IMG.snowpix
        elif update_cond == "Rain":
            self.image = IMG.rainpix
        elif update_cond == "Drizzle":
            self.image = IMG.showerspix
        elif update_cond == "Thunderstorm":
            self.image = IMG.thunderstormpix


class Weather(Gtk.Layout):
    __gtype_name__ = 'Weather'

    def __init__(self, weather_data):
        Gtk.Layout.__init__(self)
        self.set_border_width(20)

        self.weather_data = weather_data

        self.temperature = self.weather_data.temperature
        self.condition = self.weather_data.condition
        self.sunrise = self.weather_data.sunrise
        self.sunset = self.weather_data.sunset
        self.cloudiness = self.weather_data.cloudiness
        self.wind = self.weather_data.wind
        self.humidity = self.weather_data.humidity
        self.image = self.weather_data.image

        self.humidity_label = Gtk.Label()
        self.wind_label = Gtk.Label()
        self.cloudiness_label = Gtk.Label()
        self.sunset_label = Gtk.Label()
        self.sunrise_label = Gtk.Label()
        self.condition_label = Gtk.Label()
        self.temperature_label = Gtk.Label()

        self.status_image = Gtk.Image()

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()
        sunbox = Gtk.HBox()
        cloudbox = Gtk.HBox()

        self.status_image.set_from_pixbuf(self.image)

        sunrise_image = Gtk.Image()
        sunset_image = Gtk.Image()
        sunrise_image.set_from_pixbuf(IMG.sunrisepix)
        sunset_image.set_from_pixbuf(IMG.sunsetpix)

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 150")
        self.temperature_label.override_font(tempdesc)
        self.temperature_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        conditiondesc = Pango.FontDescription("AnjaliOldLipi Bold 70")
        self.condition_label.override_font(conditiondesc)
        self.condition_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        labeldesc = Pango.FontDescription("AnjaliOldLipi Bold 23")

        self.sunrise_label.override_font(labeldesc)
        self.sunrise_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.sunset_label.override_font(labeldesc)
        self.sunset_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.cloudiness_label.override_font(labeldesc)
        self.cloudiness_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.wind_label.override_font(labeldesc)
        self.wind_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        self.humidity_label.override_font(labeldesc)
        self.humidity_label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))

        self.temperature_label.set_text(self.temperature.split('.')[0] + "°F")
        self.condition_label.set_text(self.condition)
        self.sunrise_label.set_text(self.sunrise)
        self.sunset_label.set_text(self.sunset)
        self.cloudiness_label.set_text("Cloudiness: " + self.cloudiness + '%')
        self.wind_label.set_text("Wind Speed: " + self.wind + ' mph')
        self.humidity_label.set_text("Humidity: " + self.humidity + '%')

        sunbox.pack_start(sunrise_image, True, False, 0)
        sunbox.pack_start(self.sunrise_label, True, True, 0)
        sunbox.pack_start(sunset_image, True, True, 0)
        sunbox.pack_start(self.sunset_label, True, True, 0)
        sunbox.pack_start(self.humidity_label, True, True, 0)

        cloudbox.pack_start(self.cloudiness_label, True, False, 0)
        cloudbox.pack_start(self.wind_label, True, False, 0)

        center.pack_start(self.status_image, True, False, 0)
        center.pack_start(self.temperature_label, True, False, 0)
        center.pack_start(self.condition_label, True, False, 0)
        center.pack_start(cloudbox, True, False, 0)
        center.pack_start(sunbox, True, False, 0)
        self.put(center, ((Gdk.Screen.width() / 2) - 325), 100)
        # self.add(center)

    def update_weather(self):
        # print(self.weather_data.condition, "gloog")
        self.humidity_label.set_text("Humidity: " + self.weather_data.humidity + '%')
        self.wind_label.set_text("Wind Speed: " + self.weather_data.wind + ' mph')
        self.cloudiness_label.set_text("Cloudiness: " + self.weather_data.cloudiness + '%')
        self.sunset_label.set_text(self.weather_data.sunset)
        self.sunrise_label.set_text(self.weather_data.sunrise)
        self.condition_label.set_text(self.weather_data.condition)
        self.temperature_label.set_text(self.weather_data.temperature.split('.')[0] + "°F")

        self.status_image.set_from_pixbuf(self.weather_data.image)

        return True
