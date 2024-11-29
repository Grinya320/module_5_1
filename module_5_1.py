class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_flor):
        for i in range(1, new_flor + 1):
            if 1 <=new_flor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Горный воздух', 20)
h2 = House('Хостел "Светлана"', 3)
h1.go_to(16)
h2.go_to(6)