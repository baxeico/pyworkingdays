pyworkingdays
=============

This package let you perform simple date arithmetics on standard
*datetime.date* objects taking into account working days (weekend,
holidays).

Python compatibility
--------------------

The package is continuosly tested on Python 2.7, 3.2, 3.3 and 3.4.

.. image:: https://travis-ci.org/baxeico/pyworkingdays.svg?branch=master  
    :target: https://travis-ci.org/baxeico/pyworkingdays


Requirements
------------

`python-dateutil <https://pypi.python.org/pypi/python-dateutil>`_

Pros
----

The API is simple and clear and the implementation is straightforward.

Localization - that is handling holidays for different countries - is
built-in and easy to extend.

Cons
----

The implementation is not very optimized and it is expected to be used
for small date deltas.

Currently only italian holidays are implemented, but feel free to send
pull requests for your country of interest.

Examples:
---------

Check if a date is a working day
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import date
    import workingdays

    is_today_working = workingdays.is_workingday(date.today())

Add a number of working days to a certain date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import date
    import workingdays

    two_workingdays_from_today = workingdays.add(date.today(), 2)

Count the number of working days between two dates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import date
    import workingdays

    workingdays_between_dates = workingdays.diff(date(2015, 3, 27), date(2015, 3, 25))

Compute the next working day starting from a certain date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import date
    import workingdays

    workingday_after_today = workingdays.next(date.today())

Use a different localization, that is taking into account holidays for a particular country
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import date
    import workingdays
    import workingdays.l10n.it

    workingdays.is_workingday = workingdays.l10n.it.is_workingday

    workingday_after_today_in_italy = workingdays.next(date.today())

**See file test.py in the source directory to have a better idea of the
API and the expected results.**
