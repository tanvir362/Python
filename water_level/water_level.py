"""
Do you ever fall into situation where you go to take shower and no water middle of the shower? Jemey fall into this situation often so he
wanted to setup a water level indicator for his home water supply. And he came sothat you write code for the indicator to detect water level.

Input:
line 1: n the number of different level
line 2: m the number of reading of the sensor
line 3: m space separated integer reading of the sensor -1 if sensor doesn't detect level else the level. the levels are between 0 and n-1 

Output:
m lines, each line should have corresponding level for the reading
"""
"""
Need to write a program to identify water level

if sensor provied a level print the level if don't print the previous level
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Water Level

You must output water level for corresponding sensor reading

<<Line 1:>> An integer [[n]] denotes the number of different level.
<<Line 2:>> An integer [[m]] the number of reading from sensor
Line 3: [[m]] space separated integer [[reading]] indicating sensor readings. A [[reading]] is -1 if water surface lies between two level else the level


1 line [[m]] space separated integer [[water_level]] for corresponding sensor readings. If any reading can not specify water level you have to print previous [[water_level]]

3 ≤ [[n]], [[m]] ≤ 100
-1 ≤ [[reading]] ≤ [[n-1]]
0 ≤ [[water_level]] ≤ [[n-1]]

Test 1:
in:
3
5
0 -1 1 -1 2
out:
0 0 1 1 2

Validator 1:
in:
4
9
0 -1 1 -1 -1 2 -1 3 4
out:
0 0 1 1 1 2 2 3 4

Test 2:
in:
5
9
4 -1 -1 3 -1 2 1 -1 0
out:
4 4 4 3 3 2 1 1 0


"""

n = int(input())
m = int(input())
lvl = 0
levels = []
for r in input().split():
    reading = int(r)
    if reading != -1:
        lvl = reading
    
    levels.append(lvl)

print(*levels)
