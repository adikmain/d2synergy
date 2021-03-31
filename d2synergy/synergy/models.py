from django.db import models
from django.urls import reverse


# class SynergyHeroes(models.Model):
#     hero_name = models.CharField(max_length=255, verbose_name='Имя героя')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
#     hero_bio = models.TextField(blank=True, verbose_name='Биография')
#
#     def __str__(self):
#         return self.hero_name
#
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Биография персонажей'
#         verbose_name_plural = 'Биографии персонажей'
#         ordering = ['pk']
#

