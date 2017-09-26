#oefening 2
days = input("Quantity of days ")
hours = input("Quantity of hours ")
minutes = input("Quantity of minutes ")
seconds = input("Quantity of seconds ")
seconds = (int(seconds)+(int(minutes)*60)+(int(hours)*3600)+(int(days)*86400))
print ("The total of seconds is {0}".format(seconds))