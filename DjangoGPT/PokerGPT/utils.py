def get_hand_info(hand):
    # Extract the player names and their chip counts
    # example: 
    #       players = get_hand_info(hand)
    #       print(players)
    #       OUTPUT: ['Nabets', 'steps31870', 'lesombre4', 'Siamon', 'Marmule825']
    #
    
    players = []
    for line in hand:
        if line.startswith('Seat'):
            player = line.split(':')[1].strip()
            players.append(player)
    return players

def get_players_chips(hand, players):
    # return a dictionary to store the player names and their corresponding chip counts
    # OUTPUT: {'Nabets': 2.61, 'steps31870': 1.38, 'lesombre4': 2.0, 'Siamon': 1.97, 'Marmule825': 2.47}
    player_chips = {}
    for i, player in enumerate(players):
        player_chips[player] = int(hand[i + 1].split(':')[1].strip())
    return player_chips