#==utf-8==
import os
import sys
import codecs
reload(sys)
sys.setdefaultencoding( "utf-8" )
import xml.dom.minidom
info = "D:\\Data\\XML\\20160910\\"
listfile = os.listdir(info)
filename = codecs.open(info+"alert.txt","w","UTF-8")
ss = u"Ԥ����Ϣ"
for line in listfile:
	if line[-4:] == ".xml":
		dom = xml.dom.minidom.parse(info+line[0:len(listfile)])
		alert = dom.documentElement
		sen  = alert.getElementsByTagName('sender')[0]
		sender = sen.childNodes[0].data
		filename.write(sender,)
		sendt = alert.getElementsByTagName('sendTime')[0]
		sendtime = sendt.childNodes[0].data
		filename.write(sendtime,)
		filename.write(ss)
		filename.write("\n")
		mess = alert.getElementsByTagName('description')[0]
		message = mess.childNodes[0].data
		for index in range(len(message)):
			print message[index]
            filename.write(message[index])
		filename.write("\n")
		filename.write("\n")