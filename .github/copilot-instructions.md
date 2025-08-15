# Copilot Instructions for ecommerce_project

## Project Overview
This is a multi-app Django project for e-commerce, containing the following major components:
- `store`: Product catalog, shopping cart, and store logic
- `accounts`: User authentication and profile management
- `dashboard`: Admin and analytics dashboard
- `newsletter`: Email/newsletter management
- `crm_api`: API for CRM integration and external communication
- `blog`: Content/blogging system

All apps are registered in `INSTALLED_APPS` in `ecommerce_project/settings.py`.

## Architecture & Data Flow
- Each app is self-contained with its own models, views, templates, and migrations.
- Shared templates are in `/templates/`, while app-specific templates are in `app/templates/app/`.
- Static files are organized per app in `app/static/app/` and globally in `/static/`.
- The main configuration is in `ecommerce_project/settings.py`.
- URLs are routed via `ecommerce_project/urls.py`, which includes each app's `urls.py`.

## Developer Workflows
- **Run server:** `python manage.py runserver`
- **Migrate DB:** `python manage.py makemigrations && python manage.py migrate`
- **Run tests:** `python manage.py test`
- **Create superuser:** `python manage.py createsuperuser`
- **Static files:** Use `python manage.py collectstatic` for production

## Conventions & Patterns
- Templates use Django's `{% extends %}` and `{% block %}` for inheritance.
- Models are defined per app in `models.py`.
- Views are class-based or function-based, found in `views.py`.
- Forms (where used) are in `forms.py`.
- App-specific static and template folders follow Django's recommended structure.
- API logic and permissions are in `crm_api/` (see `serializers.py`, `permissions.py`).

## Integration Points
- CRM integration is handled via `crm_api/`.
- Newsletter/email logic is in `newsletter/`.
- User management is in `accounts/`.

## External Dependencies
- Uses Django (see `requirements.txt` if present).
- SQLite is default DB (see `settings.py`).

## Key Files & Directories
- `ecommerce_project/settings.py`: Main config
- `ecommerce_project/urls.py`: URL routing
- `manage.py`: Entrypoint for CLI
- Each app's `models.py`, `views.py`, `urls.py`, `templates/`, `static/`

---

**If you add new apps, update `INSTALLED_APPS` and create corresponding folders for templates/static.**

For questions or unclear conventions, ask the user for clarification.
