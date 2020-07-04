from django.contrib import admin
from .models import Agent,Property,SubProperty,RentTransactions



class SubPropertyInline(admin.TabularInline):
     model = SubProperty
     extra=3


class PropertyAdmin(admin.ModelAdmin):
    #   fieldsets = [(None,{'fields':['PropertyName']}),
    #   ('Property Description ',{'fields':['PropertyDescription'],'classes':['collapse']}),     ]
      inlines= [SubPropertyInline]



admin.site.register(Agent)
admin.site.register(Property,PropertyAdmin)
#admin.site.register(SubProperty)
admin.site.register(RentTransactions)


""" 



class PropertyInline(admin.TabularInline):
     model = Property
     extra=3


class AgentAdmin(admin.ModelAdmin):
      fieldsets = [(None,{'fields':['AgentName']}),
      ('Contact Person',{'fields':['ContactPerson'],'classes':['collapse']}),     ]
      inlines= [PropertyInline]
    
admin.site.register(Agent,AgentAdmin)
 #admin.site.register(Property)
admin.site.register(SubProperty)
admin.site.register(RentTransactions)



"""
