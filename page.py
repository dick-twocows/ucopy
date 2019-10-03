import array

from struct import Struct

PAYLOAD_SIZE = 16

with open('/home/dick/bumble.yml', mode='rb') as file:
    raw = file.read(16)

print(type(raw))

empty_payload = bytes(PAYLOAD_SIZE)

page_meta = Struct('HH16c')

page_data = array.array('b', [0] * page_meta.size)

print(page_meta)

print(page_meta.size)

page_meta.pack_into()
print(page_data)

unpacked = page_meta.unpack_from(page_data, 0)
print(unpacked)
