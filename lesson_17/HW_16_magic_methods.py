import pprint
class Train:
    def __init__(self, departure, destination, number):
        self.departure = departure
        self.destination = destination
        self.number = number
        self.traincars = {}

    def __len__(self):
        return len(self.traincars)

    def __setitem__(self, key, value):
        self.traincars[key] = value

    def __str__(self):
        return (f"Train number {self.number} {self.departure}-{self.destination}, {self.traincars}")


class TrainCar:
    def __init__(self, number):
        self.number = number
        self.limit_of_places = 32
        self.places = {}

    def __len__(self):
        return len(self.places)

    def __str__(self):
        return f"{self.places}"

    def __setitem__(self, key, value):
        self.places[key] = value
class Passenger:
    def __init__(self, passanger_name, place, departure, destination):
        self.passanger_name = passanger_name
        self.place = place
        self.departure = departure
        self.destination = destination

train1 = Train('London', 'Birmingham', '342')
traincar1 = TrainCar('1')
traincar2 = TrainCar('2')
passenger1 = Passenger('John Dow', '1', 'London', 'Luton')
passenger2 = Passenger('Joe Rogan', '2', 'Northampton', 'Birmingham')
passenger3 = Passenger('Joe Biden', '7', 'Watford', 'Coventry')
train1[f'Train car #{traincar1.number}'] = traincar1.places
train1[f'Train car #{traincar2.number}'] = traincar2.places
traincar1[f'Place {passenger1.place}'] = {'place': passenger1.place,'passenger_name': passenger1.passanger_name, 'departure': passenger1.departure, 'destination': passenger1.destination}
traincar2[f'Place {passenger2.place}'] = {'place': passenger2.place,'passenger_name': passenger2.passanger_name, 'departure': passenger2.departure, 'destination': passenger2.destination}
traincar1[f'Place {passenger3.place}'] = {'place': passenger3.place,'passenger_name': passenger3.passanger_name, 'departure': passenger3.departure, 'destination': passenger3.destination}

pprint.pprint(train1.traincars)
print(f"Number of train cars: {len(train1)}")
print(f"Number of passenger in train car #{traincar1.number}: {len(traincar1)}")
