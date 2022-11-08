import asyncio
import unittest

from utils import ip_to_loc, openweather, makeresponse


class TestRequests(unittest.TestCase):
    def setUp(self):
        self.ip = '154.185.222.216'
        self.lat = '30.0626'
        self.lon = '31.2497'
        self.openweatherresp = {"coord":{"lon":31.2497,"lat":30.0626},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":22.42,"feels_like":22.1,"temp_min":21.9,"temp_max":22.42,"pressure":1015,"humidity":53},"visibility":10000,"wind":{"speed":3.09,"deg":280},"clouds":{"all":0},"dt":1667853153,"sys":{"type":1,"id":2514,"country":"EG","sunrise":1667794406,"sunset":1667833435},"timezone":7200,"id":360630,"name":"Cairo","cod":200}


    def test_fake_resp(self):
        lat, lon = asyncio.run(ip_to_loc(self.ip))
        self.assertTrue(lat, lon)
        self.assertTrue(float(lat))
        self.assertTrue(float(lon))

    def test_openweather(self):
        weather_response = asyncio.run(openweather(self.lat, self.lon))
        self.assertTrue(weather_response)
        self.assertEqual(type(weather_response), dict)
        self.assertTrue(weather_response['name'])

    def test_make_resource(self):
        responseJSON = asyncio.run(makeresponse(self.openweatherresp))
        self.assertTrue(responseJSON)