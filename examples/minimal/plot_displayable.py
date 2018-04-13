import neodroid.wrappers.formal_wrapper as neo
from neodroid import messaging
import numpy as np


def main():
  _environment = neo.make('maze', connect_to_running=True)

  i = 0
  while _environment.is_connected:
    actions = _environment.action_space.sample()
    p = '.' * (i%100)
    i += 1
    d1 = messaging.N.Displayable('TextMeshDisplayer', f'Hello from Python{p}')
    d2 = messaging.N.Displayable('TextDisplayer', f'YEAH {i}')
    d3 = messaging.N.Displayable('BarDisplayer', (i%1000)/1000.0)
    d4 = messaging.N.Displayable('ScatterPlotDisplayer',  np.cos(np.arange(0, 1, step=0.001)*i))
    r = messaging.N.Reaction(displayables=[d1, d2, d3,d4],serialised_message='YEEEEEEEEP')
    _, reward, terminated, info = _environment.act(r)
    if terminated:
      print(info.termination_reason)


if __name__ == '__main__':
  main()