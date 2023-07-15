# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, newline='') as file:
            resultReader = csv.DictReader(file)
            dishes = {}

            for row in resultReader:
                dish_name, price, ingredient_name, recipe_amount = (
                    row["dish"],
                    float(row["price"]),
                    row["ingredient"],
                    int(row["recipe_amount"])
                )

                dish = dishes.setdefault(dish_name, Dish(dish_name, price))
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name),
                    recipe_amount
                )
                self.dishes.add(dish)