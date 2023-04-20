from Client import Client
#tylko raz można wypożyczy auto, a póżniej tylko kupić

class Cars:
    brands = {} #{fiat1: [carID, clientID, fiat, sellPrice]}

    def __init__(self, carId, brand, sellPrice, rentPrice, rentStartDay, rentEndDay):
        Cars.brands[brand] = Cars.brands.get(brand, 0) + 1
        self.brand = brand
        self.carId = carId
        self.clientId = Client.clientId
        self.sellPrice = sellPrice
        self.rentPrice = rentPrice
        self.rentStartDay = rentStartDay
        self.rentEndDay = rentEndDay

    