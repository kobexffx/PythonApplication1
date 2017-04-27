class Fileoperator:
    def  openfile(self,filepath):
        dom = xml.dom.minidom.parse(filepath)
        root = dom.documentElement
        aa = dom.getElementsByTagName('durTick')
        for a in aa:
            print a.firstChild.data
#=================================================
root_name              = []
identifier_name        = []
sender_name            = []
senderCode_name        = []
senderName_name        = []
sendTime_name          = []
status_name            = []
msgType_name           = []
scope_name             = []
methodName_name        = []
message_name           = []
audenceprt_name        = []
language_name          = []
eventType_name         = [] 
urgency_name           = []
severity_name          = []
certainty_name         = []
effective_name         = []
headline_name          = []
descriptin_name        = []
areaDesc_name          = []
geocode_name           = []
secClassification_name = []
#===================================================
