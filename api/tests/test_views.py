from django.shortcuts import reverse
from rest_framework.test import APITestCase
from api.models import movie

class TestNoteApi(APITestCase):
    """This class holds method for api view tests"""

    def setUp(self):
        #Create a movie
        self.movie = Movie(name="The space between us", year_of_release =2017)
        self.movie.save()

    def test_api_can_create_a_movie(self):
        """This function asserts whether a movie is created successfully"""
        response = self.client.post(reverse('movies'),{
            "name" : "Bee movie",
            "year_of_release": 2007
        })

        #Assert new movie was created
        self.assertEqual(Movie.objects.count(), 2)

        #Assert a created status code was created
        self.assertEqual(201, response.status_code)

    def test_api_can_get_movies(self):
        """This methods check whether the api can retrieve a movie"""
        self.client.get(reverse('movies'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_api_can_update_a_movie(self):
        """This method checks if the api can update a movie"""
        response = self.client.put(reverse(detail),kwargs={"pk": 1}),{
            "name" : "The space between us updated",
            "year_of_release" : 2017
        }, format="json")

        #Check info returned has the update
        self.assertEqual("The space between us updated", response.data["name"])

    def test_api_can_delete_a_movie(self):
        """This function check that the api is able to delete a specific movie"""
        response = self.client.delete(reverse("detail"), kwargs={'pk': 1}))
        self.assertEqual(204, response.status_code)
