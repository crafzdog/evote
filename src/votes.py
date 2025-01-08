class Menu:
    NEW = 0
    VIEW = 1


votes = {
    "name": "",
    "voters": 0,
    "winner": [],
    "candidates": [],
}


def set_name(name: str):
    votes["name"] = name


def set_voter_amount(voterAmount: int):
    votes["voters"] = voterAmount


def add_candidate(name: str):
    votes["candidates"].append({"name": name, "value": 0})
