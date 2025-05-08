# import datetime

# now = datetime.datetime.now()

# StartOfYear = datetime.datetime(now.year, 1, 1)
# Delta = now - StartOfYear
# SSJanuary = int(Delta.total_seconds()) 
# # print(f"Seconds since", x.strftime("%B"))
# print("Seconds since January 1,", now.year)
# print(SSJanuary)
# # print("Seconds since January 1,", x.strftime("%Y"))


from datetime import datetime

now = datetime.now()

StartOfYear = datetime(now.year, 1, 1)
Delta = now - StartOfYear
SSJanuary = int(Delta.total_seconds())
# print("Seconds since", now.strftime("%B"))
# print("Seconds since January 1,", now.year)
# print("Seconds since January 1,", now.day)
print("Seconds since January 1, %d: %d or %e in scientific notation" % (now.year, SSJanuary, SSJanuary))
print("%s %d %d" % (now.strftime("%b"), now.day, now.year))
