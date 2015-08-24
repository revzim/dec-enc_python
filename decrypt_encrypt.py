from Crypto.Cipher import AES
import base64
import os

blk_size = 32

padding = '{'

pad = lambda s: s + (blk_size - len(s) % blk_size) * padding

encode_aes = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode_aes = lambda c, e: c.decrypt(base64.b64decode(e)).strip(padding)

secret = os.urandom(blk_size)

cipher = AES.new(secret)

encoded = Encode(cipher, 'secret messaged: poop')
print 'Encrypted:', econded

#decode
decoded = DecodeAES(cipher, encoded)
print 'Decrypted string:', decoded


