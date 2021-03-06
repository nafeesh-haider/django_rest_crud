from django.db import models
from django.conf import settings

# Create your models here.
class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Friend(models.Model):
	name = models.CharField(max_length = 100)

class Belonging(OwnedModel):
    name = models.CharField(max_length=100)

class Borrowed(models.Model):
	what = models.ForeignKey(Belonging, on_delete = models.CASCADE)
	to_what = models.ForeignKey(Friend, on_delete = models.CASCADE)
	when = models.DateTimeField(auto_now_add = True)


