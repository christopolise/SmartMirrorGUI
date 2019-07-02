import paho.mqtt.client as mqtt
from datetime import datetime
from dateutil import tz
from time import sleep, time


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


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
        self.weather_temp = float
        self.weather_cond = str
        self.weather_cloudiness = str
        self.weather_wind = str
        self.weather_humidity = str
        self.weather_sunrise = str
        self.weather_sunset = str

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
        topic = str(msg.topic).split('/')
        if topic[1] == "Weather":
            # print("Incoming from Weather")
            if topic[2] == "Temp":
                self.weather_temp = float(msg.payload.decode("utf-8"))
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
        elif topic[1] == "event":
            print("Incoming from Calendar")
        elif topic[1] == "messages":
            print("Incoming from Messenger")
        else:
            print("Unrecognized channel: ", topic[1])
        print("Temp: ", self.weather_temp)
        print("Cond: ", self.weather_cond)
        print("Sunrise: ", self.weather_sunrise)
        print("Sunset: ", self.weather_sunset)
        print("Cloudiness: ", self.weather_cloudiness)
        print("Wind Speed: ", self.weather_wind)
        print("Humidity: ", self.weather_humidity)


if __name__ == '__main__':
    main = UpdateInfo()
    main.run()
