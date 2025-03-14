cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) 
print(type(cars))

cars = ["bmw", "audi", "toyota", "subaru"]
cars = [car.title() for car in cars]
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.insert(0,"honda")
cars = [car.title() for car in cars]
print(cars)
