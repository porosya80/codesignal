def growingPlant(upSpeed, downSpeed, desiredHeight):
    counter = 0
    height = 0
    while height <= desiredHeight :
        counter += 1
        # print(height)
        height += upSpeed
        if height >= desiredHeight:
            break
        height -= downSpeed
    return counter


upSpeed = 10 
downSpeed = 9 
desiredHeight = 4
print(growingPlant(upSpeed, downSpeed, desiredHeight))
