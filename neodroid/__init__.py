#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from neodroid.neodroid_environments import NeodroidEnvironments

__author__ = 'cnheider'
__version__ = None
'''
.. module:: neodroid
   :platform: Unix, Windows
   :synopsis: An API for communicating with a Unity Game process.

.. moduleauthor:: Christian Heider Nielsen <chrini13@student.aau.dk>


'''

from .version import __version__


_environments = None


def draw_logo():
  with open('data/.ascii') as f:
    print(f.read())


def make(environment_name='', clones=0, *args, **kwargs):
  global _environments
  _environments = NeodroidEnvironments(environment_name=environment_name, clones=clones, *args, **kwargs)
  return _environments


def seed(random_seed):
  import numpy as np
  np.random.seed(random_seed)


def get_available_environments():
  return environments


@property
def environments():
  return _environments
