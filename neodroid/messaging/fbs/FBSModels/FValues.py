# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBS

import flatbuffers


class FValues(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsFValues(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FValues()
        x.Init(buf, n + offset)
        return x

    # FValues
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FValues
    def Vals(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Float64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # FValues
    def ValsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # FValues
    def ValsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def FValuesStart(builder):
    builder.StartObject(1)


def FValuesAddVals(builder, vals):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(vals), 0
    )


def FValuesStartValsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def FValuesEnd(builder):
    return builder.EndObject()
