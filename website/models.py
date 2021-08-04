from django.db import models
from django.utils import timezone
from PIL import Image
from django.conf import settings
from django.core.validators import MinValueValidator
import os

# Create your models here.

class Categorias(models.TextChoices):
    menino = 'Menino', 'Menino'
    menina = 'Menina', 'Menina'


class Post(models.Model):
    referencia = models.CharField(max_length=100, verbose_name='Referencia')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    categories = models.CharField(max_length=6, blank=True, null=True,
                                 choices= Categorias.choices,
                                 default= Categorias.menino,)
    content = models.TextField(verbose_name='Descricao')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', verbose_name='Imagem De Perfil')
    price = models.DecimalField(max_digits=6,  decimal_places=2, blank=True, null=True, verbose_name='Preco')
    promocao = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Promocao')
    stock_bebe = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Stock Bebé')
    stock_crianca = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Stock Criança')
    stock_junior = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Stock Junior')
    vendas_bebe = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Vendas Bebé')
    vendas_crianca = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Vendas Criança')
    vendas_junior = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name='Vendas Junior')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try :
            self.resize_image(self.imagem_post.name, 600)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        # if width <= new_width:
        #     img.close()
        #     return

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

        # if width <= new_width:
        #     img.close()
        #     return

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