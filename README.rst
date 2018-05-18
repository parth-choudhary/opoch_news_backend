=====
Polls
=====

Opoch News is a simple Django app.
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "api_v1" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'api_v1',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('v1/', include('api_v1.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).
