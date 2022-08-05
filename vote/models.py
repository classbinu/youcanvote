from django.db import models

class Vote(models.Model):
    objects = models.Manager() # pylint가 동적으로 추가된 objects를 인식하지 못해서 명시함.
    subject = models.CharField(max_length=255)
    yes = models.PositiveIntegerField(default=0)
    no = models.PositiveIntegerField(default=0)
    password = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.subject)
