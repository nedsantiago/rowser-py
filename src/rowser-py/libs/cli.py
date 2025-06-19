import sys
from libs import http_requests
from libs import http_parsing
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.layout import Layout


def run_app() -> None:
    """
    This is the Application's entry point (after `main.py`). This runs the
    commandline application.
    """
    
    # Parse the commandline arguments
    args: list[str] = sys.argv

    # Check if command was used correctly
    if len(args) < 2:
        err_msg = "Incorrect Usage:\nrowser [ARGS] [URL]"
        print(err_msg)
        sys.exit()

    # Last argument should be a URL
    url: str = args[-1]

    _VALID_ARGS: dict = {
        'nc': "No Cookies"
    }

    # Run request
    response: str = http_requests.get_request(url)

    # Parse Response
    viewable: str = http_parsing.parse_for_terminal(response)

    # Print to Terminal
    layout = Layout()
    layout.split_row(
        Panel(viewable),
        Layout(name="lower")
    )
    print(layout)
    # print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"), "Hello")
    # print(
    #     Padding(
    #         "Hello",
    #         (1, 4),
    #         expand=False
    #     )
    # )

    # Listen to other commands from user

