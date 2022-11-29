# check two conditions at same time
# and . or
name = 'abc'
age = 19
if name == 'abc' and age==19:
    print("condition True")
else:
    print("condition False")

if name == 'abc' and age==23:
    print("condition True")
else:
    print("condition False")

if name == 'abcd' and age==19:
    print("condition True")
else:
    print("condition False")

if name == 'abc' or age==19:
    print("condition True")
else:
    print("condition False")

if name == 'abc' or age==23:
    print("condition True")
else:
    print("condition False")

if name == 'abcd' or age==23:
    print("condition True")
else:
    print("condition False")