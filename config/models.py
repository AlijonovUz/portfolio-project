from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Texnalogiya "
        verbose_name_plural = "Texnalogiyalar"


class Portfolio(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")
    description = models.CharField(max_length=100, verbose_name="Tavsifi")
    photo = models.ImageField(upload_to='images/', verbose_name="Rasmi")
    technologies = models.ManyToManyField(Technology, related_name='portfolio', verbose_name="Texnalogiyasi")
    demo = models.URLField(null=True, blank=True, verbose_name="Demo havolasi")
    github = models.URLField(null=True, blank=True, verbose_name="GitHub havolasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loyiha "
        verbose_name_plural = "Loyihalar"


class Data(models.Model):
    cv = models.FileField(upload_to='uploads/', verbose_name="Rezyume")
    linkedin = models.URLField(null=True, blank=True, verbose_name="Linkedin havolasi")
    instagram = models.URLField(null=True, blank=True, verbose_name="Instagram havolasi")
    telegram = models.URLField(null=True, blank=True, verbose_name="Telegram havolasi")
    github = models.URLField(null=True, blank=True, verbose_name="GitHub havolasi")
    email = models.EmailField(default="admin@example.com", verbose_name="Elektron pochta manzili")
    phone = models.CharField(max_length=13, default="+998901234567", verbose_name="Telefon raqam")
    address = models.CharField(max_length=100, default="O'zbekiston, Toshkent", verbose_name="Uy manzili")

    def __str__(self):
        return self.address or "Ma'lumotlar"

    class Meta:
        verbose_name = "Ma'lumot "
        verbose_name_plural = "Ma'lumotlar"