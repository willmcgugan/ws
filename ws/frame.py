from __future__ import print_function


class Opcode(object):
    continuation = 0
    text = 1
    binary = 2
    reserved1 = 3
    reserved2 = 4
    reserved3 = 5
    reserved4 = 6
    reserved5 = 7
    close = 8
    ping = 9
    pong = 0xA
    reserved6 = 0xB
    reserved7 = 0xC
    reserved8 = 0xD
    reserved9 = 0xE
    reserved10 = 0xF


class Frame(object):

    def __init__(self, opcode, payload=b'', masking_key=None, fin=0, rsv1=0, rsv2=0, rsv3=0):
        self.fin = fin
        self.rsv1 = rsv1
        self.rsv2 = rsv2
        self.rsv2 = rsv3
        self.opcode = opcode
        self.mask = 0
        self.payload_length = len(payload)
        self.masking_key = masking_key
        self.payload_data = payload

    @property
    def is_control(self):
        return self.opcode >= 8

    @property
    def is_binary(self):
        return self.opcode == Opcode.binary

    @property
    def is_text(self):
        return self.opcode == Opcode.text

    @property
    def is_continuation(self):
        return self.opcode == Opcode.continuation

    @property
    def is_ping(self):
        return self.opcode == Opcode.ping

    @property
    def is_pong(self):
        return self.opcode == Opcode.pong

    @property
    def is_close(self):
        return self.opcode == Opcode.close
