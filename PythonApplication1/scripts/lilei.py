class human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()
    def __init__(self,input_gender):
        self.gender = input_gender
    def printgender(self):
        print self.gender
        

            
lilei = human('male')
lilei.laugh_100th()
print lilei.gender
lilei.printgender()
