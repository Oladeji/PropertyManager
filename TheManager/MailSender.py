import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        t = t + ("<th scope=\"col\">RENT</th><th scope=\"col\">AMOUNT PAID</th><th scope=\"col\">BALANCE</th>	<th scope=\"col\">OCCUPANT</th></tr>	</thead>	<tbody>")
        for item in properties:           
            if (item.SubPropertyState=="VACANT"):
                period = "----"
                daysleft = "----"
            else :
                period = str(item.EffectiveDate) + " to " +str( item.ExpiryDate)
                daysleft =  str(timezone.localdate() - item.ExpiryDate) 
                
            t = t + ("<tr>")
            t = t + ("<td>"+str(sno)+"</td>	<td>"+item.getpropertyname()+' - '+item.SubPropertyName+ "</td><td>" + item.getagentname() + "</td><td>" + period + "</td> <td>" + item.SubPropertyState + "</td><td>" + daysleft+ "</td>	<td>" + str(item.RentRate) + "</td>	<td>" + str(item.AmountPaidSofar) + "</td>	<td>" + str(item.AmountToBalance) + "</td>		<td>" + item.PresentOccupant + "</td>")
            t = t + ("</tr>")
            sno=sno+1
            
        t = t + ("</tbody></table></body></html>")
        print('AGENT ',item.getagentname() +'  '+item.getpropertyname()+' - '+item.SubPropertyName)
        return t

        
    def sendEmailOld(self ,sender_email, password, to, subject, msg):
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


    def sendEmail(self ,sender_email, password, to, subject, msg):
        try:
            print ("Attempting to send mail")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)

            message = MIMEMultipart("alternative")
            message["Subject"] = "multipart test"
            message["From"] = sender_email
            message["To"] = to
            text = """\
            Hi,
            How are you?
            Real Python has many great tutorials:
            www.realpython.com"""



            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(msg, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            print(message)
            server.sendmail(sender_email, to, message.as_string())
            server.quit()
            print("Email Sent Finally ")
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
         schedule.every(15).minutes.do(self.collateResult )
         while True :
            schedule.run_pending()
            time.sleep(1)


    def start(self):
         scheduler = BackgroundScheduler()
         scheduler.add_job(self.collateResult , 'interval', minutes=15)
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