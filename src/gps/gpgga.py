import pynmea2
import serial

# s = "GPGGA,144758.00,4519.13011,N,07545.36373,W,1,09,0.95,86.1,M,-34.2,M,,*5D"
# msg = pynmea2.parse(s)
# print("latitude", msg.latitude, msg.lat_dir, "            longitude", msg.longitude, msg.lon_dir)

gps = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 0.1)
coord = []

while True:
    s = gps.readline().decode("utf-8")
    print(s)
    if s[0:6] == "$GPGGA":
        msg = pynmea2.parse(s)
        data = {"latitude": msg.latitude, "logitude": msg.longitude}
        coord.append(data)
        # print(data)
    # else:
        # data = "nothing"
    # print(data)