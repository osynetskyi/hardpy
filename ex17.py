from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = open(from_file).read()

#print "The input file is %s bytes long" % len(indata)

#print "Does the output file exists? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

# out_file = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())

# print "Alright, all done."

# out_file.close()
# in_file.close()