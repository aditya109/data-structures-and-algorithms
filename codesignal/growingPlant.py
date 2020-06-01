def growingPlant(upSpeed, downSpeed, desiredHeight):

    day = 0
    height = 0
    while True:
        height += upSpeed 
        day += 1
        if desiredHeight <= height:
            return day
        height -= downSpeed

print(growingPlant(10, 9, 4))

