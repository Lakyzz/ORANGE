from django.db import models
import uuid
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
        verbose_name="Categoría padre"
    )
    demanded = models.BooleanField(verbose_name='demanded state',null=True,blank=True)
    



    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    



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