import pytest

from hworder.generator import ArrayGenerator


@pytest.mark.parametrize(
    "size",
    [
        (
            1
        ),
        (
            2
        ),
    ],
)
def test_array_generator(
    size: int,
):
    array_generator = ArrayGenerator(size)

    assert size == array_generator().shape[0]
