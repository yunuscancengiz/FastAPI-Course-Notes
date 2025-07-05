from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *


def battle(hero: Hero, enemy: Enemy):
    enemy.talk()
    
    while hero.health_points > 0 and enemy.health_points > 0:
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    if enemy.health_points > 0:
        print(f'Hero wins.')
    else:
        print(f'{enemy.get_type_of_enemy()} wins.')


zombie = Zombie(health_points=10, attack_damage=1)
hero = Hero(health_points=10, attack_damage=1)
weapon = Weapon(weapon_type='Sword', attack_increase=5)
hero.weapon = weapon
hero.equip_weapon()

battle(hero=hero, enemy=zombie)
