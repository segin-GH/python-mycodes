import sayings as say
import sys


if len(sys.argv) == 2:
    say.hello(sys.argv[1])
    say.goodbye(sys.argv[1])
