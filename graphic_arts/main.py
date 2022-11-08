from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Воитель наносит атаку."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name}  нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')


# noinspection SpellCheckingInspection
def defence(char_name: str, char_class: str) -> str:
    """Воитель защищается."""
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} ед. урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона'
    if char_class == 'healer':
        return f'{char_name}  блокировал {10 + randint(2, 5)} ед. урона'


# noinspection SpellCheckingInspection
def special(char_name: str, char_class: str) -> str:
    """Воитель применил специальное умение."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return f'{char_name}  применил специальное умение «Атака {5 + 40}»'
    if char_class == 'healer':
        return (f'{char_name}  применил специальное умение '
                f'«Защита {10 + 30}»')


# noinspection PyTypeChecker,SpellCheckingInspection
def start_training(char_name: str, char_class: str) -> str:
    """ты Воитель — великий мастер ближнего боя."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


# noinspection PyTypeChecker,SpellCheckingInspection
def choice_char_class() -> str:
    """Введите пожалуйсто название персонажа."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


# noinspection SpellCheckingInspection
def main():
    """Выбирай на выбор кем ты будешь."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()