import re
data = "title=Hello&body=Hello World&key=hi&value=Bye guys&test=check literal&result=every thing is fine"
res = re.findall(r'([\w\s]+=[\w\s]+)', data)
print("res: {}\n".format(res))

if res:
    print("got it")
else:
    print("not there")
