===================
advent of code 2015
===================

Python 3.10 edition

Notes on the repo
=================

* Package management is done with `Poetry <https://python-poetry.org/>`_
* Utils in the ``utils/`` directory can/should be used to bootstrap new directories/files for solutions
* Some parts of this repo are specific to the problems I receive (e.g. this won't entirely scale for non-me people)

    * utils in the ``utils/`` derectory require `advent-of-code-data <https://github.com/wimglenn/advent-of-code-data>`_, which relies on my session cookie. So don't use those unless you are me.
    * To make refactoring safer, after completing a problem, a test will be added asserting that my input produces the right output. If you aren't me, your input/output probably don't match.

Getting started
===============

#. Make sure you have `Poetry <https://python-poetry.org/>`_ installed
#. ``poetry install``
#. If you are using utils that use ``advent-of-code-data``, have my adventofcode session cookie stored in ``~/.config/aocd/token`` (note that this may be tricky if you are not me)

Commands to run
===============

+---------------------------------+--------------------------------------------------------------------------------------------+
| Purpose                         | Command                                                                                    |
+=================================+============================================================================================+
| Run all tests                   | ``poetry run python -m unittest``                                                          |
+---------------------------------+--------------------------------------------------------------------------------------------+
| Run specific test file          | ``poetry run python -m unittest <FILE>``                                                   |
+---------------------------------+--------------------------------------------------------------------------------------------+
| Run solution file               | ``poetry run python -m src.day_<DAY>.<PART>`` (where ``DAY`` has a leading zero if needed) |
+---------------------------------+--------------------------------------------------------------------------------------------+
| Format code                     | ``poetry run python -m black . --target-version py310``                                    |
+---------------------------------+--------------------------------------------------------------------------------------------+
| Bootstrap files for new problem | ``poetry run python -m utils.create_files -d <DAY> -p <PART>``                             |
+---------------------------------+--------------------------------------------------------------------------------------------+
| Submit solution                 | ``poetry run python -m utils.submit -d <DAY> -p <PART>``                                   |
+---------------------------------+--------------------------------------------------------------------------------------------+

Handy Links
===========

* `AoC <https://adventofcode.com/2015>`_
* `Repo <https://github.com/tyler-hoffman/aoc-2015>`_
