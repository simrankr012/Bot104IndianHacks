from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import json
import requests

from helloworld import settings
from bot.models import HospitalBeds,Hospital,HospitalBooking

def index(request):
	print (request.GET)

	hospital = Hospital.objects.get(title = request.GET.get('hospital'))
	obj = HospitalBeds.objects.get(title_id=hospital.id)
	print (obj)
	context = {
			"hospital":hospital,
			"hospital_details":obj

		}

	if request.method=="POST":
		print "-----------------"
		print request.POST
		hospital_name = request.POST.get('hospital_name')
		bed_type = request.POST.get("bed")
		print (hospital_name,bed_type)
		hospital = Hospital.objects.get(title = hospital_name)
		bed_book = HospitalBooking()
		bed_book.title_id = hospital.id
		bed_book.bed_type = bed_type
		bed_book.save()
		print bed_book

		obj_bed = HospitalBeds.objects.get(title_id=hospital.id)
		if bed_book.bed_type == 'A':
			obj_bed.room_type_a = obj_bed.room_type_a - 1
			obj_bed.save()
			print obj_bed,bed_book.bed_type
		else:
			obj_bed.room_type_b = obj_bed.room_type_b - 1
			obj_bed.save()
			print obj_bed,bed_book.bed_type
	return render(request,"book-a-bed.html",context)

