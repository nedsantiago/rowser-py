from bs4 import BeautifulSoup, Tag
from typing import Optional


def parse_for_terminal(webpage: str) -> str:
    """
    Parses through the HTML to create a terminal-viewable string
    """
    soup: BeautifulSoup = BeautifulSoup(webpage, "html.parser")

    html_text: str = soup.decode()

    tag_title: Optional[Tag] = soup.title
    if tag_title is not None:
        title: str = str(tag_title.name)
    else:
        title = "[No Title]"

    output_text: str = ""
    output_text += f"{title}\n"
    # output_text = output_text + f"{soup.find_all("link")=}\n"
    output_text += f"{soup.find_all("span")}\n"
    output_text += f"{soup.find_all("form")}\n"

    return output_text

# Parsers go here

# Render title
# Span class=header
# Forms
