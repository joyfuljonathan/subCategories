from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductData(models.Model):
    product_model = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    general_name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, default =1, on_delete=models.CASCADE) 
    country_of_origin = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    imgURL1 = models.CharField(max_length=255, null = True)
    imgURL2 = models.CharField(max_length=255, null = True)
    imgURL3 = models.CharField(max_length=255, null = True)
    weight = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    size_one = models.IntegerField();
    price = models.IntegerField();
    shipping = models.IntegerField();
    stock = models.IntegerField();
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')