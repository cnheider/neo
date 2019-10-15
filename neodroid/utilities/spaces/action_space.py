#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from typing import Sequence

from neodroid.utilities.spaces.range import Range
from neodroid.utilities.spaces.space import Space
from neodroid.utilities.transformations.encodings import signed_ternary_encoding

__author__ = 'Christian Heider Nielsen'

import numpy


class ActionSpace(Space):

  def parse_action_space(self, action_spaces: Sequence[Range], motion_names):
    self._ranges = action_spaces
    self._names = motion_names

  def sample(self):
    actions = []
    for valid_input in self._ranges:
      sample = numpy.random.uniform(valid_input.min_unnorm, valid_input.max_unnorm, 1)
      actions.append(numpy.round(sample, valid_input.decimal_granularity))
    return actions

  def validate(self, actions):
    for i in range(len(actions)):
      clipped = numpy.clip(actions[i],
                           self._ranges[i].min_unnorm,
                           self._ranges[i].max_unnorm,
                           )
      actions[i] = numpy.round(clipped, self._ranges[i].decimal_granularity)
    return actions

  @property
  def num_binary_discrete_actions(self) -> int:
    return sum([r.discrete_steps for r in self._ranges])

  def discrete_ternary_one_hot_sample(self):
    idx = numpy.random.randint(0, self.num_actuators)
    zeros = numpy.zeros(self.num_ternary_actions)
    if len(self._ranges) > 0:
      sample = numpy.random.uniform(self._ranges[idx].min_unnorm,
                                    self._ranges[idx].max_unnorm,
                                    1
                                    )
      if sample > 0:
        zeros[idx] = 1
      else:
        zeros[idx + self.num_actuators] = 1
    return zeros

  def discrete_binary_one_hot_sample(self):
    idx = numpy.random.randint(0, self.num_actuators)
    zeros = numpy.zeros(self.num_binary_actions)
    if len(self._ranges) > 0:
      sample = numpy.random.uniform(self._ranges[idx].min_unnorm,
                                    self._ranges[idx].max_unnorm,
                                    1
                                    )
      if sample > 0:
        zeros[idx] = 1
      else:
        zeros[idx + self.num_actuators] = 1
    return zeros

  def signed_one_hot_sample(self):
    num = self.num_binary_actions
    return random.randrange(num)

  def discrete_one_hot_sample(self):
    idx = numpy.random.randint(0, self.num_actuators)
    zeros = numpy.zeros(self.num_actuators)
    if len(self._ranges) > 0:
      val = numpy.random.random_integers(
        int(self._ranges[idx].min_unnorm),
        int(self._ranges[idx].max_unnorm),
        1,
        )
      zeros[idx] = val
    return zeros

  def discrete_sample(self):
    idx = numpy.random.randint(0, self.num_binary_actions)
    return idx

  def one_hot_sample(self):

    idx = numpy.random.randint(0, self.num_actuators)
    zeros = numpy.zeros(self.num_actuators)
    if len(self._ranges) > 0:
      zeros[idx] = 1
    return zeros

  @property
  def num_actuators(self):
    return self.n

  @property
  def num_binary_actions(self):
    return self.n * 2

  @property
  def num_ternary_actions(self):
    return self.n * 3

  def ternary_discrete_action_from_idx(self, idx):
    return signed_ternary_encoding(size=self.n, index=idx)

  def binary_discrete_action_from_idx(self, idx):
    return signed_ternary_encoding(size=(self.n * 2) / 3, index=idx)


if __name__ == '__main__':
  acs = ActionSpace([Range(min_value=0, max_value=3, decimal_granularity=2),
                     Range(min_value=0, max_value=2, decimal_granularity=1)])
  print(acs, acs.low, acs.high, acs.decimal_granularity, acs.num_binary_discrete_actions, acs.shape)

  acs = ActionSpace([Range(min_value=0, max_value=3, decimal_granularity=2, normalised=False),
                     Range(min_value=0, max_value=2, decimal_granularity=1, normalised=False)])
  print(acs, acs.low, acs.high, acs.decimal_granularity, acs.num_binary_discrete_actions, acs.shape)

  acs = ActionSpace([Range(min_value=0, max_value=1, decimal_granularity=0, normalised=False)])
  print(acs, acs.low, acs.high, acs.decimal_granularity, acs.num_binary_discrete_actions, acs.shape)
