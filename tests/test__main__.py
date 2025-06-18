import os


def test_entrypoint():
    exitstatus = os.system("python src/rowser-py https://lite.duckduckgo.com/lite")
