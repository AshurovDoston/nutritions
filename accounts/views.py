from django.http import HttpResponse
import datetime

def account_view(request):
    return HttpResponse("Welcome to the account page!")


def current_datetime_view(request):
    now = datetime.datetime.now()
    html = f"<html><body><h2>Current date and time: {now}</h2></body></html>"
    return HttpResponse(html)