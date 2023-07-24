from django.db import models
from users.models import User
from django_jalali.db import models as jmodels


class BlogPost(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان", blank=False, null=False)
    content = models.TextField(verbose_name="متن", null=False, blank=False)
    slug =models.SlugField(primary_key=True, max_length=100,unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="post_author",
                                related_query_name="get_posts", verbose_name="پست")
    date=jmodels.jDateField(auto_now_add=True, verbose_name="تاریخ")
    date_modified=jmodels.jDateField(auto_now=True, verbose_name="تاریخ ویرایش")
    subject= models.ManyToManyField(to="Subject",related_name="post_subject")
   
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

class Subject(models.Model):
    title = models.CharField(max_length=50, verbose_name="موضوع", blank=False, null=False)
    