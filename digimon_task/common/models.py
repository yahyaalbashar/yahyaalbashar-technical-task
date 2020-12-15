from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

class Digimon(models.Model):
    name=models.CharField(max_length=255)
    image=models.URLField()
    level=models.CharField(max_length=255)
    is_favorite=models.BooleanField()
    slug=models.SlugField(allow_unicode=True)

    def save(self, *args, **kwargs):
        name=self.name
        name=slugify(name)
        self.slug=name
        super(Digimon,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("digimon_detail", kwargs={"slug": self.slug})
    
