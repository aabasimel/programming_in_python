
class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
   
    def __str__(self):
        return f"{self.max_speed} {self.mileage}"
    
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity
        
    def __str__(self):
        return f"{self.max_speed} {self.mileage} {self.capacity}"

print("\n Creating Vehicle objects: ")
car1 = Vehicle(180,50000)
car2 = Vehicle(200,60000)

print(car1)
print (car2)

print("\n Creating Bus objects: ")
bus1 = Bus(180,50000,50)
bus2 = Bus(200,60000,60)

print(bus1)
print (bus2)

print("\nInheritance Relationship:")
print(f"Is bus1 an instance of Bus? {isinstance(bus1, Bus)}")
print(f"Is bus1 an instance of Vehicle? {isinstance(bus1, Vehicle)}")
print(f"Is Bus a subclass of Vehicle? {issubclass(Bus, Vehicle)}")
    
print("\nAccessing inherited attributes:")
print(f"bus1.max_speed = {bus1.max_speed} km/h")
print(f"bus1.mileage = {bus1.mileage} km")
print(f"bus1.capacity = {bus1.capacity} passengers")

