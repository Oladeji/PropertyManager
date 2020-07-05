import smtplib
import schedule
import time
from datetime import datetime
from .models import Agent,SubProperty
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

class MailSender:

    def getpage(self, properties):
        sno = 1
        t = ""
        period = ""
        fro = ""
        daysleft = ""
        t = t + ("<html> <head> 	<title></title></head><body>")
        t = t + ("<table border=\"1\" cellpadding=\"1\" cellspacing=\"1\" style=\"width:1000px;\">")
        t = t + ("<thead>	<tr><th scope=\"col\">SNO</th><th scope=\"col\">PROPERTY</th>")
        t = t + ("<th scope=\"col\">AGENT</th><th scope=\"col\">PERIOD</th> <th scope=\"col\"> STATE</th> <th scope=\"col\">&nbsp;DAYS LEFT</th>")
        t = t + ("<th scope=\"col\">AMOUNT PAID</th>	<th scope=\"col\">OCCUPANT</th></tr>	</thead>	<tbody>")
        for item in properties:           
            if (item.SubPropertyState=="VACANT"):
                period = "----"
                daysleft = "----"
            else :
                period = str(item.EffectiveDate) + " to " +str( item.ExpiryDate)
                daysleft =  str(timezone.now() - item.ExpiryDate) 
                
            t = t + ("<tr>")
            t = t + ("<td>"+str(sno)+"</td>	<td>"+item.SubPropertyName+ "</td><td>" + item.SubPropertyName + "</td><td>" + period + "</td> <td>" + item.SubPropertyState + "</td><td>" + daysleft+ "</td>	<td>" + str(item.SubPropertyState) + "</td>		<td>" + item.SubPropertyDescription + "</td>")
            t = t + ("</tr>")
            ++sno
            
        t = t + ("</tbody></table></body></html>")
        return t

        
    def sendEmail(self ,sender_email, password, to, subject, msg):
        try:
            print ("Attempting to send mail")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            message = f'From: {sender_email}\nTo: {to}\nSubject: {subject}\n\n{msg}'
            print(message)
            server.sendmail(sender_email, to, message)
            server.quit()
            print("Email Sent")
        except:
            print("Some Error Occured while sending mail")


    def collateResult(self):
        #print("We are ok")
         subptylist= SubProperty.objects.all()
         for x in subptylist:
             print(x.SubPropertyName)
         msg= self.getpage(subptylist)
         self.sendEmail("ppirosamson@gmail.com","gbpeters@1","Akomspatrick@yahoo.com"," Report as at "+str(datetime.now()),msg)


    def PerformScheduling(self):
         schedule.every(1).seconds.do(self.collateResult )
         while True :
            schedule.run_pending()
            time.sleep(1)


    def start(self):
         scheduler = BackgroundScheduler()
         scheduler.add_job(self.collateResult , 'interval', minutes=1)
         scheduler.start()
"""
    if __name__ == '__main__':
    SENDER_EMAIL = "youremail@xyz.com"
    PASSWORD = "password"
    TO = "yourfrnds@email.com"
    SUBJECT = "Just having fun"
    MESSAGE = "hey dawg! it's my first Email"
    sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)
                    #       GeneralClass.sendmail("ppirosamson@gmail.com", "smtp.gmail.com", 587, "gbpeters@1", "Akomspatrick@yahoo.com", msg, "Testing Project Manager", "Renting-587", "AKOMOKLAFE OLADEJI-587");

"""