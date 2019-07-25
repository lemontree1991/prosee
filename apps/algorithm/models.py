from django.db import models


class Algorithm(models.Model):
    id = models.CharField(unique=True, max_length=255, primary_key=True, db_column="alg_id")
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    class_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'algorithm'

    def __str__(self):
        return self.name
