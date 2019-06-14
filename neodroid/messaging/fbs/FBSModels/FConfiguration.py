# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Reaction

import flatbuffers


class FConfiguration(object):
  __slots__ = ['_tab']

  @classmethod
  def GetRootAsFConfiguration(cls, buf, offset):
    n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
    x = FConfiguration()
    x.Init(buf, n + offset)
    return x

  # FConfiguration
  def Init(self, buf, pos):
    self._tab = flatbuffers.table.Table(buf, pos)

  # FConfiguration
  def ConfigurableName(self):
    o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
    if o != 0:
      return self._tab.String(o + self._tab.Pos)
    return None

  # FConfiguration
  def ConfigurableValue(self):
    o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
    if o != 0:
      return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
    return 0.0


def FConfigurationStart(builder): builder.StartObject(2)


def FConfigurationAddConfigurableName(builder, configurableName): builder.PrependUOffsetTRelativeSlot(0,
                                                                                                      flatbuffers.number_types.UOffsetTFlags.py_type(
                                                                                                          configurableName),
                                                                                                      0)


def FConfigurationAddConfigurableValue(builder, configurableValue): builder.PrependFloat64Slot(1,
                                                                                               configurableValue,
                                                                                               0.0)


def FConfigurationEnd(builder): return builder.EndObject()