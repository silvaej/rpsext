import random

'''
Rock - Paper - Scissors - Lizard - Spock
+ Scissors cuts Paper
+ Paper covers Rock
+ Rock crushes Lizard
+ Lizard poisons Spock
+ Spock smashes Scissors
+ Scissors decapitates Lizard
+ Lizard eats Paper
+ Paper disproves Spock
+ Spock vaporizes Rock
+ (and as it always has) Rock crushes Scissors

Let Rock, Paper, Scissors, Lizard, Spock be equal to
0 , 1, 2, 3, 4 respectively
'''
TRANSLATIONS = {
    'scissors': 0,
    'paper': 1,
    'rock': 2,
    'lizard': 3,
    'spock': 4
}

ADJMAT = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0]
]

def generate(playerDecision, botDecision):
    playerTranslated = TRANSLATIONS[playerDecision]
    botTranslated = TRANSLATIONS[botDecision]
    playerPt = ADJMAT[playerTranslated][botTranslated]
    botPt = ADJMAT[botTranslated][playerTranslated]

    return playerPt, botPt 

playerTotal = 0
botTotal = 0

print(
"""

Welcome to Rock-Paper-Scissors extd.

+++++++++RULES+++++++++
+ Scissors cuts Paper
+ Paper covers Rock
+ Rock crushes Lizard
+ Lizard poisons Spock
+ Spock smashes Scissors
+ Scissors decapitates Lizard
+ Lizard eats Paper
+ Paper disproves Spock
+ Spock vaporizes Rock
+ (and as it always has) Rock crushes Scissors
"""
)

for _ in range(7):
    #get their throws
    while (playerDecision := input('Your pick: ').lower()) not in TRANSLATIONS: pass
    botDecision = random.choices(list(TRANSLATIONS.keys()))[0]

    print(playerDecision, botDecision)

    playerPt, botPt = generate(playerDecision, botDecision)
    playerTotal += playerPt
    botTotal += botPt
    print(':|') if playerPt==botPt else print(':)') if playerPt==1 else print(':(')
    print('--------------------------------')

print(playerTotal, botTotal, sep='-')
if (playerTotal > botTotal): print('You won!')
elif (playerTotal == botTotal) : print('Draw!')
else: print('You lose!')