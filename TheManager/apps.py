from django.apps import AppConfig
from . import sayhello
from . import SimpleScheduler
class ThemanagerConfig(AppConfig):
    name = 'TheManager'


x = SimpleScheduler.MySimpleScheduler("Halleluyah")
x.singing()