import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, element):
        super().append(element)
        super().log(element)


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)

#Tue May 29 00:21:08 2018: msg1
#Tue May 29 00:21:08 2018: msg2
#['msg1', 'msg2']