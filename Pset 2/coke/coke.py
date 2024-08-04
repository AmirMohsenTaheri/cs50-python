price = 50
amount_due = 0

while price > 0 :
    coin = int(input("Insert Coin: "))
    match coin:
        case 25 | 10 | 5:
            price -= coin
            amount_due += coin
            if amount_due >= 50:
                break
            else:
                print(f"Amount Due: {price}")
        case _:
            print(f"Amount Due: {price}")
            continue

change_owed = amount_due - 50
print(f"Change Owed: {change_owed}")
