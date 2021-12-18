from pathlib import Path
import datetime as dt

INPUTS_FOLDER = Path(__file__).parent.parent / "inputs"


def get_input(name):
    with open(INPUTS_FOLDER / name) as f:
        content = f.read()
    return content

def test_func(expected, func, *args, **kwargs):
    t_start = dt.datetime.now()
    actual = func(*args, **kwargs)
    assert actual == expected, f"{actual} != {expected}"
    elapsed = dt.datetime.now() - t_start
    print(f"test passed in {elapsed.total_seconds()} seconds")