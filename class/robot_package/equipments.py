class AirPurifier:
    """
    Represents an air purifying equipment that can be equipped to the robot.

    Attributes:
    - is_running (bool): Indicates whether the air purifier is running.

    Methods:
    - start(): Starts the air purifier.
    - stop(): Stops the air purifier.
    """

    def __init__(self):
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            return "Air purifier started!"
        return "Air purifier is already running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Air purifier stopped!"
        return "Air purifier is not running."