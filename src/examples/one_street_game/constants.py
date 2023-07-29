""" Constants for one street poker example. """


from enum import Enum


class Action(Enum):
    UNSPECIFIED = 0
    CHECK = 1
    FOLD = 2
    CALL = 3
    BET_25 = 4
    BET_50 = 5
    BET_75 = 6
    BET_100 = 7
    BET_150 = 8


class Suit(Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3

    def __str__(self):
        if self == Suit.SPADE:
            return "♠"

        if self == Suit.HEART:
            return "❤️"

        if self == Suit.DIAMOND:
            return "♦"

        return "♣️"


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self):
        if self == Rank.ACE:
            return "A"
        if self == Rank.JACK:
            return "J"
        if self == Rank.QUEEN:
            return "Q"
        if self == Rank.KING:
            return "K"

        return str(self.value)
