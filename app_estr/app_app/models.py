from django.conf import settings
from django.db import models
from django.utils import timezone


class Unidade(models.Model):
    
    CLASSES = [('A', 'Assistência Social'), ('E','Educação'), ('S', 'Saude'), ('EL','Esporte e Lazer'), ('P','Prédios Públicos'), ('M', 'Meio Ambiente'), ('S','Saneamento'), ('C','Cultura'), ('O', 'Outros')]
    A_UNIDADES = [('CREAS','CREAS'), ('CRAS', 'CRAS'), ('Abrigo', 'Abrigo'), ('Centro POP', 'Centro POP'), ('Centro Dia', 'Centro Dia'), ('Centro de Convivência','Centro de Convivência'), ('Conselho Tutelar', 'Conselho Tutelar'), ('AMA', 'AMA'), ('LAC','LAC'), ('ASA', 'ASA'), ('APAE', 'APAE'), ('APADA', 'APADA'), ('Casa', 'Casa')]
    
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    classe = models.CharField(max_length=100, choices=CLASSES)
    print(classe.get_choices)
    unidade = models.CharField(max_length=200)
    zone = models.CharField(max_length=100, blank=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
