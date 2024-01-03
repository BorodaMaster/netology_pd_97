def download_data(source_path):
    shift = 3
    data = {}
    start_index, stop_index = -1, 0
    index_dish_name, index_count_ingr = 0, 1
    templ = ["ingredient_name", "quantity", "measure"]

    with open(source_path) as f:
        for index, line in enumerate(f):
            if index == index_dish_name:
                # get name dish
                name = line.strip()
                # add key (name dish) to dictionary
                data[name] = []
            elif index == index_count_ingr:
                # get count ingredients
                count_ingr = int(line.strip())

                # set start & stop indexes ingredients
                start_index = index + 1
                stop_index = index + count_ingr

                # set next index dish name
                index_dish_name += count_ingr + shift

                # set next index count ingredient
                index_count_ingr += count_ingr + shift
            elif start_index <= index <= stop_index and index != 0:
                # convert data (str to list) and create new element
                ingredient = line.strip().split(' | ')
                ingredient_formatted = dict(map(lambda i, j: (i, j), templ, ingredient))
                # add value (ingredient) to dictionary
                data[name].append(ingredient_formatted)

    return data


def get_shop_list_by_dishes(cook_book: dict, person: int, dishes: list):
    list_ingredient = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] in list_ingredient:
                list_ingredient[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"], "quantity": int(ingredient["quantity"]) * person
                                                                  + list_ingredient[ingredient["ingredient_name"]][
                                                                      "quantity"]}
            else:
                list_ingredient[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"], "quantity": int(ingredient["quantity"]) * person}

    return list_ingredient


if __name__ == "__main__":
    # set dish list
    dish_list = ['Запеченный картофель', 'Омлет']
    # load cook books
    cook_books = download_data("recipes.txt")
    # generate shop list
    shop_list = get_shop_list_by_dishes(cook_books, 2, dish_list)
    # output result
    for key, value in shop_list.items():
        print("{} - {} {}".format(key, value["quantity"], value["measure"]))
