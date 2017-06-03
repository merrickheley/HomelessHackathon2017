from django.core.management.base import BaseCommand, CommandError
from HackApp.models import *
import csv
#This file will launch a listener for the aktn device it can be modified to change the device

def main():
	f = open("./HackApp/management/commands/raw_data/Brisbane_Services.csv", "r")
	reader = csv.reader(f)
	headers = next(reader, None)
	column ={}
	count=0
	for h in headers:
		column[h]=[]
	for row in reader:
		for h, v in zip(headers, row):
			column[h].append(v)
		count+=1

	for i in range(count):
		category=column["Service_Category"][i]
		serv_type=column["Service_Type"][i]
		serv_cat = get_category(category, serv_type)

def get_category(category, serv_type):
	cat_query=ServiceCategory.objects.filter(category=category, serv_type=serv_type)
	if cat_query.count()==0:
		serv_cat=ServiceCategory()
		serv_cat.category=category
		serv_cat.serv_type=serv_type
		serv_cat.save()
	else:
		serv_cat=cat_query[0]
	return serv_cat

class Command(BaseCommand):
	help = "Opens up the subscription and updates the database."

	def handle(self, *args, **options):
		main()
