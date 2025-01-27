# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Derived class: ElectricVehicle
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Calls Vehicle constructor
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Derived class: GasVehicle
class GasVehicle(Vehicle):
    def __init__(self, brand, model, fuel_capacity):
        super().__init__(brand, model)  # Calls Vehicle constructor
        self.fuel_capacity = fuel_capacity

    def display_info(self):
        super().display_info()
        print(f"Fuel Capacity: {self.fuel_capacity} liters")

# Multiple Inheritance: HybridVehicle
class HybridVehicle(ElectricVehicle, GasVehicle):
    def __init__(self, brand, model, battery_capacity, fuel_capacity):
        ElectricVehicle.__init__(self, brand, model, battery_capacity)  # Call ElectricVehicle constructor
        GasVehicle.__init__(self, brand, model, fuel_capacity)  # Explicitly call GasVehicle constructor

    def display_info(self):
        super().display_info()  # Calls ElectricVehicle's display_info()
        print(f"Fuel Capacity: {self.fuel_capacity} liters")  # Ensures fuel info is displayed

# Create instances of different vehicle types
ev = ElectricVehicle("Tesla", "Model S", 100)
gv = GasVehicle("Ford", "F-150", 80)
hv = HybridVehicle("Toyota", "Prius", 8, 40)

# Display vehicle information
print("Electric Vehicle Info:")
ev.display_info()
print("\nGas Vehicle Info:")
gv.display_info()
print("\nHybrid Vehicle Info:")
hv.display_info()
