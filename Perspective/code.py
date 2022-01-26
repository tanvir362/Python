seq=input()
p=input()

indxs = [i for i,c in enumerate(seq) if c==p]
trgt = (len(seq)-1)//2

for indx in indxs:
    print(seq[indx-trgt:]+seq[:indx-trgt])



"""

0123456789
len 3 - mid 1 - last 2
len 4 - mid 1 - last 3
len 5 - mid 2 - last 4
len 6 - mid 2 - last 5
len 7 - mid 3 - last 6


Title:
Perspective

Stacement:
Suppose you play a multiplayer game where the orientation of the players is important, in each round it changes the orientation of the players but you see yourself at a specific place of the screen

"""