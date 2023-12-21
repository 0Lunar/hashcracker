#!/usr/bin/python3
from hashlib import *
import sys

def checkargs():
    if len(sys.argv) < 3:
        print("usage: python3 hashcracker.py <format> <hash> <wordlist>\nexample: python3 hashcracker.py sha256 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 /usr/share/wordlists/rockyou.txt")
        return 1
    return 0

def crack_sha256(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = sha256(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

def crack_md5(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = md5(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

def crack_sha1(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = sha1(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

def crack_sha224(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = sha224(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

def crack_sha384(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = sha284(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

def crack_sha512(wordlist, rawhash):
    found = 0
    line = wordlist.readline()
    while found == 0 and line != "":
        encoded = sha512(line[:-1].encode('utf-8')).hexdigest()
        if encoded == rawhash:
            print("\npassword found: " + line[:-1])
            found = 1
        else:
            line = wordlist.readline()
    if found == 0:
        print("password non trovata")

if __name__ == "__main__":
    if checkargs() != 1:
        hashformat = sys.argv[1]
        rawhash = sys.argv[2]
        try:
            wordlist = open((sys.argv[3]), "r")
        except:
            print("Error, wordlist not found")
            sys.exit()
        if hashformat == "sha256":
            crack_sha256(wordlist, rawhash)
        elif hashformat == "md5":
            crack_md5(wordlist, rawhash)
        elif hashformat == "sha1":
            crack_sha1(wordlist, rawhash)
        elif hashformat == "sha224":
            crack_sha224(wordlist, rawhash)
        elif hashformat == "sha384":
            crack_sha384(wordlist, rawhash)
        elif hashformat == "sha512":
            crack_sha512(wordlist, rawhash)
        else:
            print("Error, invalid hash format")
