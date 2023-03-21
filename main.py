import random
from translate import Translator


class Card:
    def __init__(self, name):  # Инициализируем класс с параметром Имя игрока////
        self.name = name  # Установка имени игрока в свойство name
        self.card = self.generate_card()  # Вызов метода генерации карты и сохранение её в свойство card

    def generate_card(self):  # Метод генерации игровой карты
        card = []  # Создаем пустой список для карточки
        for i in range(3):  # Цикл по 3 строкам карты
            row = []  # Создаем пустой список для строки карточки
            for j in range(9):  # Цикл по 9 столбцам карты
                if j == 0:  # Если это первый столбец,
                    num = random.randint(1, 9)  # выбираем случайное число от 1 до 9
                elif j == 8:  # Если это последний столбец,
                    num = random.randint(80, 90)  # выбираем случайное число от 80 до 90
                else:  # Иначе
                    num = random.randint(j * 10 + 1, j * 10 + 10)  # выбираем случайное число от j*10+1 до j*10+10.
                row.append(num)  # Добавляем число в текущую строку
            card.append(row)  # Добавляем строку в карточку
        return card  # Возвращаем созданную карту

    def print_card(self):  # Выводим карточку игрока на экран
        print(self.name + "s' card:")  # Выводим имя игрока
        print('-------------------')  # Разделительная линия/
        for row in self.card:  # Цикл по каждой строке в карточке
            for num in row:  # Цикл по каждому числу в строке
                print('{:2s}'.format(str(num)), end=" ")  # Выводим строку шириной в 2 символа
            print('')  # Переход на новую строку
        print('-------------------')

    def mark_number(self, number):  # Закрашиваем число в карточке
        for i in range(3):
            for j in range(9):
                if self.card[i][j] == number:  # Если число в карточке совпадаем с числом, которое выпало рандомно
                    self.card[i][j] = 'X'  # Это число меняется на Х

    def check_card(self):  # Проверяем все ли числа закрашены
        for row in self.card:
            for num in row:
                if num != 'X':  # Если на карточке есть неотмеченные числа
                    return False  # Возвращаем False
        return True  # Иначе возвращаем True


class Game:
    def __init__(self, players):  # Инициализируем класс с параметрами игроки
        self.players = players  # Список игроков
        self.numbers = list(range(1, 91))  # Список чисел для игры
        self.called_numbers = []  # Список готовых чисел
        self.game_over = False  # Когда игра заканчивается переменная, становится True

    def play(self):
        for player in self.players:
            player.print_card()  # Выводим карточки на экран перед стартом игры, начальные карточки
        while not self.game_over:  # Пока игра не закончится цикл продолжается
            self.call_number()  # Показываем номер
            for player in self.players:  # Перебираем всех игроков и выводим их карточки
                player.print_card()
                if player.check_card():  # Если карточка игрока заполнена 'X', объявляем его победителем и заканчиваем игру
                    print(player.name + ' Победитель!!!')
                    self.game_over = True
                    break

    def call_number(self):
        if not self.numbers:  # Проверка на пустой список, если пустой выходим из функции
            return
        number = random.choice(self.numbers)  # Выбираем случайный элемент из списка
        self.numbers.remove(number)  # Удаляем выбранный элемент из списка
        self.called_numbers.append(number)  # Добавляем выбранный элемент в список
        print('Номер боченка: ', number)  # Выводим на экран номер, который был выбран
        for player in self.players:
            player.mark_number(number)  # Помечаем номер на его карточке 'X'


class HumanPlayer:
    def __init__(self, name):  # Инициализация класса с параметром имя игрока и создает карту для игрока
        self.name = name  # устанавливаем имя игрока
        self.card = Card(name)  # Создаем экземпляр класса Card с именем игрока и сохраняем его в свойстве "card"

    def print_card(self):  # Метод вывода карточки игрока на экран
        self.card.print_card()

    def mark_number(self, number):  # Метод для пометки числа на карточке игрока
        self.card.mark_number(number)

    def check_card(self):  # Метод для проверки наличия выигрышной комбинации на карточке игрока
        return self.card.check_card()


class ComputerPlayer:
    def __init__(self, name):
        self.name = name
        self.card = Card(name)

    def print_card(self):
        self.card.print_card()

    def mark_number(self, number):
        self.card.mark_number(number)

    def check_card(self):
        return self.card.check_card()


def main():
    human_players = int(input('Введите количество игроков (реальных): '))  # Запрашиваем количество реальных игроков
    computer_players = int(input('Введите количество игроков (бот): '))  # Запрашиваем количество игроков-ботов
    players = []  # Создаем список игроков
    for i in range(human_players):  # Цикл для создания экземпляров реальных игроков
        translator = Translator(from_lang='ru', to_lang='en')  # Создаем экземпляр переводчика
        name = translator.translate(input('Введите имя игрока (реального) {}: '.format(
            i + 1)))  # Запрашиваем имя реального игрока и переводим его на английский язык с использованием API-переводчика
        player = HumanPlayer(
            name)  # Создаем экземпляр реального игрока с указанным именем и добавляем его в список игроков.
        players.append(player)
    for i in range(computer_players):  # Цикл для создания экземпляров игроков-ботов
        player = ComputerPlayer('Computer {}'.format(
            i + 1))  # Создаем экземпляр игрока-бота с указанным именем и добавляем его в список игроков.
        players.append(player)
    game = Game(players)  # Создаем экземпляр игры с использованием списка игроков и запускаем игру.
    game.play()


if __name__ == '__main__':  # Запускаем функцию main(), если модуль запускается как программа, а не импортируется как модуль
    main()
