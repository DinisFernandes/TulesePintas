from django.db import models
from django.utils import timezone
from PIL import Image, ExifTags
from django.conf import settings
from django.core.validators import MinValueValidator
import os

# Create your models here.

class Categorias(models.TextChoices):
    menino = 'Menino', 'Menino'
    menina = 'Menina', 'Menina'
    ambos = 'Ambos', 'Ambos'


class Tamanhos(models.TextChoices):
    china = 'China', 'China'
    polonia = 'polonia', 'Polonia'
    outros = 'Outros', 'Outros'


class Post(models.Model):
    referencia = models.CharField(max_length=100, verbose_name='Referencia')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    categories = models.CharField(max_length=6, blank=True, null=True,
                                 choices= Categorias.choices,
                                 default= Categorias.menino,)
    tamanho = models.CharField(max_length=10,
                                 choices= Tamanhos.choices,
                                 default= Tamanhos.polonia,)
    content = models.TextField(verbose_name='Descricao')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', verbose_name='Imagem De Perfil')
    price = models.DecimalField(max_digits=6,  decimal_places=2, blank=True, null=True, verbose_name='Preco')
    promocao = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Promocao')

    vendido_3_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_6_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_9_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_12_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_18_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_2_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_12_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_13_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')
    vendido_14_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True,verbose_name='nrº vendido')

    stock_3_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 3 meses 62 cm')
    stock_6_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 6 meses 68 cm')
    stock_9_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 9 meses 74 cm')
    stock_12_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 12 meses 80 cm')
    stock_18_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 18 meses 86 cm')
    stock_2_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 2 anos 92 cm')
    stock_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 3 anos 98 cm')
    stock_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 4 anos 104 cm')
    stock_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 5 anos 110 cm')
    stock_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 6 anos 116 cm')
    stock_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 7 anos 122 cm')
    stock_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 8 anos 128 cm')
    stock_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 9 anos 134 cm')
    stock_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 10 anos 140 cm')
    stock_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 11 anos 146 cm')
    stock_12_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 12 anos 152 cm')
    stock_13_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 13 anos 158 cm')
    stock_14_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Stock 14 anos 164 cm')

    vendas_3_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Vendas 3 meses 62 cm')
    vendas_6_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Vendas 6 meses 68 cm')
    vendas_9_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='Vendas 9 meses 74 cm')
    vendas_12_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 12 meses 80 cm')
    vendas_18_meses = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 18 meses 86 cm')
    vendas_2_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 2 anos 92 cm')
    vendas_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 3 anos 98 cm')
    vendas_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 4 anos 104 cm')
    vendas_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 5 anos 110 cm')
    vendas_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 6 anos 116 cm')
    vendas_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 7 anos 122 cm')
    vendas_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 8 anos 128 cm')
    vendas_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 9 anos 134 cm')
    vendas_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 10 anos 140 cm')
    vendas_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 11 anos 146 cm')
    vendas_12_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 12 anos 152 cm')
    vendas_13_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 13 anos 158 cm')
    vendas_14_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 14 anos 164 cm')

    vendido_2_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_3_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')
    vendido_4_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')
    vendido_5_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_6_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')
    vendido_7_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')
    vendido_8_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='nrº vendido')
    vendido_9_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')
    vendido_10_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='nrº vendido')

    stock_2_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='stock 2/3 anos 90cm')
    stock_3_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 3/4 anos 100cm')
    stock_4_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 4/5 anos 110cm')
    stock_5_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='stock 5/6 anos 120cm')
    stock_6_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 6/7 anos 130cm')
    stock_7_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 7/8 anos 140cm')
    stock_8_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='stock 8/9 anos 150cm')
    stock_9_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 9/10 anos 160cm')
    stock_10_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='stock 10/11 anos 170cm')

    vendas_2_3_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='vendas 2/3 anos 90cm')
    vendas_3_4_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 3/4 anos 100cm')
    vendas_4_5_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 4/5 anos 110cm')
    vendas_5_6_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='vendas 5/6 anos 120cm')
    vendas_6_7_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 6/7 anos 130cm')
    vendas_7_8_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 7/8 anos 140cm')
    vendas_8_9_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0,  blank=True, null=True, verbose_name='vendas 8/9 anos 150cm')
    vendas_9_10_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 9/10 anos 160cm')
    vendas_10_11_anos = models.IntegerField(validators=[MinValueValidator(0)], default=0, blank=True, null=True, verbose_name='vendas 10/11 anos 170cm')


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, *args, **kwargs):

        self.stock_3_meses -= self.vendido_3_meses
        self.stock_6_meses -= self.vendido_6_meses
        self.stock_9_meses -= self.vendido_9_meses
        self.stock_12_meses -= self.vendido_12_meses
        self.stock_18_meses -= self.vendido_18_meses
        self.stock_2_anos -= self.vendido_2_anos
        self.stock_3_anos -= self.vendido_3_anos
        self.stock_4_anos -= self.vendido_4_anos
        self.stock_5_anos -= self.vendido_5_anos
        self.stock_6_anos -= self.vendido_6_anos
        self.stock_7_anos -= self.vendido_7_anos
        self.stock_8_anos -= self.vendido_8_anos
        self.stock_9_anos -= self.vendido_9_anos
        self.stock_10_anos -= self.vendido_10_anos
        self.stock_11_anos -= self.vendido_11_anos
        self.stock_12_anos -= self.vendido_12_anos
        self.stock_13_anos -= self.vendido_13_anos
        self.stock_14_anos -= self.vendido_14_anos

        self.vendas_3_meses += self.vendido_3_meses
        self.vendas_6_meses += self.vendido_6_meses
        self.vendas_9_meses += self.vendido_9_meses
        self.vendas_12_meses += self.vendido_12_meses
        self.vendas_18_meses += self.vendido_18_meses
        self.vendas_2_anos += self.vendido_2_anos
        self.vendas_3_anos += self.vendido_3_anos
        self.vendas_4_anos += self.vendido_4_anos
        self.vendas_5_anos += self.vendido_5_anos
        self.vendas_6_anos += self.vendido_6_anos
        self.vendas_7_anos += self.vendido_7_anos
        self.vendas_8_anos += self.vendido_8_anos
        self.vendas_9_anos += self.vendido_9_anos
        self.vendas_10_anos += self.vendido_10_anos
        self.vendas_11_anos += self.vendido_11_anos
        self.vendas_12_anos += self.vendido_12_anos
        self.vendas_13_anos += self.vendido_13_anos
        self.vendas_14_anos += self.vendido_14_anos

        self.stock_2_3_anos -= self.vendido_2_3_anos
        self.stock_3_4_anos -= self.vendido_3_4_anos
        self.stock_4_5_anos -= self.vendido_4_5_anos
        self.stock_5_6_anos -= self.vendido_5_6_anos
        self.stock_6_7_anos -= self.vendido_6_7_anos
        self.stock_7_8_anos -= self.vendido_7_8_anos
        self.stock_8_9_anos -= self.vendido_8_9_anos
        self.stock_9_10_anos -= self.vendido_9_10_anos
        self.stock_10_11_anos -= self.vendido_10_11_anos

        self.vendas_2_3_anos += self.vendido_2_3_anos
        self.vendas_3_4_anos += self.vendido_3_4_anos
        self.vendas_4_5_anos += self.vendido_4_5_anos
        self.vendas_5_6_anos += self.vendido_5_6_anos
        self.vendas_6_7_anos += self.vendido_6_7_anos
        self.vendas_7_8_anos += self.vendido_7_8_anos
        self.vendas_8_9_anos += self.vendido_8_9_anos
        self.vendas_9_10_anos += self.vendido_9_10_anos
        self.vendas_10_11_anos += self.vendido_10_11_anos

        self.vendido_3_meses = 0
        self.vendido_6_meses = 0
        self.vendido_9_meses = 0
        self.vendido_12_meses = 0
        self.vendido_18_meses = 0
        self.vendido_2_anos = 0
        self.vendido_3_anos = 0
        self.vendido_4_anos = 0
        self.vendido_5_anos = 0
        self.vendido_6_anos = 0
        self.vendido_7_anos = 0
        self.vendido_8_anos = 0
        self.vendido_9_anos = 0
        self.vendido_10_anos = 0
        self.vendido_11_anos = 0
        self.vendido_12_anos = 0
        self.vendido_13_anos = 0
        self.vendido_14_anos = 0

        self.vendido_2_3_anos = 0
        self.vendido_3_4_anos = 0
        self.vendido_4_5_anos = 0
        self.vendido_5_6_anos = 0
        self.vendido_6_7_anos = 0
        self.vendido_7_8_anos = 0
        self.vendido_8_9_anos = 0
        self.vendido_9_10_anos = 0
        self.vendido_10_11_anos = 0

        super().save(force_insert, force_update, *args, **kwargs)
        self.stock_3_meses = 0
        try :
            self.resize_image(self.imagem_post.name, 600)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        new_height = round(new_width * height / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)
        new_image.close()


class GaleriaPhotos(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    galeria = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Galeria')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.resize_image(self.galeria.name, 600)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        new_height = round(new_width * height / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)
        new_image.close()


class Contact(models.Model):
    name = models.CharField(max_length=150)
    telefone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(default='mensagem')
    artigo = models.ForeignKey(Post, related_name = 'artigo', on_delete=models.PROTECT, null=True, blank=True)
    tratado = models.BooleanField(default=False)
    data_contact = models.DateTimeField(default=timezone.now, verbose_name='Data')

    def __str__(self):
        return self.name
