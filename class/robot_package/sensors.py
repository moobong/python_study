class Sensor:
    """
    Represents a sensor used by the robot to gather information from its environment.

    Attributes:
    - sensor_type (str): The type of the sensor (e.g., "camera", "ultrasonic").

    Methods:
    - sense(): Simulates sensing and returns the sensed data.
    """

    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
        self.data = None

    def sense(self):
        return f"Data from {self.sensor_type}"


