from django.shortcuts import render
from django.http import HttpResponse



from pyfcm import FCMNotification

# Create your views here.
from aps.models import local
from aps.serializers import locationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from scipy.spatial import cKDTree
from scipy import inf
import json
from pyfcm import FCMNotification
FCM_SERVER_KEY="AAAANeDBYLI:APA91bE8eVwhG6uP6INDXA0GCbU-Sl5xsZHh96_tW3v47uSnUTuoEC4Wt2GjX4nT39_V0E5IIe7OzIh4OGyKCN3gvj5JDJrzEorFVdj3BDVmN6rmF-9UlIG1p6i57omFSnw9LcUR_N1g"
    
class Locate(APIView):

	def get(self, request, format=None):
		snippets = local.objects.all()
		serializer = locationSerializer(snippets, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = locationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)




class Notify(APIView):
	def get(self, request, format=None):
		token = request.GET.get("device_token", '')
		a = local(device_token=token)
		a.save()


	   




		return HttpResponse(token)

	def post(self, request, format=None):

		#reg_id = local.objects.all()[0].device_token
		reg_id="c4SrVpf3RVWgEMJmBfnz_U:APA91bFqlEk3lURwtME9Az6VD5SsA-eaeHBOOrNyW1cH0TcFKWsDH-uhNOvCBiIDHf0L6DjHISKyzLsPZwfPnxeX2YiZr_IFccWTQtIJPRtEwUFmg3meeKLo3nRM3HektNHF5wSu4mxe"
		print(reg_id) #quick and dirty way to get that ONE fcmId from table
		message_title = "Zeo Learn"
		message_body = "Hi john, Zeo learn Rocks!"
		result = FCMNotification(api_key=FCM_SERVER_KEY).notify_single_device(registration_id=reg_id, message_title=message_title, message_body=message_body)
		
		return JsonResponse(result)


	
	    


	




    


