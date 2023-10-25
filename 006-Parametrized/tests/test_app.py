from typing import Type

import pytest

from app.main import add_positive_numbers, factorial, fibonacci


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 26),
    ],
)
def test_factorial(test_input: int, expected_output: int) -> None:
    assert factorial(test_input) == expected_output


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ((1, 2), 3),
        ((100, 200), 300),
        ((0, 0), 0),
    ],
)
def test_add_positive_numbers(
    test_input: tuple[int, int], expected_output: int
) -> None:
    assert add_positive_numbers(*test_input) == expected_output


@pytest.mark.parametrize(
    "test_input, expected_exception",
    [
        ((-1, 2), ValueError),
        ((1, -2), ValueError),
        ((-1, -2), ValueError),
    ],
)
def test_add_positive_numbers_exceptions(
    test_input: tuple[int, int], expected_exception: Type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        add_positive_numbers(*test_input)


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
    ],
)
def test_fibonacci_valid(test_input: int, expected_output: int) -> None:
    assert fibonacci(test_input) == expected_output


@pytest.mark.parametrize(
    "test_input, expected_exception",
    [
        (-1, ValueError),
        (-100, ValueError),
    ],
)
def test_fibonacci_exceptions(
    test_input: int, expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        fibonacci(test_input)
