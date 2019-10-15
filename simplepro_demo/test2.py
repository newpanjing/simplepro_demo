# import struct
# import base64
#
# f = open('/Users/panjing/dev/simplepro/simplepro/simpepro.lic', 'rb')
# buffer = f.read()
# a, = struct.unpack('h', buffer[0:2])
# b, = struct.unpack('h', buffer[2:4])
# d1 = buffer[4:a + 4]
#
# d2 = base64.b64decode(buffer[a + 4:])
# print(d1)
# print(d2)
