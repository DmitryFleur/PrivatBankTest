from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import DummyData
from .dummy_data_creation import load_dummy_data
import time


class ChartsView(View):
    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        if start_date and end_date:
            data = DummyData.objects.filter(date__range=[start_date, end_date])
            response_data = list()
            for record in data:
                record_data = list((time.mktime(record.date.timetuple()) * 1000, record.first_value, record.second_value))
                response_data.append(record_data)
            return JsonResponse({'data': response_data})

        return render(request, 'index.html')


class LoadDummyData(View):
    def get(self, request):
        records_number = request.GET.get('records_number', 100)

        try:
            records_number = int(records_number)
        except TypeError:
            raise TypeError

        data = load_dummy_data(records_number)
        if data:
            return JsonResponse({'status': 'loaded'})
        return JsonResponse({'status': 'not loaded'})
