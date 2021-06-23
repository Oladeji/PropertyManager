import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Agent(models.Model):
    AgentName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    ContactPerson = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    PhoneNo = models.CharField(max_length=30)
    

    def __str__(self):
        return 'AGENT NAME :>'+ self.AgentName +', ADDRESS :> ' +self.Address +', PHONE No:>  '+ self.PhoneNo
   

class Property(models.Model):
    Agent_Property = models.ForeignKey(Agent,on_delete=models.DO_NOTHING)
    PropertyName = models.CharField(max_length=100)
    PropertyDescription = models.CharField(max_length=100)
    PropertyState = models.CharField(max_length=20)
    PropertyLocation = models.CharField(max_length=100)


    def __str__(self):
        return 'PROPERTY NAME :> '+self.PropertyName +', DESCRIPTION :> ' +self.PropertyDescription +', @ :>' +self.PropertyLocation  +', PROPERTY STATE :> '+ self.PropertyState


class SubProperty(models.Model): 
    VACANT='VACANT'
    RENTED='RENTED'
    EXPIRED='EXPIRED'
    PART_PAYMENT='YET TO BALANCE UP'
    SUB_PROP_STATE_CHOICES=[
        (VACANT,'VACANT'),
        (RENTED,'RENTED'),
        (EXPIRED,'EXPIRED'),
        (PART_PAYMENT,'YET TO BALANCE UP'),
    ]
    Property_SubProperty = models.ForeignKey(Property,on_delete=models.CASCADE)
    SubPropertyName = models.CharField(max_length=100)
    SubPropertyDescription = models.CharField(max_length=100)
    SubPropertyState = models.CharField(max_length=100,choices=SUB_PROP_STATE_CHOICES, default=VACANT)
    RentRate = models.DecimalField('RENT AMOUNT',max_digits=15, decimal_places=2,default=0)
    AmountPaidSofar = models.DecimalField('TOTAL PAID SO FAR (Auto Fill)',max_digits=15, decimal_places=2,default=0)
    AmountToBalance = models.DecimalField('BALANCE (Auto Fill)',max_digits=15, decimal_places=2,default=0)
    EffectiveDate = models.DateField('WHEN THE PROPERTY WAS GIVEN OUT(Auto Fill)',default=timezone.now())
    ExpiryDate =models.DateField('RENT EXPIRY DATE(Auto Fill)',default=timezone.now())
    PaymentState = models.CharField('PAYMENT STATE (Auto Fill)',max_length=20 ,default='YET TO BALANCE UP')
    PresentOccupant = models.CharField('PRESENT OCCUPANT (Auto Fill)',max_length=100 ,default='NONE')
    PresentOccupantID = models.CharField(max_length=100,default='NONE')
    CurrentRunningPeriod = models.CharField(max_length=100,default='SAMPLE :FROM  JAN 1900 TO JAN JAN1900')


    def __str__(self):
        return 'SUB PROPERTY => : '+self.Property_SubProperty.PropertyName + ' ' +self.SubPropertyName +' @ '+self.SubPropertyDescription


    def getpropertyname(self):
        return self.Property_SubProperty.PropertyName  


    def getagentname(self):
        return self.Property_SubProperty.Agent_Property.AgentName  


   
class Tenant (models.Model):
    PRESENT='PR'
    DONEWITH='DW'
    TenantCHOICES=[
        (PRESENT,'Present'),
        (DONEWITH,'Done'),
    ]
    SubProperty_Tenant= models.ForeignKey(SubProperty,on_delete=models.DO_NOTHING)
    PresentOccupant = models.CharField('FULL NAME',max_length=100)
    OccupantPhoneNo = models.CharField('PHONE NO',max_length=100)
    Referee = models.CharField('REFEREE NAME',max_length=100)  
    OccupantRefDetails = models.CharField('REFEREE INFORMATION',max_length=100)
    TenantPhoto = models.ImageField('PASSPORT PHOTO',upload_to='TenantPhotos',blank = True)
    TenantState = models.CharField(max_length=100,choices=TenantCHOICES, default=PRESENT)
    CurrentRunningPeriod = models.CharField('PERIOD OF RENT',max_length=50)
    TotalRent = models.DecimalField('TOTAL AMOUNT FOR RENT (Auto Fill)',max_digits=15, decimal_places=2,default=0)
    
    CurrentRentRate = models.DecimalField('CURRENT RENT (Auto Fill)',max_digits=15, decimal_places=2,default=0)
    AmountPaidSofar = models.DecimalField('AMOUNT PAID SO FAR (Auto Fill)',max_digits=15, decimal_places=2, default=0)
    AmountToBalance = models.DecimalField('BALANCE (Auto Fill)',max_digits=15, decimal_places=2,default=0)
    FirstEngagementDate = models.DateField('DATE PROPERTY WAS FIRST GIVEN OUT',default=timezone.now())
    PaymentState = models.CharField('BALANCE (Auto Fill)',max_length=20 ,default='YET TO BALANCE UP')

    def __str__(self):
        return 'TENANT => : '+self.PresentOccupant+' ('+ self.OccupantPhoneNo+')  Occupying ' +   self.SubProperty_Tenant.Property_SubProperty.PropertyName + ' ' +self.SubProperty_Tenant.SubPropertyName +' @ '+self .SubProperty_Tenant.SubPropertyDescription

    def save(self, *args, **kwargs):
        rate = SubProperty.objects.get(pk=self.SubProperty_Tenant.pk)
        if rate :
            self.CurrentRentRate = rate.RentRate        
            super(Tenant, self).save(*args, **kwargs)
        else:
            super(Tenant, self).save(*args, **kwargs)
    

