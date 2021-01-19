def evaluate(hand):
    check = []
    handValue = [hand[0], hand[2], hand[4], hand[6], hand[8]]
    i = 0

    for i in range (len(handValue)):
        if handValue[i] == "T":
            handValue[i] = "10"
        if handValue[i] == "J":
            handValue[i] = "11"
        if handValue[i] == "Q":
            handValue[i] = "12"
        if handValue[i] == "K":
            handValue[i] = "13"
        if handValue[i] == "A":
            handValue[i] = "14"

    # Flush case
    if (hand[1] == hand[3] == hand[5] == hand[7] == hand[9]):
        return "flush"

    # Remaining cases
    for i in handValue:
        if i not in check:
            check.append(i)

    # Four of a kind or Full House
    if (len(check) == 2):
        start = check[0]
        counter = 0
        for i in handValue:
            if i == start:
                counter += 1
        if (counter == 1 or counter == 4):
            return "four of a kind"
        else: 
            return "full house"

    # Three of a kind or pair
    elif (len(check) == 3 or len(check) == 4):
        for i in check:
            counter = 0
            for j in handValue:
                if i == j:
                    counter += 1
            if counter == 3:
                return "three of a kind"
        return "pair"
    else:
        max = int(handValue[0])
        for i in handValue:
            i = int(i)
            if i > max:
                max = i
        if (max == 10):
            max = "T"
        if (max == 11):
            max = "J"
        if (max == 12):
            max = "Q"
        if (max == 13):
            max = "K"
        if (max == 14):
            max = "A"
        return str(max) + " high"

# Test case
hand = ["2s8hThQs9d"] 
for i in hand:
    print(evaluate(i))
# Expected: flush, pair, full houese, four of a kind, three of a kind, high