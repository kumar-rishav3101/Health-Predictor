from django.db import models

# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.




MY_CHOICES2 = ((1, 'Headache'),
               (2, 'Sore Throat'),
               (3, 'Sneezing'),
               (4, 'Earache'),
               (5, 'Muscle Pain'),
               (6,'Fever'),
               (7,'Vomiting'),
               (8, 'Cough'),
               (9, 'Weight Loss'),
               (10, 'Dehydration'),
               (11, 'Stomachache'),
               (12, 'Sweat And Chill'),
               (13, 'Tiredness'),
               (14, 'Loss of Apetite'),
               (15, 'Greyish White Spot on Cheek'),
               (16, 'Constipation'),
               (17, 'Hairloss'),
               (18, 'Sore Tongue'),
               (19, 'Shortness in Breathe'),
               (20, 'Dysphagia'),
               (21, 'Red Spots'),
               (22, 'Wheezing'),
               (23, 'TightChest'),
               (24, 'Swolen Abdomen'),
               (25, 'Hydrophobia'),
               (26, 'Rashes'),
               (27, 'Rice Watery Stool'),
               (28, 'Dry Mouth'),
               (29, 'Rapid Heart Rate'),
               (30, 'Redness of Eye'),
               
               
               )
             
               


class MyModel(models.Model):      
    Symptoms = MultiSelectField(choices=MY_CHOICES2,blank=True)
    #  Days=models.IntegerField()
    Days= models.IntegerField(null=False ,blank=True)


class Files(models.Model):     
    display_picture = models.FileField()



class Remedy(models.Model):
    Diseasename=models.CharField(max_length=2225)
    Remedies=models.CharField(max_length=2225)    



