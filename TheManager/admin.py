from django.contrib import admin

from .models import Agent,Property,SubProperty,RentTransactions

# class AgentAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,{'fields':['AgentName']}),

#       ('Contact Person',{'fields':['ContactPerson']}),
#     ]
    
admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(SubProperty)
admin.site.register(RentTransactions)

# AgentName = models.CharField(max_length=100)
#     Address = models.CharField(max_length=100)
#     ContactPerson = models.CharField(max_length=100)
#     Email = models.CharField(max_length=50)
#     PhoneNo = models.CharField(max_length=30)
