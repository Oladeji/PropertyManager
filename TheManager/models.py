import datetime
from django.db import models
from django.utils import timezone

class Agent(models.Model):
    AgentName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    ContactPerson = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    PhoneNo = models.CharField(max_length=30)


    def __str__(self):
        return 'Name =>'+ self.AgentName +' Address :=> ' +self.Address +' Phone No: '+ self.PhoneNo
   

class Property(models.Model):
    Agent_Property = models.ForeignKey(Agent,on_delete=models.DO_NOTHING)
    PropertyName = models.CharField(max_length=100)
    PropertyDescription = models.CharField(max_length=100)
    PropertyState = models.CharField(max_length=20)
    PropertyLocation = models.CharField(max_length=100)
   # PropertyDescription= models.CharField(max_length=100)


    def __str__(self):
        return self.PropertyName + self.PropertyDescription 

class SubProperty(models.Model):
    VACANT='VC'
    RENTED='RT'
    EXPIRED='EX'
    SUB_PROP_STATE_CHOICES=[
        (VACANT,'Vacant'),
        (RENTED,'Rented'),
        (EXPIRED,'Expired')
    ]
    Property_SubProperty = models.ForeignKey(Property,on_delete=models.CASCADE)
    SubPropertyName = models.CharField(max_length=100)
    SubPropertyDescription = models.CharField(max_length=100)
    SubPropertyState = models.CharField(max_length=100,choices=SUB_PROP_STATE_CHOICES, default=VACANT)
    # SubPropertyState = models.CharField(max_length=100)
    RentRate = models.DecimalField(max_digits=15, decimal_places=2)
    EffectiveDate = models.DateTimeField('date Property was given out')
    ExpiryDate =models.DateTimeField('Rent Expiry Date')
    PaymentState = models.CharField(max_length=20)
    #PresentOccupant = models.CharField(max_length=100)

    def __str__(self):
        return self.SubPropertyName +' @ '+self.SubPropertyDescription

class RentTransactions(models.Model):
    SubProperty_RentTransactions = models.ForeignKey(SubProperty,on_delete=models.DO_NOTHING)
    StartingPeriod = models.DateTimeField('Date Property was given out')
    EndingPeriod =models.DateTimeField('Expiry Date of Rent')
    AmountPaid = models.DecimalField(max_digits=15, decimal_places=2)
    AmountToBalance = models.DecimalField(max_digits=15, decimal_places=2)
    PresentOccupant = models.CharField(max_length=100)
    OccupantPhoneNo = models.CharField(max_length=100)
    OccupantRefDetails = models.CharField(max_length=100)
    Referee = models.CharField(max_length=100)    


    def __str__(self):
        return self.PresentOccupant +' , Remaining Period  '+ str(timezone.now() - self.EndingPeriod)
