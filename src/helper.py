import questionary
from console import console

import sys


def term_on_kbi(question: questionary.Question):
    try:
        return question.unsafe_ask()
    except:
        console.print("[bold #ff6b6b]app terminated...")
        sys.exit(1)


name = []
