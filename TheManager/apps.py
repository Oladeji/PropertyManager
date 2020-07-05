from django.apps import AppConfig
#from . import sayhello



class ThemanagerConfig(AppConfig):
    name = 'TheManager'

    def ready(self):
        from . import MailSender   
        x = MailSender.MailSender()
        #x.PerformScheduling()
        x.start()