class PeriodicRentTransactions(models.Model):
    Tenant_RentTransactions = models.ForeignKey(Tenant,on_delete=models.DO_NOTHING)
    StartingPeriod = models.DateField('Date Property was given out')
    EndingPeriod =models.DateField('Expiry Date of Rent')
    CurrentRunningPeriod = models.CharField('PERIOD OF RENT',max_length=50)
    RentRate = models.DecimalField('RENT RATE (Auto Fill)',default=0, max_digits=15, decimal_places=2)
    AmountPaidSofar = models.DecimalField('AMOUNT PAID SO FAR (Auto Fill)',default=0,max_digits=15, decimal_places=2)
    AmountToBalance = models.DecimalField('REMAINING BALANCE (Auto Fill)',default=0,max_digits=15, decimal_places=2)


    def __str__(self):
        return 'PERIODIC => : '+self.CurrentRunningPeriod+' '+ self.Tenant_RentTransactions.SubProperty_Tenant.SubPropertyName +'  ('+ self.Tenant_RentTransactions.SubProperty_Tenant.Property_SubProperty.PropertyName+' :' +self.Tenant_RentTransactions.SubProperty_Tenant.SubPropertyDescription  +  ')  Occupied by '+self.Tenant_RentTransactions.PresentOccupant + ' ' +' , Remaining Period  '+    str( self.EndingPeriod-timezone.localdate() )
        #return  self.SubProperty_RentTransactions.Property_SubProperty.PropertyName + ' '  + self.SubProperty_RentTransactions.SubPropertyName + ' '+self.SubProperty_RentTransactions.SubPropertyDescription +' Ocupied by '+ self.PresentOccupant +' , Remaining Period  '+    str( self.EndingPeriod-timezone.now() )
    
    def save(self, *args, **kwargs):
        rate = Tenant.objects.get(pk=self.Tenant_RentTransactions.pk)
        if rate :
            self.RentRate = rate.CurrentRentRate
            #self.AmountToBalance =   self.RentRate - self.AmountPaidSofar     
            #super(PeriodicRentTransactions, self).save(*args, **kwargs)
        #else:
            #self.AmountToBalance =   self.RentRate - self.AmountPaidSofar     
        super(PeriodicRentTransactions, self).save(*args, **kwargs)


class DetailTransactions(models.Model):
    PeriodicRentTransactions_DetailTransactions = models.ForeignKey(PeriodicRentTransactions,on_delete=models.DO_NOTHING)
    AmountPaid = models.DecimalField('How much do you want to pay ? ',max_digits=15, decimal_places=2)
    DateOfPayment =models.DateField('Payment Date',default=timezone.now())


    def __str__(self):
        return 'PAYMENT => '+self.PeriodicRentTransactions_DetailTransactions.Tenant_RentTransactions.PresentOccupant +' PERIOD: '+self.PeriodicRentTransactions_DetailTransactions.CurrentRunningPeriod+ 'PAID: '+ str(self.AmountPaid) +' On '+ str(self.DateOfPayment)+ 'For '+ self.PeriodicRentTransactions_DetailTransactions.Tenant_RentTransactions.SubProperty_Tenant.SubPropertyName +', '+ self.PeriodicRentTransactions_DetailTransactions.Tenant_RentTransactions.SubProperty_Tenant.Property_SubProperty.PropertyName
        

def gettotalmoneypaidbytenant(tenant):
        All_RentTransactions =tenant.periodicrenttransactions_set.all()
        totalsumpaid=0
        totalrentrate=0
        for a_periodictrans in All_RentTransactions:
            totalrentrate +=   a_periodictrans.RentRate
          # A_PeriodicRentTransactions = PeriodicRentTransactions.objects.get(pk=aperiodictrans.pk)     
      
            print(a_periodictrans)
            details=a_periodictrans.detailtransactions_set.all()
        
            for dt in details:
                totalsumpaid += dt.AmountPaid
                print('value',dt.AmountPaid)
        print(totalsumpaid,totalrentrate)
        return totalsumpaid,totalrentrate

