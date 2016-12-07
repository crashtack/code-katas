import pytest
from hr_operators import meal_cost_calc


PAR_TABLE = [
    (12.00, 20, 8, 15),
]


@pytest.mark.parametrize('cost, tip, tax, result', PAR_TABLE)
def test_meal_cost_calc(cost, tip, tax, result):
    # import pdb; pdb.set_trace()
    assert meal_cost_calc(cost, tip, tax) == result
