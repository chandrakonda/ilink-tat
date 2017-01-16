# import csv
#
# with open('.\\Results\\names.csv', 'wb') as csvfile:
#     fieldnames = ['firstcolvalue', 'currentkey', 'values', 'status']
#     __pass = [{'firstcolvalue': 'Baked', 'currentkey': 'Beans','values':"pass",'status':"test"},{'firstcolvalue': 'Baked', 'currentkey': 'Beans', 'values': "pass", 'status': "test"}]
#     writer = csv.DictWriter(csvfile,delimiter=',',fieldnames=fieldnames)
#
#     #writer.writerow(dict((fn, fn) for fn in fieldnames))
#     writer.writeheader()
#     # writer.writeheader()
#     x=0
#     #values = zip(*[d.values() for d in __pass])
#     for x in range(0,len(__pass)):
#         writer.writerow(__pass[x])
#     # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

__pass = [{'firstcolvalue': 'Baked', 'currentkey': 'Beans','values':"fail",'status':"pass"},{'firstcolvalue': 'Baked', 'currentkey': 'Beans', 'values': "pass", 'status': "fail"}]
status = [d["firstcolvalue"] for d in __pass if d["status"] == "fail"]
print(status)
print(type(status))
if len(status) >= 1:
    print("hi")