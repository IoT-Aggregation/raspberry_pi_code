from flask import Flask
from flask_restful import Api, Resource
from threading import Thread
# from kivy.clock import Clock
from adc_converter import get_pin_value, get_all_pins_values
from config import TIME_INTERVAL

'''
class cyclic_sensors_state(Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        Clock.schedule_interval(get_all_pins_values, TIME_INTERVAL)
'''
        
# Define resources (endpoints)
class SensorsList(Resource):
    def get(self):
        return get_all_pins_values()

    def post(self):
        return {"data": "Sensors list post method"}

class Sensor(Resource):
    def get(self, pin_number):
        return {"data": "Get value of one sensor", "pin_number": pin_number}

    def post(self):
        return {"data": "Sensor post method"}


# Initialize RESTful API using Flask
app = Flask(__name__)
api = Api(app)
api.add_resource(SensorsList, "/sensors")
api.add_resource(Sensor, "/sensor/<int:pin_number>")


if __name__ == "__main__":
    app.run(debug=True)
    # TODO: delete debug=True after finish testing
