import random
import time

poolheroes = ["Enigma", ""]
flag = True
a = 0


class Hero:
    """Как создать персонажа. Туториал."""

    critical_damage = random.randint(30, 100)
    uklonenie = random.randint(5, 20)
    skilldamagebonus = random.randint(30, 50)
    DAMAGE = 100
    RELOAD_FLAG = True

    def __init__(self,
                 name: str,

                 skill: str,
                 damage: int,
                 skilldamage: int,
                 reload: int,

                 hp: int):
        self.name = name

        self.skill = skill
        self.damage = damage
        self.skilldamage = skilldamage
        self.reload = reload

        self.hp = hp

    def info(self):
        print(f'Мое имя - {self.name} \n'
              f'Мой скилл - {self.skill}, \n'

              f'Мое здоровье {self.hp}')

    def fight(self):
        if self.RELOAD_FLAG:
            print(f'Атакой нанесено {self.damage + self.critical_damage - self.uklonenie} урона,\n'
                  f'Способность {self.skill} нанесла {self.skilldamage + self.skilldamagebonus} урона, перезарядка {self.reload}, \n'
                  f'Осталось {self.hp - (self.damage + self.critical_damage + self.skilldamage)}')

        else:
            for x in range(self.reload):
                print(f'Атакой нанесено {self.damage + self.critical_damage - self.uklonenie} урона,\n'
                      f'Способность {self.skill} нанесла 0 урона, перезарядка {self.reload}, \n'
                      f'Осталось {self.hp - (self.damage + self.critical_damage)}')


class Intellect(Hero):
    skilldamagebonus = random.randint(20, 35)


class Lovkost(Hero):
    uklonenie = random.randint(20, 35)


class Sila(Hero):
    critical_damage = random.randint(60, 150)


class Enigma(Hero):
    skilldamagebonus = random.randint(50, 65)


def training(hero):
    print('Приветствую тебя на тренировочной арене\n'
          'Здесь ты можешь отточить свои навыки и научиться герою\n'
          'Для атаки по манекену нажми "a"')
    action = None
    while action != "skip":
        action = input('Напишите "a" для атаки')
        maneken = 10000
        if action == 'a':
            print(f'{int(maneken) - int(hero.skilldamage) - int(hero.damage) - int(Intellect.skilldamagebonus)}')
            hero.RELOAD_FLAG = False
            print('Reload')
            time.sleep(2)
            hero.RELOAD_FLAG = True
            print('Reloaded')


def choose_character() -> Hero:
    c = {"Enigma": Intellect
         }
    character = input('Здравствуй, ты попал в игру Dota 2 python edition\n'
                      f'Вот полный список героев: {poolheroes}\n'
                      'Выбирай любого, просто написав его имя, сохраняя орфографию и пунктуацию\n'
                      'Краткая сводка по атрибутам:\n'
                      'Интеллект - дает прирост к урону от заклинаний\n'
                      'Ловкость - дает больший шанс уклонения\n'
                      'Сила - больший урон\n')

    name = input('Ваше имя')
    skill = input('Скилл')
    damage = input('Урон')
    skilldamage = input('Урон скилла')
    reload = input('Перезарядка')
    hp = input('Здоровье')
    return c[character](name, skill, damage, skilldamage, reload, hp)


enigma = Intellect('Енигма', 'Black Hole', 60, 100, 3, 600)

if __name__ == '__main__':
    hero = choose_character()
    training(hero)
