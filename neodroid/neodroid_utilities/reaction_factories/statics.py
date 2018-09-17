#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from neodroid.neodroid_utilities import ActionSpace, ObservationSpace

__author__ = 'cnheider'


def flattened_observation(message):
  # flat = np.array([np.hstack([obs.observation_value]).flatten() for obs in message.observers.values() if
  # obs.observation_value is not None and type(obs.observation_value) is not _io.BytesIO])
  # flatter = np.hstack(flat).flatten()
  # flatter = np.hstack(flatter).flatten()
  # flatest = np.nan_to_num(flatter).tolist()
  obs = message.observables
  return obs


def construct_action_space(environment_description):
  motion_spaces = []
  for actor in environment_description.actors.values():
    for motor in actor.motors.values():
      motion_spaces.append(motor.motion_space)
  action_space = ActionSpace()
  action_space.parse_valid_inputs(motion_spaces)
  return action_space


def construct_observation_space(state):
  observation_space = ObservationSpace()

  observation_space.parse_observation_space(state)
  return observation_space