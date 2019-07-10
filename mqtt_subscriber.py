import paho.mqtt.client as mqtt
from datetime import datetime
from dateutil import tz
from time import sleep, time


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


def time_field_get(time_event):
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


class UpdateInfo:
    broker_address = "postman.cloudmqtt.com"
    password = "yMk7upKt2dcGEao3u2uxvXC4KnQRL224"
    username = "messages"
    port = 27408
    ssl_certificate = r"/home/christopolise/devel/SmartMirrorGUI/ca.crt"
    Connected = False  # global variable for the state of the connection
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    def __init__(self):
        client = self.create_client("GUI_subscriber")
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.subscribe("immerse/#")
        client.loop_start()  # start the loop
        print("Reading from immerse/#")
        self.client = client

        # Weather Values:
        self.weather_temp = ""
        self.weather_cond = ""
        self.weather_cloudiness = ""
        self.weather_wind = ""
        self.weather_humidity = ""
        self.weather_sunrise = ""
        self.weather_sunset = ""
        self.weather_time_of_day = ""

        # Event Values:
        self.event_title_1 = ""
        self.event_title_2 = ""
        self.event_title_3 = ""
        self.event_title_4 = ""
        self.event_date_1 = ""
        self.event_date_2 = ""
        self.event_date_3 = ""
        self.event_date_4 = ""
        self.event_location_1 = ""
        self.event_location_2 = ""
        self.event_location_3 = ""
        self.event_location_4 = ""

        self.message_queue = []

    def run(self):
        while not self.Connected:  # Wait for connection
            sleep(0.1)

        try:
            while True:
                sleep(5)

        except KeyboardInterrupt:
            print("exiting")
            self.client.disconnect()
            self.client.loop_stop()

    def create_client(self, name):
        print("Creating Client")
        client = mqtt.Client(name)  # create new instance
        client.username_pw_set(self.username, password=self.password)  # set username and password
        client.tls_set(ca_certs=self.ssl_certificate)
        client.connect(self.broker_address, port=self.port)  # connect to broker
        print("Finished Creating Client")
        return client

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            global Connected  # Use global variable
            Connected = True  # Signal connection
        else:
            print("Connection failed")

    def on_message(self, client, userdata, msg):
        # print(msg.payload)
        # self.get_day_night()
        topic = str(msg.topic).split('/')
        if topic[1] == "Weather":
            print("Incoming from Weather")
            if topic[2] == "Temp":
                self.weather_temp = msg.payload.decode("utf-8")[:-1]
            elif topic[2] == "Condition":
                self.weather_cond = str(msg.payload.decode("utf-8"))
            elif topic[2] == "Sunrise":
                sunrise = datetime_from_utc_to_local(datetime.utcfromtimestamp(float(msg.payload.decode("utf-8"))))
                self.weather_sunrise = sunrise.strftime("%-I:%M %p ")
            elif topic[2] == "Sunset":
                sunset = datetime_from_utc_to_local(datetime.utcfromtimestamp(float(msg.payload.decode("utf-8"))))
                self.weather_sunset = sunset.strftime("%-I:%M %p ")
            elif topic[2] == "Clouds":
                self.weather_cloudiness = str(msg.payload.decode("utf-8"))
            elif topic[2] == "Wind_Speed":
                self.weather_wind = str(msg.payload.decode("utf-8"))
            elif topic[2] == "Humidity":
                self.weather_humidity = str(msg.payload.decode("utf-8"))
            else:
                print("Unrecognized weather val: ", topic[2])
            self.get_day_night()
        elif topic[1] == "event":
            print("Incoming from Calendar")
            if topic[3] == 0:
                if topic[2] == "title":
                    self.event_title_1 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "date":
                    self.event_date_1 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "location":
                    self.event_location_1 = str(msg.payload.decode("utf-8"))
                else:
                    print("Unsupported parameter: ", topic[2])
            elif topic[3] == 1:
                if topic[2] == "title":
                    self.event_title_2 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "date":
                    self.event_date_2 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "location":
                    self.event_location_2 = str(msg.payload.decode("utf-8"))
                else:
                    print("Unsupported parameter: ", topic[2])
            elif topic[3] == 2:
                if topic[2] == "title":
                    self.event_title_3 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "date":
                    self.event_date_3 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "location":
                    self.event_location_3 = str(msg.payload.decode("utf-8"))
                else:
                    print("Unsupported parameter: ", topic[2])
            elif topic[3] == 3:
                if topic[2] == "title":
                    self.event_title_4 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "date":
                    self.event_date_4 = str(msg.payload.decode("utf-8"))
                elif topic[2] == "location":
                    self.event_location_4 = str(msg.payload.decode("utf-8"))
                else:
                    print("Unsupported parameter: ", topic[2])
            else:
                print("Unsupported number of calendar events")
        elif topic[1] == "messages":
            print("Incoming from Messenger")
            if len(self.message_queue) < 11:
                self.message_queue.insert(0, str(msg.payload.decode("utf-8")))
            elif len(self.message_queue) == 10:
                self.message_queue.pop()
                self.message_queue.insert(0, str(msg.payload.decode("utf-8")))
        else:
            print("Unrecognized channel: ", topic[1])
        print("Temp: ", self.weather_temp)
        print("Cond: ", self.weather_cond)
        print("Sunrise: ", self.weather_sunrise)
        print("Sunset: ", self.weather_sunset)
        print("Cloudiness: ", self.weather_cloudiness)
        print("Wind Speed: ", self.weather_wind)
        print("Humidity: ", self.weather_humidity)
        print("Time of Day:", self.weather_time_of_day)

    def get_day_night(self):
        now = datetime.now()
        hour, minute = time_field_get(self.weather_sunrise)
        sunrise = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
        hour, minute = time_field_get(self.weather_sunset)
        sunset = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)

        if sunrise <= now < sunset:
            self.weather_time_of_day = "day"
        else:
            self.weather_time_of_day = "night"

    def parse_weather_data(self):
        pass


if __name__ == '__main__':
    main = UpdateInfo()
    main.run()
