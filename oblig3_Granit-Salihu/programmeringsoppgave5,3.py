filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]

def filmListFil(list,filNavn):
    with open(filNavn, "w") as fineList:
        for film in list:
            fineList.write("{} - {} has a rating of {} \n".format(film.get("Name"), film.get("Year"), film.get("Rating")))

filmListFil(filmList, "film.txt")

def FilmListLes(filNavn):
    with open(filNavn, "r") as lesList:
        print(lesList.read())

FilmListLes("film.txt")