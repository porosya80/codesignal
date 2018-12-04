def groupingDishes(dishes):
    ingredients = {}
    result = []
    for dish in dishes:
        for place in range(1, len(dish)):
            if dish[place] not in ingredients.keys():
                ingredients[dish[place]] = []
            ingredients[dish[place]].append(dish[0])
    for dish, ingredients in ingredients.items():
        if len(ingredients) >= 2:
            result.append([dish] + sorted(ingredients))
    return sorted(result)


dishes=[["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print(groupingDishes(dishes))


""" [["Cheese", "Quesadilla", "Sandwich"],
 ["Salad", "Salad", "Sandwich"],
 ["Sauce", "Pizza", "Quesadilla", "Salad"],
 ["Tomato", "Pizza", "Salad", "Sandwich"]]
 """
