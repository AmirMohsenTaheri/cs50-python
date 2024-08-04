item = {

}
while True:
    try:
        get_item = input("item: ").upper()
        if get_item in item :
            item[get_item] += 1
        else :
            item[get_item] = 1
    except EOFError:
        sorted_dict = dict(sorted(list(item.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")
        break
    except KeyError:
        pass
