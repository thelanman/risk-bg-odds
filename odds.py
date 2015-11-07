'''
This script simulates one risk combat between one
attacker and one defender. It conducts 100k simulated
combats to compute probability of attacker wining
and the estimated number of armies remaining for each side
after combat.

=== Risk RULES ===
Attacker Dice = min(Armies - 1, 3
Defender Dice = min(Armies, 2)

1. Sort each set of dice from low to high and pair between Attacker / Defender
2. Compare each die roll to it's opponents pair.
3. Defender wins if it's Dice roll is equal or greater than attacker roll
4. Subtract armies from each side based on how many die rolls won / lost

=== USAGE ===
python odds.py attacker_armies defender_armies


=== EXAMPLE ===
python odds.py 8 3
Odds: 91.0% Attacker Rem: 5.7 Defender Rem: 0.2
'''

import random


def do_roll(a, d):
    a = min(a - 1, 3)
    d = min(d, 2)
    dice_to_keep = min(a, d)
    a_dice = sorted([random.randint(1,6) for i in range(a)])[-dice_to_keep:]
    d_dice = sorted([random.randint(1,6) for i in range(d)])[-dice_to_keep:]
    a_wins = sum([d_dice[i] < a_dice[i] for i in range(dice_to_keep)])
    d_wins = sum([d_dice[i] >= a_dice[i] for i in range(dice_to_keep)])
    return -d_wins, -a_wins


def do_combat(a, d):
    while a > 1 and d > 0:
        a_loss, d_loss = do_roll(a, d)
        a += a_loss
        d += d_loss
    return a, d


def odds(a, d, n=100000):
    a_wins = 0
    a_left_sum = 0
    d_left_sum = 0
    for i in range(n):
        a_final, d_final = do_combat(a, d)
        a_left_sum += a_final
        d_left_sum += d_final
        if a_final > d_final:
            a_wins += 1
    return a_wins / float(n), a_left_sum / float(n), d_left_sum / float(n)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'USAGE: python odds.py attacker_armies defender_armies'
        print 'EXAMPLE: python odds.py 15 11'
        sys.exit()
    a, d = sys.argv[1:]
    a = int(a)
    d = int(d)
    o, al, dl = odds(a, d)
    print 'Odds: %2.1f%%  Attacker Rem: %2.1f  Defender Rem: %2.1f' % (o * 100, al, dl)