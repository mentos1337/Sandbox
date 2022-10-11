filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]


def filmAdd(list, Name, Year, Rating):
    list.append({"Name": Name, "Year": Year, "Rating": Rating})


filmAdd(filmList, "Rush Hour", 1998, 7.0)
filmAdd(filmList, "Rush Hour 2", 2001, 6.6)
filmAdd(filmList, "Rush Hour 3", 2007, 6.2)
print(filmList)