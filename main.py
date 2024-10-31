import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\nИгра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer_turn()

        self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"{self.computer.name} здоровья осталось: {self.computer.health}\n")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"{self.player.name} здоровья осталось: {self.player.health}\n")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    game = Game()
    game.start()



