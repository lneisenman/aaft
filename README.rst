====
aaft
====

.. image:: https://travis-ci.org/lneisenman/aaft.svg?branch=master
  :target: https://travis-ci.org/lneisenman/aaft

.. image:: https://coveralls.io/repos/lneisenman/aaft/badge.png
  :target: https://coveralls.io/r/lneisenman/aaft


This is a python translation of the Matlab code from the `MATS-Toolkit <http://eeganalysis.web.auth.gr/>`_.
by Dimitris Kugiumtzis and Alkiviadis Tsimpiris

I obtained the code from the `Meaney lab <http://www.seas.upenn.edu/~molneuro/fluorosnnap.html>`_
as part of an effort to replicate the data analysis described in Patel et. al.
J Neurosci 34:4200 2014 and Patel et. al. Ann Biomed Eng. 40:23 2012.

The original Matlab code is included in the docs


Quickstart
==========

.. code-block:: py3

   import aaft
   surrogate = aaft.AAFTsur(data)

