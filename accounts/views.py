from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import CustomUserCreationForm


def signup_view(request):
    """
    Handle user registration.

    GET request: Display empty registration form
    POST request: Process form submission, create user, and log them in
    """

    # Check if this is a POST request (form submission)
    if request.method == 'POST':
        # Create form instance with submitted data
        form = CustomUserCreationForm(request.POST)

        # Validate the form
        if form.is_valid():
            # Save the new user to database
            user = form.save()

            # Get the username for the success message
            username = form.cleaned_data.get('username')

            # Add a success message
            messages.success(request, f'Account created successfully for {username}!')

            # Automatically log in the user after registration
            login(request, user)

            # Redirect to home page (or wherever you want)
            return redirect('home')  # 'home' is the name of the URL pattern

    else:
        # This is a GET request, show empty form
        form = CustomUserCreationForm()

    # Render the template with the form
    # If POST and form invalid, this shows the form with error messages
    # If GET, this shows the empty form
    return render(request, 'registration/signup.html', {'form': form})