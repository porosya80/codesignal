def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    if (yourLeft == friendsLeft or yourLeft == friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight):
        return True
    else:
        return False


def areEquallyStrong_smart(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
