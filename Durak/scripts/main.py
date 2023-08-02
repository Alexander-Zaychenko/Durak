from random import shuffle
from typing import List, Tuple, AnyStr

def create_deck_of_cards() -> List[Tuple[AnyStr, AnyStr]]:
    deck_of_cards = [
# heart
        ('6', 'heart'),
        ('7', 'heart'),
        ('8', 'heart'),
        ('9', 'heart'),
        ('10', 'heart'),
        ('J', 'heart'),
        ('Q', 'heart'),
        ('K', 'heart'),
        ('A', 'heart'),
# Diamond
        ('6', 'diamond'),
        ('7', 'diamond'),
        ('8', 'diamond'),
        ('9', 'diamond'),
        ('10', 'diamond'),
        ('J', 'diamond'),
        ('Q', 'diamond'),
        ('K', 'diamond'),
        ('A', 'diamond'),
# Club
        ('6', 'club'),
        ('7', 'club'),
        ('8', 'club'),
        ('9', 'club'),
        ('10', 'club'),
        ('J', 'club'),
        ('Q', 'club'),
        ('K', 'club'),
        ('A', 'club'),
# Spade
        ('6', 'spade'),
        ('7', 'spade'),
        ('8', 'spade'),
        ('9', 'spade'),
        ('10', 'spade'),
        ('J', 'spade'),
        ('Q', 'spade'),
        ('K', 'spade'),
        ('A', 'spade'),
    ]
    shuffle(deck_of_cards)
    return deck_of_cards


def give_cards_to_player(deck_of_cards: List[Tuple[AnyStr, AnyStr]]) -> List[Tuple[AnyStr, AnyStr]]:
    return deck_of_cards[0:6]


def join_cards(cards: List[Tuple[AnyStr, AnyStr]]) -> List[Tuple[AnyStr, AnyStr]]:
    pretty_cards = ''
    for card in cards:
        pretty_cards += ' '.join(card)
        pretty_cards += ', '
    return pretty_cards


def main() -> None:
    deck_of_cards = create_deck_of_cards()
    player_cards = join_cards(give_cards_to_player(deck_of_cards))
