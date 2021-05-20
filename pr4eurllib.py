import urllib.request, urllib.parse, urllib.error

import ssl

urlHand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

urlWHand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

urlOfSSL = input('Enter -')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlIfSSL = urllib.request.urlopen(urlOfSSL, context=ctx).read()

counts = dict()

for line in urlHand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

for line in urlWHand:
    print(line.decode().strip())

    
    
