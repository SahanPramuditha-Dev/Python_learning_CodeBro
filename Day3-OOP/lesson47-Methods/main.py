from car import Car  #in here we import the Car class from car.py file

# Instantiating with high-fidelity automotive data
car1 = Car(
    model="Ford Mustang Dark Horse",
    year=2025,
    max_speed=267,
    color="Vapor Blue",
    engine_type="5.0L Coyote V8",
    horsepower=500,
    zero_to_hundred=3.7,
    drivetrain="RWD"
)

car2 = Car(
    model="Chevrolet Corvette ZR1",
    year=2025,
    max_speed=346,
    color="Competition Yellow",
    engine_type="5.5L LT7 Twin-Turbo V8",
    horsepower=1064,
    zero_to_hundred=2.5,
    drivetrain="RWD"
)

car3 = Car(
    model="Ferrari SF90 XX Stradale",
    year=2026,
    max_speed=320,
    color="Rosso Corsa",
    engine_type="4.0L V8 Plug-in Hybrid",
    horsepower=1016,
    zero_to_hundred=2.3,
    drivetrain="AWD"
)

car1.drive()
car2.stop()
car3.jump()

print("\n-----------------------------\n")