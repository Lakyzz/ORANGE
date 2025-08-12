from django.db import models
import uuid
from django.utils.text import slugify
# Create your models here.

    
class Category(models.Model):
    id_category = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,verbose_name='ID')
    category_name = models.CharField(max_length=45,verbose_name='Category',null=False,blank=False)
    category_description = models.CharField(max_length=255,verbose_name='Description',null=False,blank=False)
    image_category = models.ImageField(upload_to='categories/',verbose_name='imagen de categorias',null=True,blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="parent"
    )
    demanded = models.BooleanField(verbose_name='demanded state',null=True,blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)



    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)



class Specifications(models.Model):
    id_specification = models.UUIDField(primary_key=True,max_length=255,verbose_name='ID')
    specification_name = models.CharField(max_length=45,verbose_name='name',null=False,blank=False)


class Product(models.Model):
    code = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,max_length=255,verbose_name='id')
    name = models.CharField(max_length=45,verbose_name='Nombre',null=False,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Precio',null=False,blank=False)
    description = models.TextField(verbose_name='Descripción',null=False,blank=False)
    image_product = models.ImageField(upload_to='tecnology/',verbose_name='Imagen de productos',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.name
    

class Poster(models.Model):
    code = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True, verbose_name='id')
    poster_name = models.CharField(max_length=255,null=False,blank=False)
    poster_image = models.ImageField(upload_to='posters/',null=False,blank=False)
    ACTIVE_INACTIVE = [
        (True,'Active'),
        (False,'Inactive'),
    ]
    state = models.BooleanField(choices=ACTIVE_INACTIVE,default=True,verbose_name='State')

    def __str__(self):
        return self.poster_name