from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    bacon = Ingredient("bacon")

    assert bacon.name == 'bacon'
    assert bacon == Ingredient("bacon")
    assert repr(bacon) == f"Ingredient('{bacon.name}')"
    assert len(bacon.restrictions) == 2
    assert hash(bacon) == hash('bacon')