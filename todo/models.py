from django.db import models

# Create your models here.
#Kullaancağımız tabloları modeller halinde burada hazırlıyoruz.
class Todo(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık")
    completed = models.BooleanField(verbose_name="Durum")
    # id özelliğini eklememize gerek yok django kendisi otomatik ekliyor
    def __str__(self) -> str: 
        # Burada admin paanelinde kaydedilen verilerimiz Todo project başlığı ile gözüküyordu, biz başlığı şeklinde gözüksün istedik opndan dolayı alttakini yaptık
        return self.title
    