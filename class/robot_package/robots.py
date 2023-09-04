from .equipments import AirPurifier

class Robot:
    """
    Main class representing the robot, integrating various subsystems and functionalities.

    Attributes:
    - name (str): The name of the robot.
    - sensor (Sensor): The sensor subsystem of the robot.
    ... (Other attributes for each subsystem)

    Methods:
    - move(x, y): Moves the robot to a specified position.
    ... (Other methods corresponding to robot functionalities)
    """

    def __init__(self, name, sensor, actuator, battery, controller, comm_module, nav_system, ui, learning_module):
        self.name = name
        self.sensor = sensor
        self.actuator = actuator
        self.battery = battery
        self.controller = controller
        self.comm_module = comm_module
        self.nav_system = nav_system
        self.ui = ui
        self.learning_module = learning_module

    def move(self, x, y):
        if self.battery.use(10) <= 0:
            return "Battery low! Can't move."
        self.actuator.activate("move")
        return self.nav_system.navigate(x, y)

    def sense(self):
        return self.sensor.sense()

    def communicate(self, message):
        return self.comm_module.send(message)

    def execute(self, command):
        return self.controller.execute(command)

    def interact(self, user_input):
        return self.ui.interact(user_input)

    def learn_from_data(self, data):
        return self.learning_module.learn(data)

    def charge_battery(self):
        self.battery.charge()
        return "Battery fully charged!"

    def display_status(self):
        return {
            "Name": self.name,
            "Battery": f"{self.battery.current_charge}/{self.battery.capacity}",
            "Position": self.nav_system.position,
            "Processor": self.controller.processor,
            "Memory": f"{self.controller.memory['used']}/{self.controller.memory['size']}",
            "OS": self.controller.os
        }




class ServiceRobot(Robot):  # 위에서 정의한 Robot 클래스를 상속합니다.
    """
    Extended robot class designed to provide specific services, such as air purification.

    Attributes:
    - equipment (object): The additional equipment equipped to the robot.

    Methods:
    - activate_equipment(): Activates the equipped equipment.
    - deactivate_equipment(): Deactivates the equipped equipment.
    """

    def __init__(self, name, sensor, actuator, battery, controller, comm_module, nav_system, ui, learning_module, equipment):
        super().__init__(name, sensor, actuator, battery, controller, comm_module, nav_system, ui, learning_module)
        self.equipment = equipment

    def activate_equipment(self):
        if isinstance(self.equipment, AirPurifier):
            return self.equipment.start()

    def deactivate_equipment(self):
        if isinstance(self.equipment, AirPurifier):
            return self.equipment.stop()
