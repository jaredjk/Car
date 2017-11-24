class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def displayinfo(self):
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        print '{} {} {} {} {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)
    

Car_1 = Car(2000, '35mpg', 'Full', '15mpg')
Car_2 = Car(2000, '5mpg', 'Not Full', '15mpg')
Car_3 = Car(2000, '15mpg', 'Kind of Full', '15mpg')
Car_4 = Car(2000, '25mpg', 'Full', '15mpg')
Car_5 = Car(2000, '45mpg', 'Empty', '15mpg')
Car_6 = Car(20000000, '35mpg', 'Empty', '15mpg')

Car_1.displayinfo()
