class Movie:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration


    def getMovie(self):
        return self.name


    def getGenre(self):
        return self.genre


    def getDuration(self):
        return self.duration


    def movieInfo(self):
        return f"""Movie Name:Mission: {self.name}
Movie Genre : {self.genre}
Movie Duration : {self.duration} minutes."""


    @classmethod
    def createMovie_fromString(cls, movie_details):
        name, genre, duration = movie_details.split("-")
        new_movie = cls(name, genre, duration)
        return new_movie



class StarCinema:
    name = "StarCinema"
    all_branch_info = {}

    def __init__(self, branch):
        self.branch = branch
        self.movieList = []
        print(f"Welcome to the {self.branch} branch of {StarCinema.name}! ")


    def addMovies(self, *movie_objects):
        for movie in movie_objects:
            if movie.getMovie() not in self.movieList:
                self.movieList.append(movie.getMovie())
                if self.branch not in StarCinema.all_branch_info:
                    StarCinema.all_branch_info [self.branch] = [movie]

                else:
                    StarCinema.all_branch_info [self.branch].append(movie)

                print(f"{movie.getMovie()} added to {self.branch} branch. ")

            else:
                print(f"Movie is already added in this branch. ")


    def removeMovie(self, movieObject):
        for branch, movieObj in StarCinema.all_branch_info.items():
            if self.branch == branch:
                for movie in movieObj:
                    if movie == movieObject:
                        StarCinema.all_branch_info [self.branch].remove(movie)



    @classmethod
    def check(self, movieName):
        Flag = False
        movie1 =""
        for branch, movieObj in StarCinema.all_branch_info.items():
            for movie in movieObj:
                if movie.getMovie() == movieName:
                    Flag = True
                    movie1 = movie
                    print(f"{movieName} is being streamed in {branch} branch.")

        if Flag == False:
            print(f"{movieName} is not being streamed in any branch.")

        elif Flag == True:
            print(f"It is of {movie1.getGenre()} genre and {movie1.getDuration()} minutes duration. ")


    @classmethod
    def showAllBranchInfo(cls):
        for branch, movieObj in StarCinema.all_branch_info.items():
            counter = 0
            print(f"Branch Name : {branch}")
            for movie in movieObj:
                counter += 1
                print(f"""Movie No : {counter}
Movie Name : {movie.getMovie()}
Movie Genre : {movie.getGenre()}
Movie Duration : {movie.getDuration()} minutes.
************************** """)
        print("################################# ")



movie1 = Movie('Oppenheimer', 'Biographical Drama', 180)
movie2 = Movie('Barbie', 'Fantasy Comedy', 114)
movie3 = Movie('Mission: Impossible – Dead Reckoning Part One', 'Action', 163)
print('1==========================================')
print(movie3.movieInfo())
print('2==========================================')
movie4 = Movie.createMovie_fromString('Prohelika-Drama-153')
print('3==========================================')
print(movie4.movieInfo())
print('4==========================================')
branch1 = StarCinema('Mohakhali')
print('5==========================================')
branch1.addMovies(movie1, movie2, movie4)
print('6==========================================')
branch1.addMovies(movie1, movie3)
print('7==========================================')
StarCinema.showAllBranchInfo()
print('8==========================================')
branch2 = StarCinema('Mirpur')
print('9==========================================')
branch2.addMovies(movie1, movie2, movie3)
print('10==========================================')
StarCinema.showAllBranchInfo()
print('11==========================================')
StarCinema.check('Oppenheimer')
print('12=========================================')
StarCinema.check('Sound of Freedom')
print('13=========================================')
branch1.removeMovie(movie2)
StarCinema.showAllBranchInfo()
print('14=========================================')
branch2.removeMovie(movie1)
StarCinema.showAllBranchInfo()