@receiver(post_save, sender=DetailTransactions)
def Update_PeriodicRentTransactions(sender, instance, **kwargs):
        print(instance)
        PaymentState='PAID FULL'
        A_PeriodicRentTransactions = PeriodicRentTransactions.objects.get(pk=instance.PeriodicRentTransactions_DetailTransactions.pk)     
        print(A_PeriodicRentTransactions)
        details=A_PeriodicRentTransactions.detailtransactions_set.all()
        sumpaid=0
        for dt in details:
            sumpaid += dt.AmountPaid
            print('value',dt.AmountPaid)
        print(sumpaid)
        A_PeriodicRentTransactions.AmountPaidSofar = sumpaid
        A_PeriodicRentTransactions.AmountToBalance = A_PeriodicRentTransactions.RentRate-sumpaid
        A_PeriodicRentTransactions.save()

        if A_PeriodicRentTransactions.AmountToBalance > 0 :
            PaymentState='YET TO BALANCE UP'
            print(PaymentState) #

         # get the tenant , update AmountPaidSofar AmountToBalance PaymentState

        A_Tenant = Tenant.objects.get(pk=A_PeriodicRentTransactions.Tenant_RentTransactions.pk)     
        print(A_Tenant)
  
        # get the SubProperty , update AmountPaidSofar AmountToBalance PaymentState

        A_SubProperty = SubProperty.objects.get(pk=A_Tenant.SubProperty_Tenant.pk)     
        print(A_SubProperty)
        A_SubProperty.AmountPaidSofar=sumpaid
        A_SubProperty.AmountToBalance=A_PeriodicRentTransactions.AmountToBalance
        A_SubProperty.PaymentState=PaymentState
        A_SubProperty.PresentOccupant = A_Tenant.PresentOccupant
        A_SubProperty.EffectiveDate=A_PeriodicRentTransactions.StartingPeriod
        A_SubProperty.ExpiryDate = A_PeriodicRentTransactions.EndingPeriod
        if PaymentState =='YET TO BALANCE UP':
            A_SubProperty.SubPropertyState = PaymentState
        else:
           A_SubProperty.SubPropertyState = 'RENTED'
        A_SubProperty.save()
  
        # new additions to update payments made so far to be all payment realy made so far 
        # not just periodic but all payments for the tenant
        totalsumpaid, totalrent= gettotalmoneypaidbytenant(A_Tenant)
        A_Tenant.AmountPaidSofar=totalsumpaid
        A_Tenant.TotalRent=totalrent
        A_Tenant.AmountToBalance=    totalrent-totalsumpaid# #A_PeriodicRentTransactions.AmountToBalance
        if totalrent-totalsumpaid > 0 :
                  A_Tenant.PaymentState='YET TO BALANCE UP'
        else :
       
                 A_Tenant.PaymentState='PAID FULL'
        A_Tenant.save()
        # All_RentTransactions =A_Tenant.periodicrenttransactions_set.all()
        # totalsumpaid=0
        # for a_periodictrans in All_RentTransactions:

        #   # A_PeriodicRentTransactions = PeriodicRentTransactions.objects.get(pk=aperiodictrans.pk)     
      
        #     print(a_periodictrans)
        #     details=a_periodictrans.detailtransactions_set.all()
        
        #     for dt in details:
        #         totalsumpaid += dt.AmountPaid
        #         print('value',dt.AmountPaid)
        # print(totalsumpaid)

        #A_PeriodicRentTransactions.save()
        #post_save.connect(Update_PeriodicRentTransactions, sender=DetailTransactions)
      
        #return  self.SubProperty_RentTransactions.Property_SubProperty.PropertyName + ' '  + self.SubProperty_RentTransactions.SubPropertyName + ' '+self.SubProperty_RentTransactions.SubPropertyDescription +' Ocupied by '+ self.PresentOccupant +' , Remaining Period  '+    str( self.EndingPeriod-timezone.now() )
    

# ...
# class RentTransactions(models.Model):
#     Tenant_RentTransactions = models.ForeignKey(Tenant,on_delete=models.DO_NOTHING)
#     StartingPeriod = models.DateField('Date Property was given out')
#     EndingPeriod =models.DateField('Expiry Date of Rent')
#     AmountPaid = models.DecimalField(max_digits=15, decimal_places=2)
   
#     PresentOccupant = models.CharField(max_length=100)
#     OccupantPhoneNo = models.CharField(max_length=100)
#     OccupantRefDetails = models.CharField(max_length=100)
#     Referee = models.CharField(max_length=100)    


#     def __str__(self):
#         #return self.PresentOccupant +' , Remaining Period  '+    str( self.EndingPeriod-timezone.now() )
#         return  self.SubProperty_RentTransactions.Property_SubProperty.PropertyName + ' '  + self.SubProperty_RentTransactions.SubPropertyName + ' '+self.SubProperty_RentTransactions.SubPropertyDescription +' Ocupied by '+ self.PresentOccupant +' , Remaining Period  '+    str( self.EndingPeriod-timezone.now() )
    
    
#     def getsubpropertyname(self):
#         return self.SubProperty_RentTransactions.SubPropertyName + ' '+self.SubProperty_RentTransactions.SubPropertyDescription 
# ...


