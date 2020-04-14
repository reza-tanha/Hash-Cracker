#!/usr/bin/python3
import hashlib, time, argparse
from colorama import Fore
from colorama import init
init(autoreset = True)
from threading import Thread


banner_t = """     

            +++++++++++++++++++++++++++++++++++++++++++++++++++++
            #    Hash Cracker - Md5 , Sha1 , Sha224 ,           #
            #                 Sha256 , Sha384 , Sha512          #
            #    Version 1.0                                    #
            #    Github : https://github.com/reza-tanha/        #
            #    Telegram : T.me/S3CURITY_GARY                  #
            #    Youtube : https://bit.ly/2yas3rm               #
            #    Code By : Haji (Reza)                          #
            #                                                   #
            #    Gray Security Team                             #
            +++++++++++++++++++++++++++++++++++++++++++++++++++++

    """
def banner(txt):
    for x in txt:
        print(Fore.LIGHTYELLOW_EX+x, end='', flush=True)
        time.sleep(0.0003)
    print()


def a_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', dest='WORDLIST' ,help='WordList ' )
    parser.add_argument('-f', dest='HASHLIST' ,help='Hash List ' )
    parser.add_argument('-H', dest='HASH', help='One Hash For Crack ')
    parser.add_argument('-c', dest='COMBO', help='Combo For Crack ')
    parser.add_argument('-t', dest='TYPE', help='Type Hash , (md5, sha1, sha256, sha512)')
    return parser.parse_args()

def md5_crack(password, hash):

    try :
        res = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        # res = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")


def sha1_crack(password, hash):
    try:
        res = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        # res = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")

def sha224_crack(password, hash):
    try:
        res = hashlib.sha224(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")

def sha256_crack(password, hash):
    try:
        res = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")

def sha384_crack(password, hash):
    try:
        res = hashlib.sha384(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")

def sha512_crack(password, hash):
    try:
        res = hashlib.sha512(password.strip().encode('utf-8')).hexdigest()
        if ":" in hash:
            if res == hash.split(":")[1]:
                print(Fore.GREEN + hash.split(":")[0] + ":" + Fore.LIGHTGREEN_EX + password)
        # res = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        elif res == hash:
            print(Fore.LIGHTGREEN_EX + password+":"+ Fore.GREEN+hash)
    except KeyboardInterrupt :
        print(Fore.RED+"Erorr . Cancelled")


def file_crack(hashpath,wordpath, fun_type):
    try:
        banner(banner_t)
        with open(hashpath, "r", encoding='utf-8') as hash:
            for i in hash.readlines():
                with open(wordpath, "r") as password:
                    for pa in password.readlines():
                        t = Thread(target=fun_type, args=(pa.strip(), i.strip()))
                        t.start()
    except KeyboardInterrupt:
        print(Fore.RED+"Erorr . Cancelled")


def combo_crack(combo,wordpath, fun_type):
    try:
        banner(banner_t)
        with open(combo, "r", encoding='utf-8') as hash:
            for i in hash.readlines():
                with open(wordpath, "r" , encoding='utf-8') as password:
                    for pa in password.readlines():
                        t = Thread(target=fun_type, args=(pa.strip(), i.strip()))
                        t.start()
    except KeyboardInterrupt:
        print(Fore.RED + "Erorr . Cancelled")


def one_crack(hash, wordpath,fun_type):
    try:
        banner(banner_t)
        with open(wordpath, "r") as password:
            for pa in password.readlines():
                t = Thread(target=fun_type, args=(pa.strip(), hash))
                t.start()
    except KeyboardInterrupt:
        print(Fore.RED + "Erorr . Cancelled")
if __name__ == '__main__':
    if a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='md5'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, md5_crack)
    elif a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='sha1'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, sha1_crack)
    elif a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='sha224'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, sha224_crack)
    elif a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='sha384'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, sha384_crack)
    elif a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='sha256'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, sha256_crack)
    elif a_parse().HASH and a_parse().WORDLIST and (a_parse().TYPE=='sha512'):
        one_crack(a_parse().HASH, a_parse().WORDLIST, sha512_crack)
#==================================================================================
    elif a_parse().HASHLIST and a_parse().WORDLIST and (a_parse().TYPE=='md5'):
        file_crack(a_parse().HASHLIST, a_parse().WORDLIST, md5_crack)
    elif a_parse().HASHLIST and a_parse().WORDLIST and (a_parse().TYPE=='sha1'):
        file_crack(a_parse().HASHLIST, a_parse().WORDLIST, sha1_crack)
    elif a_parse().HASHLIST and a_parse().WORDLIST and (a_parse().TYPE=='sha256'):
        file_crack(a_parse().HASHLIST, a_parse().WORDLIST, sha256_crack)
    elif a_parse().HASHLIST and a_parse().WORDLIST and (a_parse().TYPE=='sha512'):
        file_crack(a_parse().HASHLIST, a_parse().WORDLIST, sha512_crack)
#==================================================================================
    elif a_parse().COMBO and a_parse().WORDLIST and a_parse().TYPE=='md5':
        combo_crack(a_parse().COMBO, a_parse().WORDLIST, md5_crack)
    elif a_parse().COMBO and a_parse().WORDLIST and (a_parse().TYPE=='sha1'):
        combo_crack(a_parse().COMBO, a_parse().WORDLIST, sha1_crack)
    elif a_parse().COMBO and a_parse().WORDLIST and (a_parse().TYPE=='sha256'):
        combo_crack(a_parse().COMBO, a_parse().WORDLIST, sha256_crack)
    elif a_parse().COMBO and a_parse().WORDLIST and (a_parse().TYPE=='sha512'):
        combo_crack(a_parse().COMBO, a_parse().WORDLIST, sha512_crack)
