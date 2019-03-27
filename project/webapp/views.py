from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Flight
from . serializers import flightSerializer

import json
class flightList(APIView):

    def get(self,request):
        flight1=Flight.objects.all()
        serializer=flightSerializer(flight1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
def get_flight(request,flight_no):
    if request.method=='GET':
        try:
            flight=Flight.objects.get(f_no=flight_no)
            response=json.dumps([{
        "Flight No.":flight.f_no,
        "Aircraft Type":flight.a_type,
        "Arrival From ":flight.a_from,
        "Arrival From ":flight.a_time,
        "Departure To":flight.d_to,
        "Departure Time":flight.d_time
        }])
        except:
            response=json.dumps([{'Error':'No flight found'}])
    return HttpResponse(response,content_type='text/json')

def input(request):
    return HttpResponse("<h3> Enter Flight No.</h3><input type='text'><input type='submit' value='submit'>")
