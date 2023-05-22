from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Links
# Create your views here.
def scraper(request):
    response = requests.get('http://www.google.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        Links.objects.create(name = link.string, linkk = link.get('href'))
    links = Links.objects.all()
    context = { 'links':links }
    return render(request, 'myapp/links.html', context)