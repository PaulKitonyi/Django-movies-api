from django.test import TestCase

from api.models import Movie


class TestMovieModel(TestCase):
    """This is a class to hold the test functions"""

    def setUp(self):
        """This a function to setup the test object"""
        self.movie = Movie(name="split", year_of_release=2016)
        self.movie.save()

    def test_api_saves_the_movie(self):
        self.assertEqual(Movie.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.movie.name, str(self.movie))

