#This is the CipherSabre2 implementation used by the TauNet system.
#Copyright (c) 2015 Matthew Tighe

import sys, string, random

def rc4(n, r, k):
    l = len(k)
    j, state = 0, range(256)
    for x in range(r):
        for i in range(256):
            j = (j + state[i] + k[i % l]) % 256
            state[i], state[j] = state[j], state[i]
    
    j, keystream = 0, [] 
    #for i in range(n):
     #   keystream[i] = 0
    for i in range(n):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        keystream.append(state[(state[i] + state[j]) % 256])
    return keystream

def encrypt(m, k):
    n = len(m)
    iv = ''.join(random.choice(string.ascii_letters) for x in range(10))
    k += iv
    key = []
    for i in range(len(k)):
        key.append(ord(k[i]))
    keystream = rc4(n, 20, key)
    ciphertext = []
    for i in range(10):
        ciphertext.append(iv[i])
    for i in range(n):
        ciphertext.append(ord(m[i]) ^ keystream[i])
        ciphertext[i+10] = chr(ciphertext[i+10])

    return ''.join(ciphertext)

def decrypt(m, k):
    n = len(m)
    iv = m[:10]
    m = m[10:]
    k = k + iv
    key = []
    for i in range(len(k)):
        key.append(ord(k[i]))
    keystream = rc4(n - 10, 20, key)

    plaintext = []
    for i in range(n - 10):
        plaintext.append(ord(m[i]) ^ keystream[i])
        plaintext[i] = chr(plaintext[i])

    return ''.join(plaintext)
