class Car:
    def __init__(self, model, year, max_speed, color, engine_type, horsepower, zero_to_hundred, drivetrain):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.color = color
        self.engine_type = engine_type  # This was likely missing!
        self.horsepower = horsepower
        self.zero_to_hundred = zero_to_hundred
        self.drivetrain = drivetrain


    def drive(self):
        print(f"You Drive a {self.model} which was made in {self.year} and is {self.color} color at max speed of {self.max_speed} km/h")

    def stop(self):
        print(f"You stopped the {self.model} using its high-performance brakes, bringing all {self.horsepower} horsepower to a halt")

    def jump(self):
        print(f"You Jump the {self.model} from 0 to 100 km/h in just {self.zero_to_hundred} seconds using its {self.drivetrain} system")



    