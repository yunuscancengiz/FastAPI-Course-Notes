class Enemy:
    def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int):
        self.__type_of_enemy = type_of_enemy    # __attribute means it is a private attribute and we need to use getter setters to use it - Encapsulation
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')


    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    
    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage.')

    
    def get_type_of_enemy(self):    # getter for type_of_enemy - Encapsulation
        return self.__type_of_enemy
    

    def set_type_of_enemy(self, type_of_enemy):    # setter for type_of_enemy
        self.__type_of_enemy = type_of_enemy


    def special_attack(self):
        print(f'{self.__type_of_enemy} has no speacial attack.')