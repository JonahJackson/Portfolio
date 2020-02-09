try:
    score = float(input("Enter score: "))
    if score < 0 or score > 1:
        raise ValueError
    if score >= .9:
            print('A')
    elif score >= .8:
            print('B')
    elif score >= .7:
            print('C')
    elif score >= .6:
            print('D')
    else:
            print('F')
except ValueError:
    print("Bad score")
delay = input()