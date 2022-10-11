class filmer:
    def __init__(self, filmtittel, utgivelsesår, score):
        self.filmtittel = filmtittel
        self.utgivelsesår = utgivelsesår
        self.score = score
        print(f"{filmtittel} was released in {utgivelsesår} and currently has a score of {score}")
    def printer(self):
        return (f"{self.filmtittel} was released in {self.utgivelsesår} and currently has a score of {self.score}")

film1 = filmer("Inception", 2010, 8.8)
film2 = filmer("The Martian", 2015, 8.0)
film3 = filmer("Joker", 2019, 8.4)

print()
print(film1.printer())
print(film2.printer())
print(film3.printer())