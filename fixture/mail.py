
import poplib
import email
import time



class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            #opredelenie kolich pisem
            num = pop.stat()[0]
            #esli pisem >0
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]
                    #skleivaem stroki
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    #analiz text pisma
                    msg = email.message_from_string(msgtext)
                    #esli tema pisma=zadan., to ego dernut
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()
            pop.quit()
            time.sleep(6)
        return None

