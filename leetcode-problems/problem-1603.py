# 1603. Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.available_parks = {
            1:big,
            2:medium,
            3:small
        }        

    def addCar(self, carType: int) -> bool:
        if self.available_parks[carType]:
            self.available_parks[carType] -= 1
            return True
        else:
            return False
