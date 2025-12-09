from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    ranks = []
    suits = []
    for card in hand:
        ranks.append(card.rank.value)
        suits.append(card.suit)
    rank_counts = {}
    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    sorted_counts = sorted(rank_counts.values(), reverse = True)

    suit_counts = {}
    for suit in suits:
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1


    flush = False
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush = True
            flush_suit = suit
            break

    unique_ranks = sorted(list(set(ranks)))

    straight = False
    straight_rank = []

    for i in range(len(unique_ranks)-4):
        if (unique_ranks[i+1] == unique_ranks[i] + 1 and
            unique_ranks[i+2] == unique_ranks[i] + 2 and
            unique_ranks[i+3] == unique_ranks[i] + 3 and
            unique_ranks[i+4] == unique_ranks[i] + 4):
            is_straight = True
            straight_ranks = unique_ranks[i:i+5]
            break


    if not straight and 14 in unique_ranks:
        if 2 in unique_ranks and 3 in unique_ranks and 4 in unique_ranks and 5 in unique_ranks:
            straight = True
            straight_ranks = [1, 2, 3, 4, 5]


    if straight and flush:
        straight_in_flush_suit = True
        for card in hand:
            if card.rank.value in straight_rank and card.suit != flush_suit:
                straight_in_flush_suit = False
                break

        if straight_in_flush_suit:
            return "Straight Flush"

    if sorted_counts[0] == 4:
        return "Four of a Kind"

    if sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return "Full House"

    if flush:
        return "Flush"

    if straight:
        return "Straight"

    if sorted_counts[0] == 3:
        return "Three of a Kind"

    if sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return "Two Pair"

    if sorted_counts[0] == 2:
        return "One Pair"

    return "High Card" # If none of the above, it's High Card
