'''

regular expression
.  -> anything,letter,numbers,symbol but not newlines
+  -> one or more of
*  -> zero or more of
?  -> zero or one of


'''

import re

email = 'suraj@surajkarki.com'
expression = '[a-z\.@]+'

matches = re.findall(expression,email)
print(matches)

price = '$10.54'

expression = '\$([0-9].*\.[0-9]*)'

matches = re.findall(expression,email)
print(matches)

