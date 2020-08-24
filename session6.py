def generate_deck_single_expression(vals: 'list of strings',
                                    suits: 'list of strings') -> 'list of tuples containing the deck':
    """
    Combine the vals and the suits to form a complete deck using just a single expression!
    :param vals: list of strings
    :param suits: list of strings
    :return: list of tuples containing the entire deck
    """

    if isinstance(vals, list):
        if False in [isinstance(x, str) for x in vals]:
            raise ValueError('list elements must be strings')
    if isinstance(suits, list):
        if False in [isinstance(x, str) for x in suits]:
            raise ValueError('list elements must be strings')

    deck = lambda vals, suits: [(x, y) for x in vals for y in suits]
    return deck(vals, suits)


def generate_deck_function(vals: 'list of strings',
                           suits: 'list of strings') -> 'list of tuples containing the deck':
    """
    Combine the vals and the suits to form a complete deck without using lambda, zip or map!
    :param vals: list of strings
    :param suits: list of strings
    :return: list of tuples containing the entire deck
    """

    if isinstance(vals, list):
        if False in [isinstance(x, str) for x in vals]:
            raise ValueError('list elements must be strings')
    if isinstance(suits, list):
        if False in [isinstance(x, str) for x in suits]:
            raise ValueError('list elements must be strings')

    deck = []
    for x in vals:
        for y in suits:
            deck.append((x, y))
    return deck


def declare_winner(set_a: 'list of tuples', set_b: 'list of tuples') -> 'int value indication the winner':
    """
    When given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per
    player) (1 deck of cards only), (2 players only), can identify who won the game of poker.
    :param set_a: list of tuples containing 3, 4 or 5 cards from the deck
    :param set_b: list of tuples containing the 3, 4, or 5 cards from the deck
    :return: 0 if there is a draw, 1 if B is the winner, -1 if A is the winner.
    """
    # todo: check lengths of both sets to be equal
    if len(set_a) != len(set_b):
        raise ValueError('Both sets must of same size')

    if len(set_a) not in {3, 4, 5}:
        raise ValueError('Set size must be in {3, 4, 5}')

    a_rank = determine_set_rank(set_a)
    b_rank = determine_set_rank(set_b)

    if a_rank < b_rank:
        return -1
    elif b_rank < a_rank:
        return 1
    else:
        return 0


def determine_set_rank(poker_set: 'list of tuples') -> 'int value indicating the set rank':
    """
    Determine the rank (a number between and including 1 and 10), for the given set of poker cards.
    Rank 1: A, K, Q, J, 10 (of same suit) - Royal Flush
    Rank 2: 10, 9, 8, 7, 6 (of same suit) - Straight Flush
    Rank 3: Four of a kind (kind - same value)
    Rank 4: Three of one kind, and two of other kind - Full house
    Rank 5: Flush
    Rank 6: Straight (five sequential values)
    Rank 7: Three of a kind
    Rank 8: Two pair
    Rank 9: One pair
    Rank 10:

    :param poker_set: A set of 3, 4 or 5 cards
    :return: int (rank of the set)
    """

    # todo:
    if isinstance(poker_set, list):
        if False in [isinstance(x, tuple) for x in poker_set]:
            raise ValueError('list elements must be tuples')
        if set([len(x) for x in poker_set]) != {2}:
            raise ValueError('tuple must be of size 2')


    # todo: test the elements of the poker set to be valid
    # todo: test the length of the poker set
    # todo: test the type of poker_set

    if not 3 <= len(poker_set) <=5:
        raise ValueError('Expected a set of length 3, 4 or 5 but found {}'.format(len(poker_set)))

    all_vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    all_suits = ['spades', 'clubs', 'hearts', 'diamonds']
    vals = list(map(lambda x: x[0], poker_set))
    suits = list(map(lambda x: x[1], poker_set))

    if not set(all_vals).issuperset(vals):
        raise ValueError('Invalid value')
    if not set(all_suits).issuperset(suits):
        raise ValueError('Invalid suit')

    set_size = len(poker_set)

    # 1: Royal Flush
    if len(set(suits)) == 1:
        if {*all_vals[-set_size:]} == set(vals):
            return 1

    # 2: Straight Flush
    if len(set(suits)) == 1:
        element_indices = list(map(lambda x: all_vals.index(x), sorted(vals, key=lambda x: all_vals.index(x))))
        if element_indices[-1] - element_indices[0] + 1 == set_size:
            return 2

    # 3: Four of a kind
    if 4 in [vals.count(x) for x in vals]:
        return 3

    # 4: Full House
    if 3 in [vals.count(x) for x in vals]:
        if set_size == 5:
            if 2 in [vals.count(x) for x in vals]:
                return 4
        else:
            return 4

    # 5: Flush
    if len(set(suits)) == 1:
        return 5

    # 6: Straight
    element_indices = list(map(lambda x: all_vals.index(x), sorted(vals, key=lambda x: all_vals.index(x))))
    if element_indices[-1] - element_indices[0] + 1 == set_size:
        return 6

    # 7: Three of a kind
    if 3 in [vals.count(x) for x in vals]:
        return 7

    # 8: Two pair
    if list(sorted([vals.count(x) for x in vals])).count(2) == 4:
        return 8

    # 9: One pair
    if list(sorted([vals.count(x) for x in vals])).count(2) == 2:
        return 9

    return 10


if __name__ == '__main__':
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    deck = generate_deck_single_expression(vals, suits)
    deck = generate_deck_function(vals, suits)

    a1 = determine_set_rank([('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')])
    a2 = determine_set_rank([('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts')])
    a3 = determine_set_rank([('6', 'hearts'), ('6', 'diamonds'), ('6', 'clubs'), ('6', 'spades')])
    a4 = determine_set_rank([('2', 'hearts'), ('2', 'diamonds'), ('2', 'clubs'), ('ace', 'diamonds'), ('ace', 'clubs')])
    a5 = determine_set_rank([('7', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('ace', 'hearts'), ('5', 'hearts')])
    a6 = determine_set_rank([('jack', 'spades'), ('queen', 'hearts'), ('king', 'hearts')])
    a7 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('jack', 'clubs'), ('2', 'clubs'), ('5', 'clubs')])
    a8 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('3', 'hearts'), ('3', 'clubs')])
    a9 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('2', 'hearts'), ('3', 'clubs')])
    a10 = determine_set_rank([('queen', 'spades'), ('jack', 'hearts'), ('2', 'hearts'), ('3', 'clubs')])

    wa = declare_winner(set_a=[('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')],
                        set_b=[('queen', 'spades'), ('jack', 'hearts'), ('2', 'hearts')])
    wb = declare_winner(set_b=[('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')],
                        set_a=[('queen', 'spades'), ('jack', 'hearts'), ('2', 'hearts')])
    w0 = declare_winner(set_a=[('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')],
                        set_b=[('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')])

    pass