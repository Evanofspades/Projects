from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime

app = Flask(__name__)

scheduler = APScheduler()

# drinked
# sleep


# global h

# sleep = False

time = datetime.now()

h = int(time.strftime("%H"))

sleep = False
drinked = False


def check_hour():
    global sleep
    if h in range(0, 10):
        sleep = True
    else:
        sleep = False
    return sleep


#
#
#     print(sleep)
#
#
# print(h)


def set_sleep(status):
    global drinked
    drinked = status


def Drink_water():
    global drinked
    if not check_hour():
        print("Drink water ok?")
        drinked = False


def Check_if_you_drinked():
    if drinked == False:
        print("did you drink water??")


@app.route("/")
def home():
    return ("hello")


@app.route("/false")
def Tsleep():
    set_sleep(status=False)
    return "False"


@app.route("/true")
def Tasleep():
    set_sleep(True)
    return "True"


if __name__ == "__main__":
    scheduler.add_job(id="drink_water", func=Drink_water, trigger="interval", seconds=30)
    scheduler.add_job(id="check", func=Check_if_you_drinked, trigger="interval", seconds=5)
    scheduler.start()
    app.run(host="0.0.0.0")