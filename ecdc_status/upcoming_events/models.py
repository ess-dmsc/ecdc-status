from django.db import models
from django.utils import timezone

class EventIcon(models.Model):
    Name = models.CharField(max_length = 50)
    Image = models.FileField(upload_to = "icon_images/")
    
    def __str__(self):
        return self.Name

def convertHours(Hours):
    ReturnUnit = "hour"
    ReturnValue = Hours
    if (Hours > 24.0 * 60):
        ReturnValue = Hours / (24 * 30)
        ReturnUnit = "month"
    elif (Hours > 24.0 * 14):
        ReturnValue = Hours / (24 * 7)
        ReturnUnit = "week"
    elif (Hours > 24.0):
        ReturnValue = Hours / 24
        ReturnUnit = "day"
    ReturnValue = round(ReturnValue)
    if (ReturnValue != 1):
        ReturnUnit += "s"
    return (ReturnValue, ReturnUnit)
        
def todayMorning():
    return timezone.now().replace(hour=9,minute=0,second=0)
    
def todayAfternoon():
    return timezone.now().replace(hour=17,minute=0,second=0)

class Event(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null = True)
    StartDate = models.DateTimeField('Start of event', default = todayMorning)
    EndDate = models.DateTimeField('End of event', default = todayAfternoon, null = True)
    Icon = models.ForeignKey(EventIcon, on_delete=models.CASCADE, blank=True, null = True)
    
    def __str__(self):
        return self.Title
        
    def isOngoing(self):
        if (self.EndDate == None):
            return False
        return timezone.now() > self.StartDate and timezone.now() < self.EndDate
    
    def timeUntilStart(self):
        return convertHours((self.StartDate - timezone.now()).total_seconds() / 3600)[0]
    
    def timeUntilEnd(self):
        return convertHours((self.EndDate - timezone.now()).total_seconds() / 3600)[0]
    
    def timeUntilEndUnit(self):
        return convertHours((self.EndDate - timezone.now()).total_seconds() / 3600)[1]
        
    def timeUntilStartUnit(self):
        return convertHours((self.StartDate - timezone.now()).total_seconds() / 3600)[1]
    