#oefening 3
second = input("Quantity of seconds ")
d = (int((int(second)/86400)))
h = int(int((int(second)-((int(d)*86400))))/3600)
m = int(int((int(hr)-(3600*int(h))))/60)
s = int(int(mr)-(int(m)*60))
print("D:H:M:S -> {0}:{1}:{2}:{3}".format(d,h,m,s))