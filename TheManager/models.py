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
        return self.AgentName + self.Address +'Phone No'+ self.PhoneNo
   

class Property(models.Model):
    Agent_Property = models.ForeignKey(Agent,on_delete=models.DO_NOTHING)
    PropertyName = models.CharField(max_length=100)
    PropertyDescription = models.CharField(max_length=100)
    PropertyState = models.CharField(max_length=100)
    PropertyLocation = models.CharField(max_length=100)
    PropertyDescription= models.CharField(max_length=100)


    def __str__(self):
        return self.Property + self.PropertyName 

class SubProperty(models.Model):
    Property_SubProperty = models.ForeignKey(Property,on_delete=models.CASCADE)
    SubPropertyName = models.CharField(max_length=100)
    SubPropertyDescription = models.CharField(max_length=100)
    SubPropertyState = models.CharField(max_length=100)
    RentRate = models.DecimalField(max_digits=9, decimal_places=5)
    EffectiveDate = models.DateField('date Property was given out')
    ExpiryDate = models.CharField(max_length=100)
    PaymentState = models.CharField(max_length=100)


    def __str__(self):
        return self.SubPropertyName +' @ '+self.SubPropertyDescription

class RentTransactions(models.Model):
    SubProperty_RentTransactions = models.ForeignKey(SubProperty,on_delete=models.DO_NOTHING)
    StartingPeriod = models.DateField('date Property was given out')
    EndingPeriod =models.DateField('date Property was given out')
    AmountPaid = models.DecimalField(max_digits=9, decimal_places=5)
    AmountToBalance = models.DecimalField(max_digits=9, decimal_places=5)
    PresentOccupant = models.CharField(max_length=100)
    OccupantPhoneNo = models.CharField(max_length=100)
    OccupantRefDetails = models.CharField(max_length=100)
    Referee = models.CharField(max_length=100)    


    def __str__(self):
        return self.PresentOccupant +' , Remaining Period  '+ timezone.now() - self.EndingPeriod
