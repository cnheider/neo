#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'cnheider'

import numpy as np

from .gym_wrapper import NeodroidGymWrapper


def make(environment_name, **kwargs):
  return NeodroidGymWrapper(environment_name=environment_name, **kwargs)


def seed(seed):
  np.random.random(seed)
