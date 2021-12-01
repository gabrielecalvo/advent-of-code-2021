from pathlib import Path

INPUTS_FOLDER = Path(__name__).parent / "inputs"


def get_input(name):
    with open(INPUTS_FOLDER / name) as f:
        content = f.read()
    return content
