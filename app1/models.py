from django.db import models
# from django.db.models.fields import EmailField
# from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.


class Controller(models.Model):

    # Controller = models.ImageField(upload_to="images")
    title = models.CharField(max_length=40,null=True)
    blurController      = models.ImageField(default="blur-image.jpeg", null=True)
    originalController  = models.ImageField(upload_to="original_image", null=True)
    description = models.CharField(max_length=350, null=True)

    # multiController1  = models.ImageField(upload_to="original_image", null=True)
    # multiController2  = models.ImageField(upload_to="original_image", null=True)
    # multiController3  = models.ImageField(upload_to="original_image", null=True)
    # multiController4  = models.ImageField(upload_to="original_image", null=True)

    # TestingByDirectHTml = models.FileField(upload_to="posrtHtmls",null=True)

    def get_blur_image_url(self):
        return reverse("blur_image_view", args=[str(self.id)])

    def get_original_image_view(self, password):
        return reverse("image_view", args=[str(password), str(self.id)])


class EmbeddedLinux(models.Model):
    title = models.CharField(max_length=40,null=True)
    blurEmbeddedLinux = models.ImageField(default="blur-image.jpeg",null=True)
    originalEmbeddedLinux = models.ImageField(upload_to="original_image_01",null=True)
    # EmbeddedLinux = models.ImageField(upload_to="images")
    description = models.CharField(max_length=350,null=True)

    multiImgEmb1  = models.ImageField(upload_to="original_image", null=True)
    multiImgEmb2  = models.ImageField(upload_to="original_image", null=True)
    multiImgEmb3  = models.ImageField(upload_to="original_image", null=True)
    multiImgEmb4  = models.ImageField(upload_to="original_image", null=True)

    def get_blur_image_url_01(self):
        return reverse("blur_image_view_01", args=[str(self.id)])

    def get_original_image_view_01(self, password):
        return reverse("image_view_01", args=[str(password), str(self.id)])

class PcbDesigning(models.Model):
    title = models.CharField(max_length=40,null=True)
    blurPcbDesigning = models.ImageField(default="blur-image.jpeg",null=True)
    originalPcbDesigning = models.ImageField(upload_to="original_image_02",null=True)
    # PcbDesigning = models.ImageField(upload_to="images")
    description = models.CharField(max_length=350,null=True)

    def get_blur_image_url_02(self):
        return reverse("blur_image_view_02", args=[str(self.id)])

    def get_original_image_view_02(self, password):
        return reverse("image_view_02", args=[str(password), str(self.id)])


class WebApp(models.Model):
    title = models.CharField(max_length=40,null=True)
    blurWebApp = models.ImageField(default="blur-image.jpeg",null=True)
    originalWebApp = models.ImageField(upload_to="original_image_03",null=True)
    # WebApp = models.ImageField(upload_to="images")
    description = models.CharField(max_length=350,null=True)

    def get_blur_image_url_03(self):
        return reverse("blur_image_view_03", args=[str(self.id)])

    def get_original_image_view_03(self, password):
        return reverse("image_view_03", args=[str(password), str(self.id)])
