from bs4 import BeautifulSoup


def parse_for_terminal(webpage: str) -> str:
    """
    Parses through the HTML to create a terminal-viewable string
    """
    soup: BeautifulSoup = BeautifulSoup(webpage, "html.parser")

    html_text: str = soup.decode()

    output_text: str = ""
    output_text = output_text + f"{soup.title.name=}\n"
    # output_text = output_text + f"{soup.find_all("link")=}\n"
    output_text = output_text + f"{soup.find_all("span")=}\n"
    output_text = output_text + f"{soup.find_all("form")=}\n"

    return output_text

# Parsers go here

# Render title
# Span class=header
# Forms
