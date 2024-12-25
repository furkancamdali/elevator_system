""""
Furkan Camdali
Sevin Hatice Yagci 

                Base Elevator class simulating a parking area elevator system.
                Handles basic elevator operations such as floor requests, movement, and emergency brake functionality.
"""

class Elevator: 
    def __init__(self, max_floor):
        self.current_floor = 1  # Initially at the lobby
        self.direction = "stopped"  # Elevator starts stationary
        self.max_floor = max_floor  # Maximum number of floors
        self.requests = []  # Stores floor requests
        self.emergency_brake = False  # Emergency brake status

    def call_elevator(self, floor, direction):
        """Handles corridor calls."""
        if floor < 1 or floor > self.max_floor:
            print("Invalid floor number.")
            return
        if (floor == 1 and direction != "up") or (floor == self.max_floor and direction != "down"):
            print("Invalid direction call.")
            return
        self.requests.append((floor, direction))
        print(f"Call received for floor {floor} to go {direction}.")

    def select_floor(self, floor):
        """Handles floor selection from inside the elevator."""
        if floor < 1 or floor > self.max_floor:
            print("Invalid floor selection.")
            return
        self.requests.append((floor, None))
        print(f"Floor {floor} selected.")

    def apply_emergency_brake(self):
        """Triggers the emergency brake."""
        print("Emergency brake activated! Elevator is stopping...")
        self.emergency_brake = True
        self.direction = "stopped"

    def reset_emergency_brake(self):
        """Resets the emergency brake."""
        print("Emergency brake reset. Elevator can now move.")
        self.emergency_brake = False

    def move(self):
        """Simulates elevator movement."""
        if self.emergency_brake:
            print("Elevator is in emergency mode and cannot move.")
            return

        if not self.requests:
            self.direction = "stopped"
            print("Elevator is idle.")
            return

        next_request = self.requests.pop(0)
        target_floor, target_direction = next_request

        if target_floor > self.current_floor:
            self.direction = "up"
        elif target_floor < self.current_floor:
            self.direction = "down"
        else:
            self.direction = "stopped"

        while self.current_floor != target_floor:
            if self.direction == "up":
                self.current_floor += 1
            elif self.direction == "down":
                self.current_floor -= 1

            print(f"Elevator is at floor {self.current_floor}.")

        print(f"Elevator stopped at floor {self.current_floor}. Doors opening.")
        if target_direction:
            print(f"Elevator direction: {self.direction}")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"-----------------------------")
        result = func(*args, **kwargs)
        print(f"-----------------------------")
        return result
    return wrapper 

class BaseElevator(Elevator):
    def __init__(self, max_floor, elevator_type):
        super().__init__(max_floor)
        self.elevator_type = elevator_type

    def move(self):
        print(f"The {self.elevator_type} elevator is moving...")
        super().move()

class FreightElevator(BaseElevator):
    def __init__(self, max_floor, weight_limit):
        super().__init__(max_floor, "Freight")
        self.weight_limit = weight_limit
    
    @log_decorator  # Makes it easy to log actions using the decorator
    def move(self):
        print("Freight elevator in motion...")
        super().move()


class ServiceElevator(BaseElevator):
    def __init__(self, max_floor):
        super().__init__(max_floor, "Service")

    @log_decorator  # Makes it easy to log actions using the decorator
    def move(self):
        print("Service elevator in motion...")
        super().move()


# Example usage
max_floor = 5
freight_elevator = FreightElevator(max_floor, weight_limit=1000)
service_elevator = ServiceElevator(max_floor)

freight_elevator.call_elevator(3, "up")
freight_elevator.select_floor(4)
freight_elevator.move()
freight_elevator.call_elevator(1, "up")
freight_elevator.move()
freight_elevator.move()
freight_elevator.move()


# Emergency brake example
"""
freight_elevator.apply_emergency_brake()
freight_elevator.move()  # Elevator cannot move
freight_elevator.reset_emergency_brake()
freight_elevator.move()

while freight_elevator.requests:
    freight_elevator.move()

while service_elevator.requests:
    service_elevator.move()
"""
