# Hash-Cracker
A tool for cracking different hashes . The hashes that the tool supports are **(MD5 , Sha1 , Sha224 , Sha256 , Sha384 , Sha512)** .
The tool can retrieve a hash or a file hash or a combo list  and cracking all on the wordlist .
coded by [Gray Security Team](https://T.me/S3CURITY_GRAY)


### Crack a hash
![alt text](http://s7.picofile.com/file/8392331626/one.png "Crack a Hash ")


### Crack a hash file
![alt text](http://s6.picofile.com/file/8392331634/file.png "Crack HAsh File ")


### Crack a combo file
![alt text](http://s7.picofile.com/file/8392331642/com.png "Crack Combo file ")



## Installation & Runing
``` 
$ cd Hash-Cracker 
$ pip3 install -r requirements.txt
$ python3 hash-cracke.py -h 
$ python3 hash-cracke.py -H [hash] -w /root/Desktop/passlist.txt -t md5
$ python3 hash-cracke.py -f /root/Desktop/hashfile.txt -w /root/Desktop/passlist.txt -t md5
$ python3 hash-cracke.py -c /root/Desktop/combo.txt -w /root/Desktop/passlist.txt -t md5
``` 
## Guide 

Description of tool options

* -h Help 
* -H Hash Text
* -f Hash File
* -c Combo List 
* -w Wordlist Path 
* -t Hash Type {md5 , sha1 ,sha224 , sha256 , Sha384 , sha512}
