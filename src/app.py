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
                    Choice("Start poll", value=votes.Menu.START),
                    Choice(
                        "View results",
                        value=votes.Menu.VIEW,
                    ),
                ],
                style=style_prompt.custom_style_select,
                instruction=" ",
            )
        )
        print("")

        if menu == votes.Menu.NEW:
            while True:
                name = term_on_kbi(
                    questionary.text(
                        "What kind of poll would you like to create?",
                        qmark="[new]",
                        style=style_prompt.custom_style_text_NEW,
                    )
                )

                votes.set_name(name)
                print("")

                voterAmount = term_on_kbi(
                    questionary.text(
                        "The amount of voters :",
                        qmark="[new]",
                        style=style_prompt.custom_style_text_NEW,
                    )
                )
                votes.set_voter_amount(int(voterAmount))
                print("")

                candidateAmount = term_on_kbi(
                    questionary.text(
                        "The amount of candidates :",
                        qmark="[new]",
                        style=style_prompt.custom_style_text_NEW,
                    )
                )
                print("")

                for i in range(int(candidateAmount)):
                    candidate = term_on_kbi(
                        questionary.text(
                            f"- Candidate No.{i+1} :",
                            qmark="[new]",
                            style=style_prompt.custom_style_text_NEW,
                        )
                    )
                    votes.add_candidate(candidate)

                print("")

                sure = term_on_kbi(
                    questionary.confirm(
                        "Are you sure with these settings?",
                        default=True,
                        auto_enter=False,
                        style=style_prompt.custom_style_text,
                    )
                )
                print("\nsetting up... OK.\n")

                if sure:
                    # disable_results = ""
                    break

        elif menu == votes.Menu.START:
            for i in range(votes.state["voters"]):
                candidate_index = term_on_kbi(
                    questionary.select(
                        "Choose your choice :",
                        choices=[
                            {"name": candidate["name"], "value": i}
                            for i, candidate in enumerate(votes.state["candidates"])
                        ],
                        qmark=f"[polling-{i+1}]",
                        style=style_prompt.custom_style_select,
                        instruction=" ",
                    )
                )

            print(votes.state)


if __name__ == "__main__":
    main()
