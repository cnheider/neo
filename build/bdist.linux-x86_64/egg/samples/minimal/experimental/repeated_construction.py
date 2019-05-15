#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cnheider'
__doc__ = ''

import neodroid
import contextlib

for i in range(100):
  with neodroid.connect() as env, contextlib.suppress(KeyboardInterrupt):
    print(i)
    env.react()
