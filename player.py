from __future__ import annotations

from card import Card
import logging


class Player:
    hand: Card | None = None

    def __init__(self, name) -> None:
        self._name = name.strip().capitalize()

    @classmethod
    def from_names(cls, names: list[str]) -> tuple[Player]:
        return tuple(cls(name) for name in names)

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_holding(self) -> bool:
        return bool(self.hand)

    def discard(self) -> Card:
        if not self.is_holding:
            raise Exception(f"{self.name} has no card to discard.")
        discarded = self.hand
        self.hand = None
        logging.info(f"{self.name} discarded {discarded}.")
        return discarded

    def hold(self, card: Card) -> None:
        if self.is_holding:
            raise Exception(
                f"{self.name} could not pick up {card} -> already holds {self.hand}."
            )
        self.hand = card
        logging.info(f"{self.name} picked up {card}.")

    def __str__(self):
        if not self.is_holding:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.hand}."


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    player = Player("evan")
    player.name  # "Evan"
    player.hold(Card.Ace)
    player.is_holding  # True
    player.discard()
    player.is_holding  # False
