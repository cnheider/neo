# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Reaction

import flatbuffers


class FReactions(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsFReactions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FReactions()
        x.Init(buf, n + offset)
        return x

    # FReactions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FReactions
    def Reactions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FReaction import FReaction

            obj = FReaction()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FReactions
    def ReactionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FReactions
    def ApiVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FReactions
    def SimulatorConfiguration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .FSimulatorConfiguration import FSimulatorConfiguration

            obj = FSimulatorConfiguration()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FReactions
    def Close(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return False


def FReactionsStart(builder):
    builder.StartObject(4)


def FReactionsAddReactions(builder, reactions):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(reactions), 0
    )


def FReactionsStartReactionsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def FReactionsAddApiVersion(builder, apiVersion):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(apiVersion), 0
    )


def FReactionsAddSimulatorConfiguration(builder, simulatorConfiguration):
    builder.PrependStructSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(simulatorConfiguration), 0
    )


def FReactionsAddClose(builder, close):
    builder.PrependBoolSlot(3, close, 0)


def FReactionsEnd(builder):
    return builder.EndObject()
