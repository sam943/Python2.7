# Regular Expressions
# Regulat Expression Cheat Sheet
# https://www.debuggex.com/cheatsheet/regex/python
import re #module for regular expression

line = '56.30.65.218.broad.xy.jx.dynamic.163data.com.cn [218.65.30.156] failed - POSSIBLE BREAK-IN ATTEMPT!'

# Simple matching
match_board = re.search('broad',line)
match_hello = re.search('hello',line)
#print match_board 
#print match_hello

#Regular Expression
match = re.match("^(56.*?)\s\[.*?\sfailed\s-\sPOSSIBLE.*?\sBREAK-IN.*?!$",line)
print match
"""
^ = starting with
.* = everything
.*?\s = complete string until space
$ = Ending with
"""
# Printing the match groups
print match.groups()
