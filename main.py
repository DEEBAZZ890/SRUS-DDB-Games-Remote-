from app.player import Player
from app.player_list import PlayerList


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    p1 = Player("20069321", "Daniel")  # This creates an instance of the player object
    print(f"{p1}")  # This line prints that object to ensure the __str__ method is working correctly


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    PlayerList.is_empty()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
