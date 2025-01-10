from rich.table import Table
from rich.console import Console


class Menu:
    NEW = 0
    START = 1
    VIEW = 2
    EXIT = 3


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


def reset_candidate():
    state["candidates"] = []


def send_poll(index: int):
    state["candidates"][index]["vote"] += 1


def get_winner():
    winners = []
    highest = 0

    for candidate in state["candidates"]:
        if candidate["vote"] > highest:
            highest = candidate["vote"]
            winners = [candidate]
        elif candidate["vote"] == highest:
            winners.append(candidate)

    return winners


def view_results():
    console = Console()

    table = Table(title=state["name"], show_lines=True, title_style="magenta bold")

    table.add_column("No", justify="center", no_wrap=True)
    table.add_column("Candidate", justify="left", no_wrap=True)
    table.add_column("Votes", justify="center", no_wrap=True)
    table.add_column("Percentages", justify="center", no_wrap=True)

    for i, candidate in enumerate(state["candidates"]):
        table.add_row(
            str(i + 1),
            candidate["name"],
            str(candidate["vote"]),
            f"{candidate["vote"] / state["voters"] * 100:.2f}%",
        )

    console.print(table)
    console.print(
        "\n[yellow bold]Total votes[/yellow bold] :",
        f"[#dee2e6 bold]{state["voters"]}",
    )
    console.print(
        "[red bold]Winner[/red bold] :",
        f"[#dee2e6 bold]{", ".join([winner["name"] for winner in get_winner()])}",
    )

    print("")
