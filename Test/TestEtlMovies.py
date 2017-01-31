from EtlMovies import groupByColumn, getMoviesByYear, createRanking, tagCloud, directorsReputation
import unittest
import csv
import time

reader = csv.DictReader(open('movie_metadata.csv'))
data = list(reader)

class TestEtlMovies(unittest.TestCase):

    def testColorMovies(self):

        results = groupByColumn(data, 'color')
        self.assertTrue(results['Color'] == 4694)

    def testMovieYears(self):
        results = getMoviesByYear(data, 'movie_title', 'title_year')
        self.assertTrue(results[1][0] == '2009' and results[1][1] == 253)

    def testRankingActors(self):
        results = createRanking(data)
        self.assertTrue(results['Robert De Niro'][0] == 53)

    def testTagCloud(self):
        results = tagCloud(data)
        self.assertTrue(results[107][0] == 'basketball' and results[107][1] == 27)

    def testDirectorsReputation(self):
        results = directorsReputation(data)
        self.assertTrue(results[0][0] == 'Steven Spielberg' and results[0][1] == 364000)


if __name__ == '__main__':
    unittest.main()