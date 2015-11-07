This script simulates one Risk boardgame combat between one
attacker and one defender. It conducts 100k simulated
combats to compute probability of attacker wining
and the estimated number of armies remaining for each side
after combat.

# Risk Rules 
Attacker Dice = min(Armies - 1, 3
Defender Dice = min(Armies, 2)

1. Sort each set of dice from low to high and pair between Attacker / Defender
2. Compare each die roll to it's opponents pair.
3. Defender wins if it's Dice roll is equal or greater than attacker roll
4. Subtract armies from each side based on how many die rolls won / lost

# USAGE
```sh
$ python odds.py attacker_armies defender_armies
```

# EXAMPLE 
```sh
$ python odds.py 8 3
Odds: 91.0% Attacker Rem: 5.7 Defender Rem: 0.2
```
