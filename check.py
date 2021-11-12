import whichlang
from whichlang import which_lang
f= open('sample-test-files\\sample-assamese.txt','r')
data = f.read()

print which_lang(data)