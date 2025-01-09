class Menu:
    NEW = 0
    START = 1
    VIEW = 2


state = {
    "name": "",
    "voters": 0,
    "winner": [],
    "candidates": [],
}


def set_name(name: str):
    state["name"] = name


def set_voter_amount(voterAmount: int):
    state["voters"] = voterAmount


def add_candidate(name: str):
    state["candidates"].append({"name": name, "vote": 0})
