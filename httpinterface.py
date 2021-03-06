from bottle import *
from PowerTailInterface import *
from os import getcwd


class HTTPInterface:
    def __init__(self):
        self.pt = PowerTailInterface();

    #@route('/ui')
    def mainui(self):
        return self.send_static('main.html')
        #'<b>Hello, this is where the UI should be </b>!'
    

    #@route('/io/:letter')
    def io_get(self,letter=''):
        if("c"==letter):
            self.pt.setPower(False)
            time.sleep(1)
            self.pt.setPower(True)
        elif ("o"==letter):
            self.pt.setPower(False)
        elif ("i"==letter):
            self.pt.setPower(True)
        else:
            p = self.pt.isready()
            self.pt.setPower(not p)

            
    #@route('/static/<filename:path>')
    def send_static(self,filename):
        newroot = getcwd().replace("\\","\\\\")+"/"+ "static"
        return static_file(filename, root=newroot)
        
if __name__ == '__main__':
    ipport = 80
    ipaddr='0.0.0.0' #'192.168.56.1' #'localhost'
    app = Bottle()
    httpi = HTTPInterface()
    app.route('/')(httpi.mainui)
    app.route('/ui')(httpi.mainui)
    app.route('/io/:letter')(httpi.io_get)
    app.route('/static/<filename:path>')(httpi.send_static)
    
    run(app,host=ipaddr, port=ipport)
