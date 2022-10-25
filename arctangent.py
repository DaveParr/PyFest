from lineup import find_artists

arctangent_artists = find_artists(
    file="test/data/LINE-UP – ArcTanGent.html",
    find_all="h2",
    class_="grid-title",
)
type(arctangent_artists)

type([artist.get_text() for artist in arctangent_artists])
