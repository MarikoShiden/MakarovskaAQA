class Train:
    def __init__(self, locomotive):
        """
        Initialize Train, define locomotive and list of train cars
        """
        self.locomotive = locomotive
        self.train_cars = []

    def add_train_car(self, car: int):
        """
        Add train cars to train_cars list
        """
        self.train_cars.append(car)

    def __len__(self):
        """
        :return: Number of train cars
        """
        return len(self.train_cars)

    def __str__(self):
        """
        Create a dictionary with data for each new train car
        """
        train_data = {}
        for i, car in enumerate(self.train_cars):
            train_data[f'train car {i + 1}'] = str(car)
        return str(train_data)


class TrainCar:
    def __init__(self, car_num: int, max_passengers=10):
        """
        Initialize TrainCar with such parameters as car number, list of passengers and max number of passengers
        :param car_num: number of a train car
        :param max_passengers: set maximum number of passengers in each train car
        """
        self.car_num = car_num
        self.passengers = []
        self.max_passengers = max_passengers

    def add_passenger(self, passenger_name: str, destination: str, place: int):
        """
        Add passengers with the following parameters:
        :param passenger_name: passenger's name
        :param destination: destination of a passenger
        :param place: place in a train car
        """
        if len(self.passengers) < self.max_passengers:
            self.passengers.append({
                'passenger name': passenger_name,
                'destination': destination,
                'place': place
            })
        else:
            print(f'Train car {self.car_num} is full. Choose other cart for {passenger_name}')

    def __len__(self):
        """
        :return: number of passengers in each train car
        """
        return len(self.passengers)

    def __str__(self):
        """
        Assign passengers to train cars
        :return: information for each train car
        """
        car_data = {'train car': str(self.car_num)}
        for i, passenger in enumerate(self.passengers):
            for key, value in passenger.items():
                car_data[f'{key} {i + 1}'] = value
        return str(car_data)


locomotive = TrainCar(0, 0)
train = Train(locomotive)

train_car1 = TrainCar(1)
train_car2 = TrainCar(2)
train_car3 = TrainCar(3)

train.add_train_car(1)
train.add_train_car(2)
train.add_train_car(3)

train_car1.add_passenger('Pavlo Zibrov', 'Lviv', 1)
train_car1.add_passenger('Stepan Giga', 'Lutsk', 4)
train_car2.add_passenger('Ivo Bobul', 'Zhytomyr', 1)
train_car2.add_passenger('Oksana Bilozir', 'Kyiv', 7)
train_car3.add_passenger('Liliya Sandulesa', 'Dnipro', 2)
train_car3.add_passenger('Svitlana Bilonozhko', 'Odesa', 3)
train_car3.add_passenger('Vitalii Bilonozhko', 'Odesa', 4)


print(train_car1)
print(train_car2)
print(train_car3)
print(train)
