import questionary
from questionary import Choice

import votes
import style_prompt
from console import console
from helper import term_on_kbi


def main():
    console.print(style_prompt.title, style="bold #cc5de8")

    disable_results = "poll not set"

    while True:
        menu = term_on_kbi(
            questionary.select(
                "Select menu that you want :",
                choices=[
                    Choice("New poll", value=votes.Menu.NEW),
                    Choice(
                        "View results",
                        value=votes.Menu.VIEW,
                        disabled=disable_results,
                    ),
                ],
            )
        )
        print("")

        if menu == votes.Menu.NEW:
            while True:
                name = term_on_kbi(
                    questionary.text("What kind of poll would you like to create?")
                )

                votes.set_name(name)
                print("")

                voterAmount = term_on_kbi(
                    questionary.text("The amount of voters :", qmark="[NEW]")
                )
                votes.set_voter_amount(voterAmount)
                print("")

                candidateAmount = term_on_kbi(
                    questionary.text("The amount of candidates :", qmark="[NEW]")
                )
                print("")

                for i in range(int(candidateAmount)):
                    candidate = term_on_kbi(
                        questionary.text(f"- Candidate No.{i+1} :", qmark="[NEW]")
                    )
                    votes.add_candidate(candidate)

                print("")

                sure = term_on_kbi(
                    questionary.confirm(
                        "Are you sure with these settings?",
                        default=True,
                        auto_enter=False,
                    )
                )
                print("")

                if sure:
                    disable_results = ""
                    break


if __name__ == "__main__":
    main()
