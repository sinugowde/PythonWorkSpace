# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

# lst = [1, 2, "a", "b"]
# print(lst)
# a,b,c=lst
# print("a:%d, b=%d, c=%s" % (a, b, c))


imelda = "more mayhem", "Imwdla May", 2011, ((1, "Pulling the Rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
title, artist, year, track = imelda
print(title)
print(artist)
print(year)
for item in track:
    print(item)
