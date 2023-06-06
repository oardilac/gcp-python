from django.http import JsonResponse
from django.shortcuts import render
import requests

def index(request):
    src_mysql = "34.125.250.32"
    destino_bigquery = "co_dtkl"
    
    api_url = "https://list-mysql-tables-ywtk7siozq-wn.a.run.app/"
    response = requests.get(api_url)
    resultados = response.json()

    return render(request, 'index.html', {'resultados': resultados, 'mysql': src_mysql, 'bigquery': destino_bigquery})