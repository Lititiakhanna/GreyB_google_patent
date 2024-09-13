from django.db import models

class GooglePatentData(models.Model):
    # CATEGORY_CHOICES = [('one','one'), ('two', 'two')]
    
    id = models.CharField(primary_key=True, max_length=100, null=False)
    title = models.TextField(null=False)
    assignee = models.TextField(null=False)
    inventor = models.TextField(null=False)
    priority_date = models.DateField(auto_now=True)
    creation_date = models.DateField(auto_now=True)
    publication_date = models.DateField(auto_now=True) 
    grant_date = models.DateField(auto_now=True)
    result_link = models.TextField(null=False)
    representative_figure_link = models.TextField(null=False)
    number_of_authors = models.CharField(max_length=100, null=False)
    number_of_viewers = models.IntegerField(auto_now=True)

    class Meta:
        db_table = 'google_patent_data' 

class CategoricalFrequencyCount(models.Model):
    category = models.CharField(primary_key=True)
    count = models.IntegerField()

    class Meta:
        db_table = 'categorical_frequency_count' 


class NumericalStatistics(models.Model):
    index = models.CharField(primary_key=True)
    number_of_viewers = models.IntegerField()

    class Meta:
        db_table = 'numerical_statistics' 



