from questionary import Style

title = """
███████╗██╗   ██╗ ██████╗ ████████╗███████╗
██╔════╝██║   ██║██╔═══██╗╚══██╔══╝██╔════╝
█████╗  ██║   ██║██║   ██║   ██║   █████╗  
██╔══╝  ╚██╗ ██╔╝██║   ██║   ██║   ██╔══╝  
███████╗ ╚████╔╝ ╚██████╔╝   ██║   ███████╗
╚══════╝  ╚═══╝   ╚═════╝    ╚═╝   ╚══════╝

"""

custom_base = [
    ("question", "fg:#868e96"),
    ("instruction", "fg:#868e96"),
    ("answer", "fg:#fd7e14"),
    ("qmark", "fg:#1864ab bold"),
]

custom_style_text = Style(
    [
        *custom_base,
    ]
)

custom_style_select = Style(
    [
        *custom_base,
        ("pointer", "fg:#1864ab"),
        ("highlighted", "fg:#1864ab"),
        ("text", "fg:#dee2e6"),
    ],
)

custom_style_text_NEW = Style(
    [
        *custom_base,
        ("qmark", "fg:#2f9e44 bold"),
    ]
)
