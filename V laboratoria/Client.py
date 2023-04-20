class Client:
    Clients = {}

    def __init__(self, firstName, surName, address):
        Client.Clients[surName] = Client.Clients.get(surName, 0) + 1
        self.clientId = surName + Client.Clients.get(surName, 0) + 1
        self.firstName = firstName
        self.surName = surName
        self.address = address

    def __str__(self, firstName, surName, address):
        return f"{firstName} {surName}, {address}"

person1 = Client("Jan", "Kowalski", "Kraków")
print(str(person1))

