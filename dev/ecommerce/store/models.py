from django.db import models

# Create your models here.




class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)  # db_index'in amacı özel olması, bütün veritabanını değil sadece bunu hızlıca bulmasına yarar
    slug = models.SlugField(max_length=250, unique=True)    # unique=True olması benzersiz olması içindir


    class Meta:
        verbose_name_plural = 'categories'

                
    def __str__(self):
        return self.name
        
class product(models.Model):

        category=models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE,null=True)

        title= models.CharField(max_length=250)

        brand = models.CharField(max_length=250,default='un-branded')

        description =models.TextField(blank=True)                       # açıklama blank=true boş bırakılabilir.

        slug= models.SlugField(max_length=250)

        price = models.DecimalField(max_digits=4 , decimal_places=2)    # fiyatı belirlermizi sağlar yani fiyat için yazarız.
        
        image = models.ImageField(upload_to='product_images/')

        class Meta:
                verbose_name_plural = 'products'

                
        def __str__(self):
                return self.title