# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Reaction

import flatbuffers

class FlatBufferMotion(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFlatBufferMotion(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FlatBufferMotion()
        x.Init(buf, n + offset)
        return x

    # FlatBufferMotion
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FlatBufferMotion
    def ActorName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # FlatBufferMotion
    def MotorName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # FlatBufferMotion
    def Strength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def FlatBufferMotionStart(builder): builder.StartObject(3)
def FlatBufferMotionAddActorName(builder, actorName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(actorName), 0)
def FlatBufferMotionAddMotorName(builder, motorName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(motorName), 0)
def FlatBufferMotionAddStrength(builder, strength): builder.PrependFloat32Slot(2, strength, 0.0)
def FlatBufferMotionEnd(builder): return builder.EndObject()