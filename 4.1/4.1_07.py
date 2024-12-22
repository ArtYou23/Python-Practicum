def can_eat(t1, t2):
    if abs(t1[0] - t2[0]) == 2 and abs(t1[1] - t2[1]) == 1:
        return True
    elif abs(t1[0] - t2[0]) == 1 and abs(t1[1] - t2[1]) == 2:
        return True
    else:
        return False