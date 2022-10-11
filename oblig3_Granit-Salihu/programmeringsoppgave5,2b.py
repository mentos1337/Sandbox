filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]

def filmListGjennomsnitt(list):
    poeng = 0
    for rating in list:
        poeng += rating.get("Rating")
    return poeng / len(list)


print(filmListGjennomsnitt(filmList))