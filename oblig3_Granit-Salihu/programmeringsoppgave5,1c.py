filmList = [{"Name": "Inception", "Year": 2010, "Rating": 8.7},
            {"Name": "Inside Out", "Year": 2015, "Rating": 8.1},
            {"Name": "Con Air", "Year": 1997, "Rating": 6.9}]

def filmAddDefaultRating(list, Name, Year, Rating = 5.0):
    list.append({"Name": Name, "Year": Year, "Rating": Rating})

filmAddDefaultRating(filmList, "The Peanut Man", 2009)
filmAddDefaultRating(filmList, "The Watermelon", 2010, 6.1)


print(filmList)