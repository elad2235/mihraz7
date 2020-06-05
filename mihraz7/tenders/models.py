from django.db import models


class Tender(models.Model):
    tender_name = models.CharField(max_length=50)
    tender_id = models.CharField(max_length=50, unique=True)
    winner = models.CharField(max_length=50, blank=True)
    files = models.CharField(max_length=100, blank=True)
    online_payment = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    update_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    Count_of_applied = models.IntegerField(blank=True)

    def __str__(self):
        return self.tender_name


class Comment(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    tender_id = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.comment_name + self.comment_content
