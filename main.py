import lineup_page

arctangent_artists = lineup_page.find_artists(
    file="test/arc-tangent-lineup.html/LINE-UP – ArcTanGent.html",
    find_all="h2",
    class_="grid-title",
)

[item.get_text() for item in arctangent_artists]
