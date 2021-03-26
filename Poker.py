def isFourOfAKind(arrayCountHand):
    if (4 in arrayCountHand):
        return True
    return False

def isFullHouse(arrayCountHand):
    if (3 in arrayCountHand) and (2 in arrayCountHand):
        return True
    return False

def isFlush(hand):
    if(hand[1] == hand[3] == hand[5] == hand[7] == hand[9]):
        return True
    return False

def isThreeOfAKind(arrayCountHand):
    if (3 in arrayCountHand):
        return True
    return False

def isPair(arrayCountHand):
    if (2 in arrayCountHand):
        return True
    return False

def High(arrayCountHand):
    high = 0
    for i in range(0, 13):
        if (arrayCountHand[i] == 1):
            high = i
    if high == 0:
        return "2 high"
    if high == 1:
        return "3 high"
    if high == 2:
        return "4 high"
    if high == 3:
        return "5 high"
    if high == 4:
        return "6 high"
    if high == 5:
        return "7 high"
    if high == 6:
        return "8 high"
    if high == 7:
        return "9 high"
    if high == 8:
        return "10 high"
    if high == 9:
        return "J high"
    if high == 10:
        return "Q high"
    if high == 11:
        return "K high"
    if high == 12:
        return "A high"

def count(hand):
    arrayCount = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    value = [hand[0], hand[2], hand[4], hand[6], hand[8]]
    for i in value:
        if (i == '2'):
            arrayCount[0] += 1
        if (i == '3'):
            arrayCount[1] += 1
        if (i == '4'):
            arrayCount[2] += 1
        if (i == '5'):
            arrayCount[3] += 1
        if (i == '6'):
            arrayCount[4] += 1
        if (i == '7'):
            arrayCount[5] += 1
        if (i == '8'):
            arrayCount[6] += 1
        if (i == '9'):
            arrayCount[7] += 1
        if (i == 'T'):
            arrayCount[8] += 1
        if (i == 'J'):
            arrayCount[9] += 1
        if (i == 'Q'):
            arrayCount[10] += 1
        if (i == 'K'):
            arrayCount[11] += 1
        if (i == 'A'):
            arrayCount[12] += 1    
    return arrayCount

def evaluate(hand):
    arrayCountHand = count(hand)
    if (isFourOfAKind(arrayCountHand)):
        return "four of a kind"
    elif (isFullHouse(arrayCountHand)):
        return "full house"
    elif (isFlush(hand)):
        return "flush"
    elif (isThreeOfAKind(arrayCountHand)):
        return "three of a kind"
    elif (isPair(arrayCountHand)):
        return "pair"
    else:
        return High(arrayCountHand)

print(evaluate("Qs7s2s4s5s"))
print(evaluate("7h8hKsTs8s"))
print(evaluate("2h4d2d4s4c"))
print(evaluate("KsKhKc8sKd"))
print(evaluate("3s9hTh9s9d"))
print(evaluate("2s8hThQs9d"))
