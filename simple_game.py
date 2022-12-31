import random
windows = ['GOAT', 'GOAT', 'CAR']

random.shuffle(windows)
luck = windows.index('CAR')
goats_at = [i for i,v in enumerate(windows) if v=='GOAT']

choice = int(input("Which window do you want to choice?\n[Window1]    [Window2]    [Window3]\n:"))

print("    ".join(f"[{'Selected' if i+1==choice else ('Goat' if v=='GOAT' and (i!=max(goats_at) or choice-1 in goats_at) else 'Window'+str(i+1))}]" for i,v in enumerate(windows)))

sw = input('Do you want to switch?(y/n): ').lower()[0]
print(['Bad luck, try again', 'Congratulations, You win a car'][(choice-1 == luck and sw=='n') or (choice-1 != luck and sw=='y')])


# print(windows)
