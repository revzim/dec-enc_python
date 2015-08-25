from Crypto.Cipher import AES
import base64
import os
import getpass

blk_size = 32

padding = '{'

pad = lambda s: s + (blk_size - len(s) % blk_size) * padding

encode_aes = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode_aes = lambda c, e: c.decrypt(base64.b64decode(e)).strip(padding)

secret = os.urandom(blk_size)

cipher = AES.new(secret)

print 'Please Input your message:',
user_input = raw_input()

encoded = encode_aes(cipher, user_input)
print 'You\'re encrypted message:', encoded

#decode
decoded = decode_aes(cipher, encoded)
#print 'Decrypted string:', decoded

print 'Do you want to decrypt your message?'
user_in = raw_input()

user_in.lower()

if user_in == 'yes':
    print 'Please enter your username:'
    uname = raw_input()
    if uname == getpass.getuser():
        file = open('messages.txt', "w+")
        file.write('The message from %s: %s\n' % (uname, decoded))
        file.close()
        print "The file was written to messages.txt, please look to find your message decoded"
else:
    print 'Ok, have a good day!'


