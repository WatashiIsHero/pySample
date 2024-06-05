from django.db import models

# Contentクラス
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Content(models.Model):
    id = models.IntegerField(primary_key=True)
    usr_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tw_date = models.CharField()
    tw_time = models.CharField()
    content = models.TextField()