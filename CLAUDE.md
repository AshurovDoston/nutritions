# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 6.0 web application for nutrition tracking. The project uses python-decouple for environment configuration and SQLite as the database.

## Development Commands

### Running the Development Server
```bash
python manage.py runserver
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Code Formatting
```bash
# Format code with Black
black .
```

### Django Shell
```bash
# Interactive Python shell with Django context loaded
python manage.py shell
```

## Project Architecture

### URL Routing Structure
The project uses a hierarchical URL configuration:

- **Root URLs** (`django_project/urls.py`): Main URL dispatcher
  - `/admin/` → Django admin interface
  - `/accounts/` → Custom account views (`accounts.urls`)
  - `/accounts/` → Django auth views (login, logout, password reset)
  - `/` → Core application views (`core.urls`)

**URL Conflict**: Both `accounts.urls` and `django.contrib.auth.urls` are mounted at `/accounts/`. The custom account views in `accounts/urls.py` will take precedence for paths defined there, but Django auth views handle authentication routes.

### Application Structure

**accounts app**: User account-related functionality
- Currently contains placeholder views (account_view, current_datetime_view)
- Path: `/accounts/` → `account_view`
- Path: `/accounts/time/` → `current_datetime_view`

**core app**: Main application logic
- Contains the home view
- Path: `/` → `home_view`

### Configuration

**Environment Variables**: Managed via python-decouple with `.env` file
- `DEBUG`: Controls debug mode (default: False)

**Settings** (`django_project/settings.py`):
- Templates directory: `BASE_DIR / "templates"`
- Database: SQLite (`db.sqlite3`)
- Installed apps: Standard Django apps + `accounts`
- Note: `core` app exists but is not registered in `INSTALLED_APPS`

### Templates

Base template system:
- `templates/base.html`: Base template with title block and content block
- `templates/home.html`: Extends base template
- `templates/registration/`: Contains empty login.html and signup.html templates

## Important Notes

- The `core` app is functional and has URL routing but is NOT listed in `INSTALLED_APPS`. Add it to `INSTALLED_APPS` in settings.py if it needs models, templates, or admin registration.
- Virtual environment is located at `.venv/`
- Static files are not yet configured (STATIC_ROOT not set)
- The SECRET_KEY in settings.py is exposed and should be moved to environment variables for production
