import time
import random

class Sensors:
    Readings = 0

    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        Sensors.Readings += 1

    def read_value(self):
        return f"We are reading the {self.name} values............"

class TemperatureSensor(Sensors):
    def __init__(self, name, unit, temps):
        super().__init__(name, unit)
        self.temps = temps

    def read_value(self):
        change = random.uniform(-0.5, 0.5)
        self.temps += change
        self.temps = max(20, min(50, self.temps))  # clamp
        return f"The '{self.name}' measures {self.temps:.2f}{self.unit} temperature value..........."

    def display(self):
        return f"Sensor name: '{self.name}' (Temperature sensor) | Current Reading: {self.temps:.2f} {self.unit}"

class HeartRateSensor(Sensors):
    def __init__(self, name, unit, rates):
        super().__init__(name, unit)
        self.rates = rates

    def read_value(self):
        change = random.randint(-5, 5)
        self.rates += change
        self.rates = max(60, min(100, self.rates))  # clamp
        return f"The '{self.name}' measures {self.rates} {self.unit} heart rate value........"

    def display(self):
        return f"Sensor name: '{self.name}' (Heart rate sensor) | Current Reading: {self.rates} {self.unit}"

def sensor_display():
    print("Initializing sensors...\n")
    time.sleep(1)

    Sensortemp1 = TemperatureSensor("TMP36", "°C", temps=random.randint(20, 30))
    Sensorheart1 = HeartRateSensor("Pulse sensor(KY-039)", "bpm", rates=random.randint(70, 90))
    Sensortemp2 = TemperatureSensor("DS18B20", "°C", temps=random.randint(20, 30))
    Sensorheart2 = HeartRateSensor("MAX30100", "bpm", rates=random.randint(70, 90))

    sensors = [Sensortemp1, Sensorheart1, Sensortemp2, Sensorheart2]

    try:
        cycle = 1
        while True:
            print(f"\n---- Cycle {cycle} ----")
            for sensor in sensors:
                print(sensor.read_value())
            cycle += 1
            time.sleep(1)  # wait before next reading
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")
        print(f"\nFinal readings from {Sensors.Readings} sensors:")
        for sensor in sensors:
            print(sensor.display())

sensor_display()
