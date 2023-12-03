from django.db import models
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField ()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # for show image on admin pannel
    def img_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" / >'.format(self.img))

    # this function call when obkect is print we overwrite the function
    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post/')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
