def order(*ingr):
    global in_stock
    ii = {
        "Эспрессо": (1, 0, 0),
        "Капучино": (1, 3, 0),
        "Макиато": (2, 1, 0),
        "Кофе по-венски": (1, 0, 2),
        "Латте Макиато": (1, 2, 1),
        "Кон Панна": (1, 0, 1),
    }
    for i in ingr:
        if in_stock["coffee"] >= ii[i][0] and in_stock["milk"] >= ii[i][1] and in_stock["cream"] >= ii[i][2]:
            in_stock["coffee"] -= ii[i][0]
            in_stock["milk"] -= ii[i][1]
            in_stock["cream"] -= ii[i][2]
            return i
    return "К сожалению, не можем предложить Вам напиток"