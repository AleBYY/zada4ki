# 1)
# def card_number(number):
#     if type(number) is int:
#         str_number = str(number)
#         if len(str_number) == 16:
#             return '*' * 12 + str_number[-4:]
#         else:
#             print('Неверно введена карта')
#             exit()
#     elif len(number) == 16:
#         return '*' * 12 + number[-4:]
#     else:
#         print('Неверно введена карта')
#         exit()
# print(card_number(4255190104160802))
#

# 2
# def palindrom(word):
#     word = word.replace(' ', '')
#     if word.lower() == word.lower()[::-1]:
#         return 'Палиндром'
#     else:
#         return 'Не палиндром'
# print(palindrom('А роза упала на лапу Азора'))


# 3
class Tomato:
    states = {0: 'расток', 1: 'куст', 2: 'зелёный томаты', 3: 'красный томаты'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Томат {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(1, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = 0


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает в данный момент')
        self._plant.grow_all()
        print('Садовник закончил работу')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Плоды ещё не созрели')

    @staticmethod
    def knowledge_base():
        print('Многие согласятся что опыт в садоводстве приходит с годами, а так же путем проб и ошибок.')
        print(
            'Чем опытнее садовод тем лучше его урожай. У каждого садовода и огородника есть свои секреты, которыми он использует и делиться с другими садоводами.')


Gardener.knowledge_base()
tomato = TomatoBush(3)
gardener = Gardener('Aleksei', tomato)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
