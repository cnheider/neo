# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Reaction

import flatbuffers

class FlatBufferReaction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFlatBufferReaction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FlatBufferReaction()
        x.Init(buf, n + offset)
        return x

    # FlatBufferReaction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FlatBufferReaction
    def Motions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FlatBufferMotion import FlatBufferMotion
            obj = FlatBufferMotion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FlatBufferReaction
    def MotionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FlatBufferReaction
    def Reset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def FlatBufferReactionStart(builder): builder.StartObject(2)
def FlatBufferReactionAddMotions(builder, motions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(motions), 0)
def FlatBufferReactionStartMotionsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FlatBufferReactionAddReset(builder, reset): builder.PrependBoolSlot(1, reset, 0)
def FlatBufferReactionEnd(builder): return builder.EndObject()