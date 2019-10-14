from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import re

import smtplib
from email.mime.text import MIMEText

# Create your views here.
def index(request, page):
    return render(request, "index.html", context={"page": page})

def load_single(request):
	source_file = request.GET.get('f', 'home') + ".html"
	return render(request, source_file)

class ContactUs(APIView):

	def post(self, request):
		if not 'name' in request.data or not 'mail' in request.data or not 'message' in request.data:
			return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Parameters are missing from the contact request."})

		# check email address loosely
		if not re.match(r"[^@]+@[^@]+\.[^@]+", request.data['mail']):
			return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "E-mail address is not in a valid format."})

		# perform email
		name = request.data['name']
		email = request.data['mail']
		message = request.data['message']
		msg = MIMEText("Someone has reached out via the E-TEC Contact form.\nName: " + name + "\nEmail: " + email + "\nMessage: " + message)

		msg['Subject'] = "New Contact on E-TEC"
		msg['From'] = "noreply@e-tec.ca"

		# fill in valid smtp server here (possibly gmail's servers)
		s = smtplib.SMTP_SSL('')
		# fill in valid credentials for smtp server here, if needed
		s.login('','')
		# fill in the recipients for the email here
		s.sendmail('noreply@e-tec.ca',[''], msg.as_string())
		s.quit()

		return Response()