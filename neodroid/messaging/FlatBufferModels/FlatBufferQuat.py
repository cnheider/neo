# automatically generated by the FlatBuffers compiler, do not modify

# namespace: State

import flatbuffers


class FlatBufferQuat(object):
  __slots__ = ['_tab']

  # FlatBufferQuat
  def Init(self, buf, pos):
    self._tab = flatbuffers.table.Table(buf, pos)

  # FlatBufferQuat
  def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags,
                                    self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))

  # FlatBufferQuat
  def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags,
                                    self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

  # FlatBufferQuat
  def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags,
                                    self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))

  # FlatBufferQuat
  def W(self): return self._tab.Get(flatbuffers.number_types.Float32Flags,
                                    self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))


def CreateFlatBufferQuat(builder, x, y, z, w):
  builder.Prep(4, 16)
  builder.PrependFloat32(w)
  builder.PrependFloat32(z)
  builder.PrependFloat32(y)
  builder.PrependFloat32(x)
  return builder.Offset()
