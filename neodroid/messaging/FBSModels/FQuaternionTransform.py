# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBS

import flatbuffers


class FQuaternionTransform(object):
  __slots__ = ['_tab']

  # FQuaternionTransform
  def Init(self, buf, pos):
    self._tab = flatbuffers.table.Table(buf, pos)

  # FQuaternionTransform
  def Position(self, obj):
    obj.Init(self._tab.Bytes, self._tab.Pos + 0)
    return obj

  # FQuaternionTransform
  def Rotation(self, obj):
    obj.Init(self._tab.Bytes, self._tab.Pos + 24)
    return obj


def CreateFQuaternionTransform(builder, position_x, position_y, position_z, rotation_x, rotation_y,
                               rotation_z, rotation_w):
  builder.Prep(8, 56)
  builder.Prep(8, 32)
  builder.PrependFloat64(rotation_w)
  builder.PrependFloat64(rotation_z)
  builder.PrependFloat64(rotation_y)
  builder.PrependFloat64(rotation_x)
  builder.Prep(8, 24)
  builder.PrependFloat64(position_z)
  builder.PrependFloat64(position_y)
  builder.PrependFloat64(position_x)
  return builder.Offset()
