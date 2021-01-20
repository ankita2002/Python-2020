import datetime
def time():
    var = datetime.datetime.now()
    return var.strftime("%d-%m-%Y %H:%M:%S")
print(time())