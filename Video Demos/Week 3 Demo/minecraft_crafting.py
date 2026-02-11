RECIPES = [
    # item, ingredients (as list of strings)
    ["torch", ["stick", "coal"]],
    ["crafting_table", ["plank", "plank", "plank", "plank"]],
    ["furnace", ["cobblestone"] * 8],
    ["stone_pickaxe", ["stick", "stick", "cobblestone", "cobblestone", "cobblestone"]],
    ["chest", ["plank"] * 8],
]

inventory = {"stick": 2, "coal": 1, "plank": 10, "cobblestone": 9}


# Takes a list of ingredient names (strings) and returns a dictionary counting how many of each item appears
def count_items(items_list):
    counts = {}
    for item in items_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts 


# Takes an inventory and recipe_ingredients as a list of strings, returns True if inventory has enough of each item, else False
def can_craft(inventory, recipe_ingredients):
    recipe_counts = count_items(recipe_ingredients)
    for ingredient_name, amount_needed in recipe_counts.items():
        if inventory.get(ingredient_name, 0) < amount_needed:
            return False
    return True

# Takes an inventory and list of recipes, returns a list of item names (strings) that are craftable
def craftable_items(inventory, recipes):
    craftable = []
    for recipe in recipes:
        if can_craft(inventory, recipe[1]):
            craftable.append(recipe[0])
    return craftable


# Takes inventory, item to craft, and recipes list. Returns new inventory after spending ingredients if craftable, otherwise None
# Do not mutate the original dictionary! If item_name isn't found in recipes, raise Exception
def craft(inventory, item_name, recipes):
    recipe_found = None
    for recipe in recipes:
        if recipe[0] == item_name:
            recipe_found = recipe
            break
    
    if recipe_found is None:
        raise Exception(f"Unknown recipe: {item_name}")
    
    ingredients = recipe_found[1]
    
    if not can_craft(inventory, ingredients):
        return None
    
    new_inventory = inventory.copy()
    
    recipe_counts = count_items(ingredients)
    for ingredient_name, amount_needed in recipe_counts.items():
        new_inventory[ingredient_name] -= amount_needed
    
    if item_name in new_inventory:
        new_inventory[item_name] += 1
    else:
        new_inventory[item_name] = 1
    
    return new_inventory


print("Function 1 - count_items:")
print(count_items(["stick", "coal", "stick"]))

print("\nFunction 2 - can_craft:")
print("Can craft torch?", can_craft(inventory, ["stick", "coal"]))

print("\nFunction 3 - craftable_items:")
print("Craftable items:", craftable_items(inventory, RECIPES))

print("\nFunction 4 - craft:")
print("Original inventory:", inventory)
new_inv = craft(inventory, "torch", RECIPES)
print("After crafting torch:", new_inv)



