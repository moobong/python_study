class Actuator:
    """
    Represents an actuator that drives the robot's movements or actions.

    Attributes:
    - actuator_type (str): The type of the actuator (e.g., "arm", "wheel").

    Methods:
    - activate(command): Activates the actuator based on the given command.
    """
    
    def __init__(self, actuator_type):
        self.actuator_type = actuator_type

    def activate(self, command):
        return f"{self.actuator_type} activated with command: {command}"