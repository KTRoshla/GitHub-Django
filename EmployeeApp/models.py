from django.db import models

# Create your models here.
class MasterCategory(models.Model):
    CatID = models.AutoField(primary_key=True)
    CatName = models.CharField(max_length=100)
    Status = models.CharField(max_length=1,null=True,blank=True)
    Parent = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=250,null=True,blank=True)

class MasterCategoryValues(models.Model):
    CatValID = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=1200,null=True,blank=True)
    Status = models.CharField(max_length=1,null=True,blank=True)
    SortOrder = models.IntegerField(null=True,blank=True)
    CatID = models.IntegerField()
    Description = models.CharField(max_length=600,null=True,blank=True)
    ParentID = models.IntegerField(null=True,blank=True)