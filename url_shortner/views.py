from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'url_short/index.html')

def index_form(request):
    if request.method == "POST":
        long_url = request.POST.get('long_url')
        new_url = shorten_url(long_url)

        if 'link' in new_url:
            return render(request, "url_short/new_url.html", context={'url': new_url['link']})
        else:
            error = new_url.get('message', 'An error occurred while shortening the URL.')
            return render(request, "url_short/new_url.html", context={'error': error})
    return render(request, 'url_short/index.html')

def shorten_url(url):
    headers = {
        'Authorization': 'Bearer 2dbe86d6d5f087790262ca83027d8fb6e9d07b06',
        'Content-Type': 'application/json',
    }

    data_dict = {"long_url": url, "domain": "bit.ly"}

    data = json.dumps(data_dict)

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    response_dict = response.json()

    return response_dict



