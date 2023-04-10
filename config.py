from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI

CONFIG1 = {"name1": "evan", "name2": "viola", "pile_str": "AKKQQQJJJJ"}
CONFIG2 = {"name1": "evan", "name2": "viola", "pile_str": "AAAAKKKKQQQQJJJJ"}


def game_factory(from_dict: dict) -> CardGame:
    cli = CLI()
    player1 = Player(from_dict["name1"])
    player2 = Player(from_dict["name2"])
    scoreboard = ScoreBoard()
    scoreboard.register(player1.name)
    scoreboard.register(player2.name)
    game_pile = Pile.from_str(seed_str=from_dict["pile_str"], name="game")
    discard_pile = Pile("discard")
    return CardGame(
        player=player1,
        other_player=player2,
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )
