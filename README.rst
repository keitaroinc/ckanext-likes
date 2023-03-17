.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org//ckanext-likes.svg?branch=master
    :target: https://travis-ci.org//ckanext-likes

.. image:: https://coveralls.io/repos//ckanext-likes/badge.svg
  :target: https://coveralls.io/r//ckanext-likes

.. image:: https://pypip.in/download/ckanext-likes/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-likes/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-likes/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-likes/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-likes/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-likes/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-likes/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-likes/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-likes/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-likes/
    :alt: License

=============
ckanext-likes
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

NOTE:
Extension is works on CKAN 2.8x if pulled from master branch 
And it works on CKAN 2.9.x if pulled from dgm-ckan2.9 branch

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-likes:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-likes Python package into your virtual environment::

     pip install ckanext-likes

3. Add ``likes`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

------------------------
Development Installation
------------------------

To install ckanext-likes for development, activate your CKAN virtualenv, make sure you are pulling from the right branch depending on what ckan version you are running.
do::

    git clone https://github.com//ckanext-likes.git
    cd ckanext-likes
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture test.ini --with-coverage --cover-package=ckanext.likes --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-likes on PyPI
---------------------------------

ckanext-likes should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-likes. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-likes
----------------------------------------

ckanext-likes is availabe on PyPI as https://pypi.python.org/pypi/ckanext-likes.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags