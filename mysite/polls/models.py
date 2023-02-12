from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=30)
    party = models.CharField(max_length=20)
    votes = models.IntegerField(null=False, default=0)
    
    def __str__(self):
        return self.name + ' of the ' + self.party + ' party.' 
    
class Voter(models.Model):
    name = models.CharField(max_length=30)
    vote = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date = models.DateField('Date of vote')
    def __str__(self):
        return "I'm {} and i voted for {}.".format(self.name, self.vote.name)