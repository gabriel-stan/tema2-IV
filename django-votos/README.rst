=====
Votos
=====

Votos es una simple aplicacion Django para gestionar un sistema de votacion de las empresas en los que hacen practicas los alumnos.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "votos" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'votos',
    )

2. !!Not yet supported!! Include the polls URLconf in your project urls.py like this::

    url(r'^votos/', include('votos.urls')),

3. Run `python manage.py migrate` to create the votos models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. !!Not yet supported!! Visit http://127.0.0.1:8000/polls/ to participate in the poll.
