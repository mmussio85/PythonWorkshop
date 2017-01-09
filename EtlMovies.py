import csv
import time
reader = csv.DictReader(open('movie_metadata.csv'))
data = list(reader)

def wrapHtml(fn):
    def wrapped():
        html =  '<html><body>'+ fn() +'</body></html>'
        with open('etl.html', 'w') as f:
            f.write(html)
    return wrapped

def wrapTableColor(fn):
    def wrapped():
        start_time = time.time()
        item = fn()
        tagInit = '<p><b>COLOR MOVIES</b></p><br/><table><tr><th>Color of movies</th><th>Count</th></tr >'
        rowColor = '<tr><td>Color</td><td></td><td>'+str(item['Color'])+'</td></tr >' \
                    + '<tr><td>Black and white</td><td></td><td>'+str(item[' Black and White'])+'</td></tr >' \
                    + '<tr><td>None</td><td></td><td>' + str(item['']) + '</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowColor + tagEnd
    return wrapped

def wrapTableDirectorMovies(fn):
    def wrapped():
        rowDirector = ''
        start_time = time.time()
        directors = fn()
        pairs = [(k, v) for k, v in directors.items()]
        tagInit = '<p><b>MOVIES BY DIRECTOR</b></p><br/><table><tr><th>Director Name</th><th>Movies</th></tr >'
        for pair in pairs:
            rowDirector += '<tr><td>'+ str(pair[0]) +'</td><td></td><td>' + str(pair[1]) + '</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowDirector + tagEnd
    return wrapped

