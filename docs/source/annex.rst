#####
Annex
#####

************************
Parsing the Database URL
************************

For example, our eventual Railway database URL may look something like this:
``postgresql://postgres:mypassword123@containers-us-west-123.railway.app:5432/railway``

We can then use **dj-database-url** to split out the above string into various items
within a dictionary. We can verify this with a simple script:

.. code-block:: python

    import dj_database_url


    remote_db_url = (
        'postgresql://postgres:mypassword123'
        '@containers-us-west-123.railway.app:5432/railway'
    )

    remote_db = dj_database_url.parse(remote_db_url)
    print(remote_db)

Running the code above would return the following output:

.. code-block:: python
    
    {'NAME': 'railway', 'USER': 'postgres',
    'PASSWORD': 'mypassword123', 'HOST': 'containers-us-west-123.railway.app',
    'PORT': 5432, 'CONN_MAX_AGE': 0, 'CONN_HEALTH_CHECKS': False,
    'ENGINE': 'django.db.backends.postgresql'}

Notice that, in addition to the expected key-value pairs from our string,
the ``dj-database-url`` actually adds in standard items.
For example, the ``ENGINE`` key is set to the usual value of
``django.db.backends.postgresql`` automatically for us.

We would be able to get the same effect as above using the config method instead:

    .. code-block:: python

        import dj_database_url
        remote_db = dj_database_url.config()
        print(remote_db)
        {'NAME': 'railway' ... 'ENGINE': 'django.db.backends.postgresql'}

We then add the above dictionary to our ``DATABASE`` dictionary in
:file:`settings.py`` under the alias of ``default``: 

.. code-block:: python

    DATABASES = {'default': dj_database_url.config()}

************************
Running Gunicorn Locally
************************

If on a Unix-like system - i.e. **not** Windows - we can run a web server locally
to test it is working by navigating to the base directory of our project and
running the following command:

.. code-block:: console

    gunicorn website.wsgi

The app by default should be running on `localhost:8000 <http:localhost:8000>`_.

.. warning::

    Gunicorn cannot run on Windows

************************
Methods to Store Secrets
************************

There are 2 ways to do this:

#.  store secrets in an untracked file (such as a JSON file)

    *   preferably located outside the repo directory

    *   only authorised collaborators are able to know its contents

#.  use environment variables

    *   environment variables are values that are defined outside of a program
        but are able to alter the behaviour

Although viable locally, the first method is not possible with many PaaS
- including Railway - as they do not allow for single files to be "uploaded"
and exist alongside your app
