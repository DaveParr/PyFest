from bs4 import BeautifulSoup


def find_artists(file, find_all: str, class_: str):
    with open(file) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    return soup.find_all(find_all, class_=class_)
