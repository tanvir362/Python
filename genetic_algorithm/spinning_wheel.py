import random

def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
    return x

def list_gcd(ls):
    gcd = find_gcd(ls[0], ls[1])
    for itm in ls[2:]:
        gcd = find_gcd(gcd, itm)
    
    return gcd

# def list_lcm(ls):
#     m = 1
#     for itm in ls:
#         m *= itm
#     gcd = list_gcd(ls)
#     return m/gcd

MAX_ITR = 1000000
def test(d, wheel):
    test_dict = {}

    for i in range(MAX_ITR):
        ch = random.choice(wheel)
        test_dict[ch] = test_dict.get(ch, 0) + 1
    
    for key in test_dict:
        test_dict[key] = (test_dict[key]/MAX_ITR) * 100
        print(f'item: {key}    given: {d[key]}    actual: {test_dict[key]}')
    
def create_wheel(d):
    gcd = list_gcd([val for val in d.values()])
    wheel = []
    for key in d:
        for i in range(int(d[key]/gcd)):
            wheel.append(key)
    
    return wheel


if __name__=="__main__":
    # print(list_gcd([8, 12]))

    d = {
        'a': 60,
        'b': 30,
        'c': 10
    }

    w = create_wheel(d)
    print(w)
    test(d, w)