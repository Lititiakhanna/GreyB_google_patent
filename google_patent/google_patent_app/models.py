from django.db import models

class GooglePatentData(models.Model):
    # CATEGORY_CHOICES = [('one','one'), ('two', 'two')]
    
    id = models.CharField(primary_key=True)
    title = models.TextField()
    assignee = models.TextField()
    inventor = models.TextField()
    priority_date = models.DateField()
    creation_date = models.DateField()
    publication_date = models.DateField() 
    grant_date = models.DateField()
    result_link = models.TextField()
    representative_figure_link = models.TextField()
    number_of_authors = models.CharField()
    number_of_viewers = models.IntegerField()

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



