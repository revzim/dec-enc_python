from Crypto.Cipher import AES
import hashlib
import base64
import os
import getpass

blk_size = 32

padding = '{'

pad = lambda s: s + (blk_size - len(s) % blk_size) * padding

USER = getpass.getuser()
#hashlib.md5('goingbacktocali').hexdigest()
PW_HASH = '6f31f0f01e9c37613ce249db9dcf700a'


encode_aes = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode_aes = lambda c, e: c.decrypt(base64.b64decode(e)).strip(padding)

secret = os.urandom(blk_size)

cipher = AES.new(secret)

user = {
    'Username': '',
    'Password': ''
    }

def get_username_and_pw(u, p):
    print 'Please enter your username'
    u = raw_input()
    print 'Please enter your password'
    p = raw_input()
    user['Username'] = u
    user['Password'] = p
    return user

get_username_and_pw(user['Username'], user['Password'])
pwfile = open('usernames_passwords.txt', 'w+')
pwfile.read()

for line in pwfile:
    if line.__contains__(user):
        print 'Hello, %s welcome!' % (user['Username'])
    else:
        print 'Welcome, first timer, %s!' %s (user['Username'])
        pwfile.write('%s' % user)
        pwfile.close()

def options_for_user():
    read_message = 'read messages'
    add_message = 'add message'
    delete_message = 'delete messages'
    decode = 'decode'
    print 'Hello %s, what would you like to do?' % (user['Username'])
    print 'Your choices are: %s, %s, or %s' % (read_message, add_message, delete_message, decode)
    choice = raw_input()
    choice.lower()
    message_file = open('messages.txt', 'r')
    if choice == read_message:
        print 'Opening messages file...'
        print message_file.read()
    elif choice == add_message:
        print 'What is the message you would like to add?'
        user_input = raw_input()
        encoded = encode_aes(cipher, user_input)
        decoded = decode_aes(cipher, encoded)
        print 'Would you like the message to be added encoded or decoded?'
        choice_2 = raw_input()
        if choice_2 == 'encoded':
            print "writing encoded message to messages.txt"
            f = open('messages.txt', "w+")
            f.write('The message from %s (encoded): %s\n' %(user['Username'], encoded))
            f.close()
        else:
            print 'writing decoded message to messages.txt'
            f = open('messages.txt', 'w+')
            f.write('The message from %s (decoded): %s\n' %(user['Username'], decoded))
            f.close()
    elif choice == delete_message:
        print 'Deleting messages from messages.txt'
        f = open('messages.txt', 'r+')
        f.truncate()
    elif choice == decode:
        print 'What message would you like to decode?'
        user_inp = raw_input()
        decoded = decode_aes(cipher, user_inp)
        print 'Decoding message...'
        print 'The message %s user_inp was decoded to: %s\n' % (user_inp, decoded)
    else:
        print "Please either enter 'read messages', 'add message', or 'delete messages'"
        options_for_user()
options_for_user()
