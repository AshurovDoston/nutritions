# Nutrition Tracker

A Django-based web application for tracking nutrition and managing dietary goals. This application provides user authentication, a responsive interface, and a foundation for nutrition tracking features.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Setup from Scratch](#project-setup-from-scratch)
- [Project Structure](#project-structure)
- [How It All Works Together](#how-it-all-works-together)
- [Development Commands](#development-commands)
- [Implementation Details](#implementation-details)
- [Future Enhancements](#future-enhancements)

## Project Overview

This is a Django 6.0 web application designed for nutrition tracking. The project currently implements a complete user authentication system with login, signup, and logout functionality, along with a responsive homepage that displays different content based on user authentication status.

## Features

### Current Features

- **User Authentication System**
  - User registration with email validation
  - Login/Logout functionality
  - Password reset capability (via Django's built-in auth)
  - Automatic login after successful registration
  - Session management

- **Responsive User Interface**
  - Modern, gradient-based design
  - Mobile-responsive layout
  - Dynamic navigation bar (shows different options for authenticated/non-authenticated users)
  - Custom styled forms with Bootstrap-inspired classes

- **Homepage**
  - Hero section for non-authenticated users with call-to-action buttons
  - Dashboard view for authenticated users
  - Feature cards showcasing app capabilities
  - Personalized welcome message for logged-in users

## Technology Stack

- **Backend Framework**: Django 6.0
- **Database**: SQLite3 (development)
- **Configuration Management**: python-decouple
- **Code Formatting**: Black
- **Python Version**: 3.13
- **Template Engine**: Django Templates
- **Static Files**: CSS (no framework dependencies)

## Project Setup from Scratch

Here's a detailed walkthrough of how this project was built from the ground up:

### Step 1: Environment Setup

```bash
# Create project directory
mkdir nutrition
cd nutrition

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# Install Django and dependencies
pip install django==6.0
pip install python-decouple
pip install black

# Save dependencies
pip freeze > requirements.txt
```

### Step 2: Django Project Initialization

```bash
# Create Django project
django-admin startproject django_project .

# Create Django apps
python manage.py startapp accounts  # For user authentication
python manage.py startapp core      # For core functionality
```

### Step 3: Configuration Setup

**Created `.env` file** for environment variables:
```
DEBUG=True
```

**Modified `django_project/settings.py`**:
- Imported `decouple` for environment variable management
- Added `accounts` app to `INSTALLED_APPS`
- Configured `TEMPLATES` to use project-level templates directory
- Set up `STATICFILES_DIRS` for static file management
- Added authentication redirects:
  - `LOGIN_REDIRECT_URL = "/"`
  - `LOGOUT_REDIRECT_URL = "/"`
  - `LOGIN_URL = "/accounts/login/"`

### Step 4: Database Setup

```bash
# Create initial database tables
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Step 5: URL Configuration

**Created hierarchical URL structure**:

**`django_project/urls.py`** (Main URL dispatcher):
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),      # Custom account views
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth views
    path("", include("core.urls")),                   # Core app views
]
```

**`accounts/urls.py`** (Account-specific URLs):
```python
urlpatterns = [
    path("signup/", signup_view, name="signup"),
]
```

**`core/urls.py`** (Core app URLs):
```python
urlpatterns = [
    path("", home_view, name="home"),
]
```

### Step 6: User Authentication Implementation

**Created `accounts/forms.py`**:
- Built `CustomUserCreationForm` extending Django's `UserCreationForm`
- Added email field (not included by default)
- Applied custom CSS classes for consistent styling
- Overrode `save()` method to handle email storage

**Created `accounts/views.py`**:
- Implemented `signup_view()` function:
  - Handles GET requests (displays form)
  - Handles POST requests (processes registration)
  - Validates form data
  - Creates new user account
  - Automatically logs in user after registration
  - Redirects to homepage with success message

### Step 7: Template System

**Created template hierarchy**:

**`templates/base.html`** (Base template):
- HTML5 boilerplate structure
- Navigation bar with conditional rendering:
  - Shows "Hello, [username]" and "Logout" for authenticated users
  - Shows "Login" and "Sign Up" for non-authenticated users
- Block system for `title` and `content`
- Links to static CSS files

**`templates/home.html`** (Homepage):
- Extends `base.html`
- Conditional content rendering:
  - **For authenticated users**: Dashboard with welcome message and quick action buttons
  - **For non-authenticated users**: Hero section with CTA buttons
- Feature cards showcasing app capabilities

**`templates/registration/login.html`**:
- Login form with username and password fields
- Error message display
- Link to password reset
- Link to signup page

**`templates/registration/signup.html`**:
- Registration form with username, email, and password fields
- Form validation and error display
- Help text for password requirements
- Link to login page for existing users

### Step 8: Static Files (CSS)

**Created `static/css/` directory with three CSS files**:

**`style.css`** (Base styles):
- CSS reset
- Navigation bar styling
- Container layout
- Responsive design utilities

**`auth.css`** (Authentication pages):
- Form container styling
- Input field styling with focus states
- Error and success message styling
- Button styling for login/signup
- Help text formatting

**`home.css`** (Homepage):
- Hero section with gradient background
- Feature card grid layout
- Dashboard styling for authenticated users
- Quick action buttons
- Responsive breakpoints for mobile devices

### Step 9: Git Version Control

```bash
# Initialize git repository
git init

# Create .gitignore
echo ".venv/
*.pyc
__pycache__/
db.sqlite3
.env" > .gitignore

# Initial commit
git add .
git commit -m "first commit"

# After adding apps
git add .
git commit -m "add new apps"
```

## Project Structure

```
nutrition/
│
├── accounts/                      # User authentication app
│   ├── forms.py                  # Custom user registration form
│   ├── views.py                  # Signup view
│   ├── urls.py                   # Account URL patterns
│   └── migrations/               # Database migrations
│
├── core/                         # Core application logic
│   ├── views.py                  # Home view
│   ├── urls.py                   # Core URL patterns
│   └── migrations/               # Database migrations
│
├── django_project/               # Project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL dispatcher
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
├── static/                       # Static files
│   └── css/
│       ├── style.css            # Base styles and navigation
│       ├── auth.css             # Authentication page styles
│       └── home.css             # Homepage styles
│
├── templates/                    # HTML templates
│   ├── base.html                # Base template (navbar, structure)
│   ├── home.html                # Homepage template
│   └── registration/
│       ├── login.html           # Login page
│       └── signup.html          # Signup page
│
├── .env                         # Environment variables (DEBUG)
├── .gitignore                   # Git ignore rules
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # SQLite database
└── README.md                    # This file
```

## How It All Works Together

### 1. Request Flow

When a user visits the application, here's what happens:

```
User Request → django_project/urls.py → App URLs → View → Template → Response
```

**Example: User visits homepage (/)**

1. Request hits `django_project/urls.py`
2. Matches `path("", include("core.urls"))`
3. Routes to `core/urls.py`
4. Matches `path("", home_view, name="home")`
5. Executes `home_view()` in `core/views.py`
6. Renders `templates/home.html` (which extends `base.html`)
7. Returns HTML response to user

**Example: User signs up (/accounts/signup/)**

1. Request hits `django_project/urls.py`
2. Matches `path("accounts/", include("accounts.urls"))`
3. Routes to `accounts/urls.py`
4. Matches `path("signup/", signup_view, name="signup")`
5. If GET: Displays empty `CustomUserCreationForm`
6. If POST: Validates form, creates user, logs them in, redirects to home
7. Renders `templates/registration/signup.html`

### 2. Authentication System

**How user registration works:**

```python
# User submits signup form
→ signup_view() receives POST request
→ CustomUserCreationForm validates data
  - Username must be unique
  - Email must be valid format
  - Password must meet Django's validators:
    * Not too similar to username
    * Minimum 8 characters
    * Not entirely numeric
    * Not a common password
→ If valid: form.save() creates User object
→ login(request, user) creates session
→ Redirect to homepage (authenticated)
```

**How login works (Django built-in):**

```python
# User submits login form at /accounts/login/
→ Django's LoginView handles request
→ Authenticates username + password
→ If valid: Creates session, redirects to LOGIN_REDIRECT_URL (/)
→ If invalid: Shows error message on login page
```

**How logout works (Django built-in):**

```python
# User clicks logout link
→ Django's LogoutView handles request
→ Destroys user session
→ Redirects to LOGOUT_REDIRECT_URL (/)
```

### 3. Template Inheritance

Templates use Django's inheritance system:

```
base.html (master template)
    ├── Defines navbar
    ├── Defines container structure
    ├── Loads static CSS
    └── Provides content block
        │
        ├── home.html extends base.html
        │   └── Fills content block with homepage
        │
        ├── login.html extends base.html
        │   └── Fills content block with login form
        │
        └── signup.html extends base.html
            └── Fills content block with signup form
```

**Conditional rendering in templates:**

```django
{% if user.is_authenticated %}
    <!-- Show dashboard with personalized greeting -->
    <h2>Welcome back, {{ user.username }}!</h2>
{% else %}
    <!-- Show hero section with signup CTA -->
    <h1>Welcome to Nutrition Tracker</h1>
{% endif %}
```

### 4. Static Files Management

**How CSS files are loaded:**

1. `{% load static %}` at top of template enables static file tags
2. `{% static 'css/style.css' %}` generates URL to static file
3. Django looks in `STATICFILES_DIRS` (defined in settings.py)
4. Finds file at `static/css/style.css`
5. Serves file to browser

**CSS file organization:**

- `style.css`: Global styles (navbar, container, resets)
- `auth.css`: Authentication-specific styles (forms, buttons)
- `home.css`: Homepage-specific styles (hero, features, dashboard)

### 5. Form Processing

**CustomUserCreationForm workflow:**

```python
class CustomUserCreationForm(UserCreationForm):
    # 1. Define custom fields
    email = forms.EmailField(required=True)

    # 2. Meta class specifies model and field order
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # 3. __init__ adds CSS classes to all fields
    def __init__(self):
        # Add 'form-control' class for styling

    # 4. save() method stores email in database
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
```

**In the view:**

```python
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Bind data to form
        if form.is_valid():                          # Validate
            user = form.save()                       # Save to database
            login(request, user)                     # Create session
            return redirect('home')                  # Redirect
    else:
        form = CustomUserCreationForm()              # Empty form
    return render(request, 'registration/signup.html', {'form': form})
```

### 6. Database Models

Currently uses Django's built-in `User` model:

```
User Model (django.contrib.auth.models.User)
├── username (unique)
├── email
├── password (hashed)
├── first_name
├── last_name
├── is_staff
├── is_active
├── date_joined
└── last_login
```

### 7. URL Naming and Reverse Resolution

**Named URL patterns:**

```python
# In urls.py
path("", home_view, name="home")
path("signup/", signup_view, name="signup")
```

**Used in templates:**

```django
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'signup' %}">Sign Up</a>
<a href="{% url 'login' %}">Login</a>  <!-- From django.contrib.auth.urls -->
```

**Used in views:**

```python
return redirect('home')  # Redirects to / (home_view)
```

This allows URLs to change without breaking links throughout the application.

## Development Commands

### Running the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### Database Operations

```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser
```

### Code Formatting

```bash
# Format all Python files with Black
black .
```

### Django Shell

```bash
# Interactive Python shell with Django context
python manage.py shell
```

### Static Files

```bash
# Collect static files for production (after setting STATIC_ROOT)
python manage.py collectstatic
```

## Implementation Details

### Authentication Settings

Located in `django_project/settings.py`:

```python
# Redirect after successful login
LOGIN_REDIRECT_URL = "/"

# Redirect after logout
LOGOUT_REDIRECT_URL = "/"

# Login page for @login_required decorator
LOGIN_URL = "/accounts/login/"
```

### URL Routing Strategy

The project uses a hierarchical URL structure:

- **Root URLs** (`django_project/urls.py`): Main dispatcher
- **App URLs** (`accounts/urls.py`, `core/urls.py`): App-specific routes
- **Django Auth URLs** (`django.contrib.auth.urls`): Built-in authentication

**Important**: Both `accounts.urls` and `django.contrib.auth.urls` are mounted at `/accounts/`. Custom views in `accounts.urls` take precedence for paths defined there, while Django handles remaining auth routes (login, logout, password reset, etc.).

### Form Validation

**Password validation rules** (defined in `settings.py`):

1. `UserAttributeSimilarityValidator`: Password can't be too similar to username
2. `MinimumLengthValidator`: Minimum 8 characters
3. `CommonPasswordValidator`: Can't be a commonly used password
4. `NumericPasswordValidator`: Can't be entirely numeric

**Custom form validation** (in `CustomUserCreationForm`):

- Email format validation
- Password confirmation matching
- Username uniqueness check

### Static Files Configuration

```python
# In settings.py
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

During development, Django serves static files from `STATICFILES_DIRS`. For production, you would set `STATIC_ROOT` and run `collectstatic`.

### Security Considerations

**Current state**:
- DEBUG mode controlled by `.env` file
- SECRET_KEY is exposed in `settings.py` (should be moved to `.env`)
- ALLOWED_HOSTS set to `["*"]` (should be restricted in production)
- CSRF protection enabled (Django default)
- Password hashing enabled (Django default)

**Production TODO**:
- Move SECRET_KEY to environment variable
- Restrict ALLOWED_HOSTS to specific domains
- Set DEBUG=False
- Configure HTTPS
- Set up proper static file serving

### Message Framework

Uses Django's built-in message framework:

```python
# In views.py
from django.contrib import messages
messages.success(request, f'Account created for {username}!')
```

```django
<!-- In templates -->
{% if messages %}
    {% for message in messages %}
        <div class="message {{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}
```

## Future Enhancements

### Planned Features

1. **Nutrition Tracking**
   - Meal logging functionality
   - Food database integration
   - Calorie and macro tracking
   - Daily nutrition summaries

2. **User Profiles**
   - Profile pages with user information
   - Goal setting (weight loss, muscle gain, maintenance)
   - Personal statistics and progress tracking

3. **Analytics Dashboard**
   - Charts and graphs for nutrition data
   - Weekly/monthly reports
   - Trend analysis

4. **Food Database**
   - Custom food creation
   - Search functionality
   - Nutritional information display
   - Portion size management

5. **Social Features**
   - Share meals with friends
   - Community recipes
   - Progress sharing

### Technical Improvements

1. **Testing**
   - Unit tests for views and forms
   - Integration tests for user flows
   - Test coverage reporting

2. **API Development**
   - REST API using Django REST Framework
   - Mobile app integration
   - Third-party integrations

3. **Performance**
   - Database query optimization
   - Caching implementation
   - Static file compression

4. **UI/UX**
   - Add CSS framework (Bootstrap/Tailwind)
   - Improve mobile responsiveness
   - Add JavaScript interactivity
   - Loading states and animations

5. **Deployment**
   - Docker containerization
   - CI/CD pipeline
   - Production-ready settings
   - Database migration to PostgreSQL

## Contributing

This is a learning project. Feel free to fork and experiment with adding new features.

## License

This project is open source and available for educational purposes.

## Acknowledgments

- Built with Django 6.0
- Styled with custom CSS
- Inspired by modern nutrition tracking applications
