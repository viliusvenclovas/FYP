# External module imp
import RPi.GPIO as GPIO
import datetime
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="34.89.20.156",
  user="root",
  password="root",
  database="project"
)

mycursor = mydb.cursor()


init = False

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered", "r")
        return f.readline()
    except:
        return "NEVER!"
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 0
            add_to_db()
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)
                    add_to_db()
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
    add_to_db()


def add_to_db():
    sql = "INSERT INTO data (data) VALUES (%s)"
    date_time = datetime.datetime
    mycursor.execute(sql, date_time)
