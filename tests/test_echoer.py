import pytest

from hworder.sayer import Echoer


@pytest.mark.parametrize(
    "value",
    [
        (
            "hello world!",
        ),
        (
            "goodbye cruel world!",
        ),
    ],
)
def test_echoer(
    value: str
):
    echoer = Echoer()

    assert value == echoer(value)
