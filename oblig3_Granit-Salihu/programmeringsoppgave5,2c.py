filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]


def filmListFraAr(list, Year):
    newlist = []
    for year in list:
        if year.get("Year") >= Year:
            newlist.append(year)
    return newlist

print(filmListFraAr(filmList,2010))