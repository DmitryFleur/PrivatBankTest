from django.test import TestCase
from django.test import Client
from .dummy_data_creation import load_dummy_data
from .models import DummyData
import time


class TestCharts(TestCase):
    def setUp(self):
        load_dummy_data(100)

    def testAjaxGetRequest(self):
        c = Client()
        response = c.get('/?start_date=2018-01-11&end_date=2018-08-30')
        self.assertEqual(response.status_code, 200)

        data = DummyData.objects.filter(date__range=['2018-01-11', '2018-08-30'])
        response_data = list()
        for record in data:
            record_data = list((time.mktime(record.date.timetuple()) * 1000, record.first_value,
                                record.second_value))
            response_data.append(record_data)

        self.assertJSONEqual(str(response.content, encoding='utf8'), {'data': response_data})