def wrapTableLessCriticism(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>LESS CRITICISM</b></p><br/><table><tr><th>Movie Title</th><th>Num of critics</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableMaxDuration(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>MAX DURATION MOVIES</b></p><table><tr><th>Movie Title</th><th>Duration</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableMostGrossMovies(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>MOST GROSS MOVIES</b></p><table><tr><th>Movie Title</th><th>Gross(desc)</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableLessGrossMovies(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>LESS GROSS MOVIES</b></p><table><tr><th>Movie Title</th><th>Gross(asc)</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableMostExpensiveMovies(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>MOST EXPENSIVE MOVIES</b></p><table><tr><th>Movie Title</th><th>Budget(desc)</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableLessExpensiveMovies(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        movies = fn()
        tagInit = '<p><b>LESS EXPENSIVE MOVIES</b></p><table><tr><th>Movie Title</th><th>Budget(asc)</th></tr >'
        for movie in movies:
            rowMovie += '<tr><td>'+ movie[0] +'</td><td>'+ movie[1] +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableMaxAndMinMoviesReleases(fn):
    def wrapped():
        start_time = time.time()
        tupleResult = fn()
        tagInit = '<p><b>MAX AND MIN MOVIES RELEASED BY YEAR</b></p><table><tr><th>Movie Year</th><th>Released movies</th></tr >'
        lessReleases = '<tr><td>'+ str(tupleResult[0][0]) +'</td><td>'+ str(tupleResult[0][1]) +'</td></tr >'
        mostReleases = '<tr><td>'+ str(tupleResult[1][0]) +'</td><td>'+ str(tupleResult[1][1]) +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + lessReleases + mostReleases + tagEnd
    return wrapped

def wrapTableTagKeywords(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        tags = fn()
        tagInit = '<p><b>TAG CLOUD KEYWORDS</b></p><table><tr><th>Keyword</th><th>Count</th></tr >'
        for tag in tags:
            rowMovie += '<tr><td>'+ str(tag[0]) +'</td><td>'+ str(tag[1]) +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableRankActorsByAppereances(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        rankByAppereance = fn()
        tagInit = '<p><b>RANK ACTORS ORDERED BY APPEREANCES</b></p><table><tr><th>Actor Name</th><th>Apprereances(desc)</th><th>Facebook Likes</th><th>Best Movie</th><th>Imdb score</th></tr >'
        for k, v in rankByAppereance:
            rowMovie += '<tr><td>'+ str(k) +'</td><td>'+ str(v[0]) +'</td><td>'+ str(v[1]) +'</td><td>'+ str(v[2][0]) +'</td><td>'+ str(v[2][1]) +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableRankActorsByLikes(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        rankByAppereance = fn()
        tagInit = '<p><b>RANK ACTORS ORDERED BY LIKES</b></p><table><tr><th>Actor Name</th><th>Apprereances</th><th>Facebook Likes(desc)</th><th>Best Movie</th><th>Imdb score</th></tr >'
        for k, v in rankByAppereance:
            rowMovie += '<tr><td>'+ str(k) +'</td><td>'+ str(v[0]) +'</td><td>'+ str(v[1]) +'</td><td>'+ str(v[2][0]) +'</td><td>'+ str(v[2][1]) +'</td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableMostGrossGenereByYear(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        years = fn()
        tagInit = '<p><b>TOP PROFITS(GROSS) BY GENRE BY YEAR</b></p><table><tr><th>Year</th><th>Genre</th><th>Count(desc)</th></tr >'
        for year in years.keys():
            rowMovie += '<tr><td>'+ str(year) + '</td>'
            if years[year]:
                rowMovie += '<td>' + str(years[year][0]) + '</td><td>' + str(years[year][1]) + '</td></tr >'
            else:
                rowMovie += '<td></td><td></td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableLessGrossGenereByYear(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        years = fn()
        tagInit = '<p><b>LESS PROFITS BY GENRE BY YEAR</b></p><table><tr><th>Year</th><th>Genre</th><th>Count(asc)</th></tr >'
        for year in years:
            rowMovie += '<tr><td>' + str(year) + '</td>'
            if years[year]:
                rowMovie += '<td>' + str(years[year][0]) + '</td><td>' + str(years[year][1]) + '</td></tr >'
            else:
                rowMovie += '<td></td><td></td></tr >'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableLikeByGenre(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        genres = fn()
        tagInit = '<p><b>MOST LIKED GENRE BU PEOPLE</b></p><table><tr><th>Genre</th><th>Likes</th></tr >'
        rowMovie += '<tr><td>' + genres[0] + '</td>' + '<td>' + str(genres[1]) + '</td>'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

def wrapTableDirectorsReputiation(fn):
    def wrapped():
        rowMovie = ''
        start_time = time.time()
        directors = fn()
        tagInit = '<p>Top Directors reputation</b></p><table><tr><th>Director Name</th><th>Likes</th></tr >'
        for director in directors:
            rowMovie += '<tr><td>' + director[0] + '</td>' + '<td>' + str(director[1]) + '</td>'
        tagEnd = '<table><br/><p>Elapsed Time: '+ str(round(time.time() - start_time, 2)) +'</p><br/>'
        return tagInit + rowMovie + tagEnd
    return wrapped

@wrapTableColor
def movieColor():
    return groupByColumn(data, 'color')

@wrapTableDirectorMovies
def directorMovies():
    return groupByColumn(data, 'director_name')

@wrapTableLessCriticism
def tenLessCriticism():
    return takeRowsByCondition(data, 'movie_title', 'num_critic_for_reviews', 10)

@wrapTableMaxDuration
def maxDurationMovies():
    return takeRowsByCondition(data, 'movie_title', 'duration', 20, reverse=True)

@wrapTableMostGrossMovies
def mostGrossMovies():
    return takeRowsByCondition(data, 'movie_title', 'gross', 5, reverse=True)

@wrapTableLessGrossMovies
def lessGrossMovies():
    return takeRowsByCondition(data, 'movie_title', 'gross', 5)

@wrapTableMostExpensiveMovies
def mostExpensiveMovies():
    return takeRowsByCondition(data, 'movie_title', 'budget', 3, reverse=True)

@wrapTableLessExpensiveMovies
def lessExpensiveMovies():
    return takeRowsByCondition(data, 'movie_title', 'budget', 3)

@wrapTableMaxAndMinMoviesReleases
def maxAndMinMoviesReleases():
    return getMoviesByYear(data, 'movie_title', 'title_year')

@wrapTableTagKeywords
def tagCloudKeywords():
    return tagCloud(data)

@wrapTableRankActorsByAppereances
def rankActorsByAppereances():
    return createRankingByAppearances(data)

@wrapTableRankActorsByLikes
def rankActorsByLikes():
    return createRankingByLikes(data)

@wrapTableMostGrossGenereByYear
def mostGrossGenereByYear():
    return gorssByYear(data, reverse=True)

@wrapTableLessGrossGenereByYear
def lessGrossGenereByYear():
    return gorssByYear(data)

@wrapTableLikeByGenre
def likesByGenre():
    return genresLikes(data)

@wrapTableDirectorsReputiation
def directorsRank():
    return directorsReputation(data)

@wrapHtml
def buildBody():
    return movieColor()  \
    + directorMovies()  \
    + tenLessCriticism()    \
    + maxDurationMovies()   \
    + mostGrossMovies() \
    + lessGrossMovies() \
    + mostExpensiveMovies() \
    + lessExpensiveMovies() \
    + maxAndMinMoviesReleases() \
    + tagCloudKeywords()    \
    + rankActorsByAppereances() \
    + rankActorsByLikes()   \
    + mostGrossGenereByYear()   \
    + lessGrossGenereByYear()   \
    + likesByGenre()    \
    + directorsRank()

def groupByColumn(data, columnName):
    selectDistinct = distinctColumn(data, 'movie_title')
    columnValues = [selectDistinct[i][columnName] for i in range(len(selectDistinct))]
    return {selectDistinct[i][columnName]: columnValues.count(selectDistinct[i][columnName]) for i in range(len(selectDistinct))}

def distinctColumn(data, selectColumn, oneColumn = False):
    columnValues = [data[i][selectColumn] for i in range(len(data))]
    if not oneColumn:
        return [data[i] for i in range(len(columnValues)) if data[i][selectColumn] not in columnValues[i + 1:]]
    else:
        return [data[i][selectColumn] for i in range(len(columnValues)) if data[i][selectColumn] not in columnValues[i + 1:]]

def takeRowsByCondition(data, selectColumn, orderByColumn, takeNumber=None, reverse=False):
    selectDistinct = distinctColumn(data, selectColumn)
    if takeNumber:
        filteredOrderedList = sorted(filter(lambda x : x[orderByColumn] != '' and x[selectColumn] != '', selectDistinct), \
           reverse = reverse, key = lambda x: int(x[orderByColumn]))[:takeNumber]
    else:
        filteredOrderedList = sorted(filter(lambda x: x[orderByColumn] != '' and x[selectColumn] != '', selectDistinct), \
            reverse=reverse, key=lambda x: int(x[orderByColumn]))
    return [(filteredOrderedList[i][selectColumn], filteredOrderedList[i][orderByColumn])  for i in range(len(filteredOrderedList))]

def getMoviesByYear(data, selectColumn, yearColumn):
    selectDistinct = distinctColumn(data, selectColumn)
    columnValues = [selectDistinct[i][yearColumn] for i in range(len(selectDistinct))]
    groupByYear = {selectDistinct[i][yearColumn]: columnValues.count(selectDistinct[i][yearColumn]) \
                   for i in range(len(selectDistinct)) if selectDistinct[i][yearColumn] != ''}
    listYears =  sorted(groupByYear.items(), key = lambda x: int(x[1]))
    return (listYears[0], listYears[-1])

def __flattenList(oldList):
    flattened = []
    for row in oldList:
        for elem in row:
            flattened.append(elem)
    return flattened



def __filterMoviesByActor(data, actorName):
    moviesByActor = filter(lambda x: (x['actor_1_name'] == actorName or x['actor_2_name'] == actorName or x['actor_3_name'] == actorName) \
                            and x['actor_1_facebook_likes'] != '' and x['actor_2_facebook_likes'] != ''\
                            and x['actor_3_facebook_likes'] != '', data)
    likesMainActor = sum([int(moviesByActor[i]['actor_1_facebook_likes']) for i in range(len(moviesByActor)) if moviesByActor[i]['actor_1_name'] == actorName])
    likesSecondActor = sum([int(moviesByActor[i]['actor_2_facebook_likes']) for i in range(len(moviesByActor)) if moviesByActor[i]['actor_2_name'] == actorName])
    likesThirdActor = sum([int(moviesByActor[i]['actor_3_facebook_likes']) for i in range(len(moviesByActor)) if moviesByActor[i]['actor_3_name'] == actorName])
    return likesMainActor + likesSecondActor + likesThirdActor

def createRanking(data):
   rank = distinctColumn(data, 'movie_title')
   rank = map(lambda x: (x['actor_1_name'], x['actor_2_name'], x['actor_3_name'], x['movie_title'], \
                         x['actor_1_facebook_likes'], x['actor_2_facebook_likes'], x['actor_3_facebook_likes'], \
                         x['actor_3_facebook_likes'], x['imdb_score']), rank)
   rank = map(lambda x: [(x[0], x[3], x[4], x[8]), (x[1], x[3], x[5], x[8]), (x[2], x[3], x[7], x[8])], rank)
   rank = reduce(list.__add__, rank)
   groupedRank = {}
   for actorName, movieTitle, facebookLikes, score in rank:
       groupedRank.setdefault(actorName, []).extend([(movieTitle , facebookLikes , score)])
   return {i : (len(groupedRank[i]), \
                  sum([int(groupedRank[i][j][1]) for j in range(len(groupedRank[i])) \
                       if len(groupedRank[i]) and groupedRank[i][j][1] != '' ]) , \
                  max([(groupedRank[i][k][0],groupedRank[i][k][2]) for k in range(len(groupedRank[i]))], key= lambda x: x[1])
                  )
             for i in groupedRank.keys() if len(groupedRank[i]) > 0}

def createRankingByAppearances(data):
    return sorted(createRanking(data).items(), key=lambda (k, v): v[0], reverse=True)

def createRankingByLikes(data):
    return sorted(createRanking(data).items(), key=lambda (k, v): v[1], reverse=True)

def tagCloud(data):
    allWords = [(data[i]['plot_keywords']).split('|') for i in range(len(data))]
    allWordsFlattened = __flattenList(allWords)
    tagCloudItems = {allWordsFlattened[i]: allWordsFlattened.count(allWordsFlattened[i]) \
                    for i in range(len(allWordsFlattened)) if allWordsFlattened[i] != ''}
    return sorted(tagCloudItems.items(), reverse = True, key=lambda x: int(x[1]))


def gorssByYear(data, reverse= True):
    grossGenre = distinctColumn(data, 'movie_title')
    grossGenre = map(lambda x: (x['genres'].split('|'), x['title_year'], x['gross']), grossGenre)
    splitedGenres = [(grossGenre[i][0][j], grossGenre[i][2], grossGenre[i][1]) for i in range(len(grossGenre)) \
             for j in range(len(grossGenre[i][0])) ]
    groupedByYear = {}
    for genre, gross, year in splitedGenres:
        groupedByYear.setdefault(year, []).extend([(genre, gross)])
    return  { i : (next(iter(sorted(filter(lambda x: x[1] != '', groupedByYear[i]),
                                    reverse= reverse, key=lambda x: int(x[1]))), None)
                )for i in groupedByYear.keys() if len(groupedByYear[i]) > 0
            }

def genresLikes(data):
    likesByGenre = distinctColumn(data, 'movie_title')
    likesByGenre = map(lambda x: (x['genres'].split('|'), x['movie_facebook_likes']), likesByGenre)
    likesByGenre = [(likesByGenre[i][0][j], likesByGenre[i][1]) for i in range(len(likesByGenre)) for j in
                    range(len(likesByGenre[i][0]))]
    groupByGenre = {}
    for genre, likes in likesByGenre:
        groupByGenre.setdefault(genre, []).extend([likes])
    result = { i : sum([int(groupByGenre[i][j]) for j in range(len(groupByGenre[i])) if groupByGenre[i][j] != '']) for i in groupByGenre.keys()}
    return sorted(result.items(), reverse = True, key=lambda x: int(x[1]))[0]

def directorsReputation(data):
    directorLikes = distinctColumn(data, 'movie_title')
    directorLikes = map(lambda x: (x['director_name'], x['director_facebook_likes']), directorLikes)
    groupByDirector = {}
    for director, likes in directorLikes:
        groupByDirector.setdefault(director, []).extend([likes])
    result = {i: sum([int(groupByDirector[i][j]) for j in range(len(groupByDirector[i])) if groupByDirector[i][j] != '']) for i
              in groupByDirector.keys()}
    return sorted(result.items(), reverse=True, key=lambda x: int(x[1]))[:5]


if __name__ == "__main__":
    buildBody()