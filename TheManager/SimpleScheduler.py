import schedule
import time
from . import MailSender
class MySimpleScheduler:


      def __init__(self,y):
        self.y=y


      def getjob(self,p) :
         print ('I am singing seriously' ,p)
       


      def singing(self):
       
         schedule.every(2).seconds.do(self.getjob , self.y)
         while True :
           schedule.run_pending()
           time.sleep(1)
