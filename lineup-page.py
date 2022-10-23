from bs4 import BeautifulSoup

with open("test/arc-tangent-lineup.html/LINE-UP – ArcTanGent.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
