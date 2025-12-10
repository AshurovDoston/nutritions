from django.shortcuts import render

def home_view(request):
    """
    Render the homepage.
    Shows different content based on whether user is authenticated.
    """
    return render(request, 'home.html')