import pytest
from hr_day10_binary import int_to_binary, consecutive_ones


TABLE1 = [
    (1, [1], 1),
    (4, [1, 0, 0], 1),
    (5, [1, 0, 1], 1),
    (7, [1, 1, 1], 3),
    (11, [1, 0, 1, 1], 2),
]


@pytest.mark.parametrize('arr, result, consecutive', TABLE1)
def test_int_to_binary(arr, result, consecutive):
    assert int_to_binary(arr) == result


@pytest.mark.parametrize('arr, result, consecutive', TABLE1)
def test_consecutive_ones(arr, result, consecutive):
    assert consecutive_ones(result) == consecutive


def test_stack_size():
    from hr_day10_binary import Stack
    st = Stack()
    assert st.size() == 0
    st.push(2)
    st.push(4)
    assert st.size() == 2
    st.pop()
    assert st.size() == 1
    assert st.pop() == 2


def test_stack_push():
    from hr_day10_binary import Stack
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    assert st.size() == 3
    assert st.pop() == 3
