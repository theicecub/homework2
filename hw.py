class familyMember():
    def __init__(self, name):
        self.name = name

class familyHome:
    def __init__(self, address, rooms):
        self.address = address
        self.rooms = rooms
        self.members = []
    
    def add_members(self, human):
        self.members.append(human)

    def show_homeinfo(self):
        if self.members:
            print(f"You have a family and your house is at the {self.address} and have {self.rooms} rooms \n Your family members is:")
            for i in self.members:    
                print(f" {i.name}")
        else:
            print(f"You don't have a family, but your house is at the {self.address} and have {self.rooms} rooms")

human1=familyMember("Abylaikhan")
human2=familyMember("Asylkhan")
human3=familyMember("Aisulu")
human4=familyMember("Ainur") #this is not my family member names, only mine

Highvill = familyHome("Baitursinuly St. 6", 5) #random address, not mine

Highvill.add_members(human1)
Highvill.add_members(human2)
Highvill.add_members(human3)
Highvill.add_members(human4)

Highvill.show_homeinfo()