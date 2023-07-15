import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

value_error = "Dish price must be greater then zero."
type_error = "Dish price must be float."

# Req 2
def test_dish():
    dish = Dish("macarronada", 20.00)

    ingredient = Ingredient("bacon")

    assert dish.recipe == {}

    assert dish.__repr__() == f"Dish('{dish.name}', R${dish.price:.2f})"
    assert dish == dish
    assert dish.__hash__() == hash(dish.__repr__())

    dish.add_ingredient_dependency(ingredient, 1)
    assert dish.recipe == {ingredient: 1}

    restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert dish.get_restrictions() == restrictions

    assert dish.get_ingredients() == {ingredient}

    with pytest.raises(ValueError, match=value_error):
        Dish(dish.name, 0)

    with pytest.raises(TypeError, match=type_error):
        Dish(dish.name, "200")