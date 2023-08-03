from random import shuffle
from typing import List, Tuple, AnyStr
import data_rus

def create_deck_of_cards() -> List[Tuple[AnyStr, AnyStr]]:
    deck_of_cards = data_rus.deck_of_cards
    shuffle(deck_of_cards)
    return deck_of_cards


def give_cards_to_player(deck_of_cards: List[Tuple[AnyStr, AnyStr]]) -> List[Tuple[AnyStr, AnyStr]] and List[Tuple[AnyStr, AnyStr]]:
    """delete deck for 2 parts: to player and to deck

    Args:
        deck_of_cards (List[Tuple[AnyStr, AnyStr]]): deck of cards

    Returns:
        List[Tuple[AnyStr, AnyStr]] and List[Tuple[AnyStr, AnyStr]]: player cards and deck
    """
    return deck_of_cards[:6], deck_of_cards[6:]


def join_cards(cards: List[Tuple[AnyStr, AnyStr]]) -> AnyStr:
    """Join cards to pretty string

    Args:
        cards (List[Tuple[AnyStr, AnyStr]]): array of cards

    Returns:
        AnyStr: pretty string
    """
    pretty_cards = ''
    for card in cards:
        pretty_cards += ' '.join(card)
        pretty_cards += ', '
    return pretty_cards


def new_step(deck_of_cards: List[Tuple[AnyStr, AnyStr]]) -> None:
    pass



def main() -> None:
    deck_of_cards = create_deck_of_cards()
    player_cards, deck_of_cards = give_cards_to_player(deck_of_cards)
    print(player_cards)


main()