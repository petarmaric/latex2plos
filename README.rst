About
=====

Console app and Python API for automated preparation of your LaTeX paper for
submission in PLOS journals.

Major features
==============

Multiple LaTeX files workflow
-----------------------------

If your paper is organized into multiple ``.tex`` files, latex2plos will
combine them into a single, cohesive ``.tex`` file.

``\verbatiminput``
------------------

Transforms a ``\verbatiminput`` file inclusion into its equivalent
``\begin{verbatim}...\end{verbatim}`` call.

``\bibliography``
-----------------

Transforms a ``\bibliography`` file inclusion into its equivalent
``\begin{thebibliography}...\end{thebibliography}`` call.

This is done as PLOS does not allow submission of BiBTeX databases, and instead
requires the reference information to be embedded in the paper directly, as per
PLOS `LaTeX guidelines`_.

``\lstinputlisting``
--------------------

Copies over the files referenced by ``\lstinputlisting`` into the papers export
directory.

``\includegraphics``
--------------------

Copies over the figures referenced by ``\includegraphics`` into the papers
export directory. It will also transform all figures into the TIFF image format
(LZW compression, at 300 dpi) and remove/comment-out them from the papers
exported PDF, as per PLOS `LaTeX guidelines`_ and `figures guidelines`_.

.. _`LaTeX guidelines`: https://journals.plos.org/plosone/s/latex
.. _`figures guidelines`: https://journals.plos.org/plosone/s/figures

Examples
========

An example paper, based on the PLOS LaTeX template, has been provided in the
``example`` directory to verify the latex2plos features listed above. To try it
out yourself, just clone the projects repository and run::

    $ pip install -e .[dev]
    $ cd example
    $ make clean export

Afterwards you can compare the contents of the ``example`` and
``example/export`` directories.

Installation
============

To install latex2plos run::

    $ pip install latex2plos

Console app usage
=================

Quick start::

    $ latex2plos <filename>

Show help::

    $ latex2plos --help

Python API usage
================

Quick start::

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")

    >>> import os
    >>> os.chdir('example')

    >>> from latex2plos.main import latex2plos
    >>> latex2plos('paper.tex')

Contribute
==========

If you find any bugs, or wish to propose new features `please let us know`_.

If you'd like to contribute, simply fork `the repository`_, commit your changes
and send a pull request. Make sure you add yourself to `AUTHORS`_.

.. _`please let us know`: https://bitbucket.org/petar/latex2plos/issues/new
.. _`the repository`: http://bitbucket.org/petar/latex2plos
.. _`AUTHORS`: https://bitbucket.org/petar/latex2plos/src/default/AUTHORS
