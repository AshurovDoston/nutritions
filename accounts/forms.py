from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom registration form that extends Django's UserCreationForm.
    Adds an email field and applies Bootstrap styling to form fields.
    """

    # Add email field (not included in default UserCreationForm)
    email = forms.EmailField(
        required=True,
        help_text="Required. Enter a valid email address.",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )

    class Meta:
        """
        Meta class defines which model to use and which fields to include.
        """
        model = User  # Use Django's built-in User model
        fields = ("username", "email", "password1", "password2")
        # password1 = password, password2 = password confirmation

    def __init__(self, *args, **kwargs):
        """
        Override __init__ to add CSS classes to all form fields.
        This makes styling easier and keeps forms consistent.
        """
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes and placeholders to username field
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })

        # Add Bootstrap classes and placeholders to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })

    def save(self, commit=True):
        """
        Override save method to save the email field.
        Django's UserCreationForm doesn't save email by default.
        """
        user = super().save(commit=False)  # Create user object but don't save yet
        user.email = self.cleaned_data['email']  # Add email to user object

        if commit:
            user.save()  # Save to database

        return user
