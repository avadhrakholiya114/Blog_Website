from django.db import models

# Create your models here.

class Categpry(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    url=models.CharField(max_length=100)
    img=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)


class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    url=models.CharField(max_length=100)
    img=models.ImageField(upload_to='post/')
    caatagory=models.ForeignKey(Categpry,on_delete=models.CASCADE)

