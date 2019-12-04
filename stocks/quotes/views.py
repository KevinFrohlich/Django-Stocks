from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e95c28451060417dba76769b63faf5af")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})
