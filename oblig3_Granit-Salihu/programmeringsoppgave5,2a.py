filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]

def filmListPrint(list):
    for film in list:
        print(film.get("Name"), "-", film.get("Year"), "has a rating of", film.get("Rating"))

        
filmListPrint(filmList)