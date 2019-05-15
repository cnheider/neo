# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBS

import flatbuffers

class FQT(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFQT(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FQT()
        x.Init(buf, n + offset)
        return x

    # FQT
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FQT
    def Transform(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .FQuaternionTransform import FQuaternionTransform
            obj = FQuaternionTransform()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def FQTStart(builder): builder.StartObject(1)
def FQTAddTransform(builder, transform): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(transform), 0)
def FQTEnd(builder): return builder.EndObject()