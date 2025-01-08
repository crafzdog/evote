import questionary

title = """
███████╗██╗   ██╗ ██████╗ ████████╗███████╗
██╔════╝██║   ██║██╔═══██╗╚══██╔══╝██╔════╝
█████╗  ██║   ██║██║   ██║   ██║   █████╗  
██╔══╝  ╚██╗ ██╔╝██║   ██║   ██║   ██╔══╝  
███████╗ ╚████╔╝ ╚██████╔╝   ██║   ███████╗
╚══════╝  ╚═══╝   ╚═════╝    ╚═╝   ╚══════╝

"""

custom_style_base = questionary.Style(
    [
        ("qmark", "fg:#ff922b"),
        ("question", "fg:#868e96"),
        ("instruction", "fg:#868e96"),
        ("pointer", "bold fg:#b197fc"),
        ("highlighted", "bold fg:#b197fc"),
        ("answer", "fg:#dee2e6"),
        ("text", "fg:#dee2e6"),
    ]
)
