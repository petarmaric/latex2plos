About
=====

Console app and Python API for automated preparation of your LaTeX paper for
submission in PLOS journals.

Please cite this project in your papers::

    @misc{latex2plos,
      title={{latex2plos public code repository}},
      author={Mari{\'c}, Petar},
      year={2019},
      url={https://bitbucket.org/petar/latex2plos/},
    }

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

An example paper, based on the `PLOS LaTeX template`_, has been provided in the
`template4plos repository`_ to verify the latex2plos features listed above.

.. _`PLOS LaTeX template`: https://journals.plos.org/plosone/s/latex
.. _`template4plos repository`: http://bitbucket.org/petar/template4plos

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
