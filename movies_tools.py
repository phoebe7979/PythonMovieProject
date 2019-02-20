import csv

with open('movies_clean.csv', 'r', encoding = "utf-8") as f:
    reader = csv.reader(f)
    movie_list = list(reader)

numberofmovies = len(movie_list)



#creating a class Movie with information for each movie item from the csv file

class Movie:
    def __init__(self, row):
        self.title = row[1]
        self.date = row[6]
        self.rating = row[7]
        self.genre = row[11]
        self.imdb = row[15]

moviestr = ""

for row in movie_list[1:6]:
    single_movie = Movie(row)
    print(single_movie.title)
    print(single_movie.imdb)
    moviestr += str(single_movie.title) + " | " + str(single_movie.imdb) + "<br>"





#if __name__ == "__main__":
#    movie = Movie()
