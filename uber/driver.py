class Driver:
    
    def __init__(self, name, rating = 0.0, driverId = 0, is_Online = False):
        self.name = name
        self.rating = rating
        self.driverId = driverId
        self.is_Online = is_Online
        
    def acceptRide(self, rideId):
        print(f"The Driver {self.name} accepted the ride")
        
        
if(__name__ == "__main__"):
        d1 = Driver("Ashok", 4.5, 123, False)
        print(d1.name)
        