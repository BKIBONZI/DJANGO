from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    #categorie = models.ForeignKey(Categorie)

    def __str__(self):
        return self.titre


class Arriveesc(models.Model):
    dater = models.CharField(max_length=10)
    jsdater = models.CharField(max_length=2, default=None, null=True, blank=True)
    numr = models.IntegerField()
    nbcr = models.IntegerField(blank=True, null=True)
    noctr = models.BooleanField(default=False)
    paysr = models.CharField(max_length=30)
    viller = models.CharField(max_length=30)
    Hippor = models.CharField(max_length=30, default=None, null=True, blank=True )
    numc = models.IntegerField()
    hdepc = models.CharField(max_length=5)
    nomc = models.CharField(max_length=30, default=None, null=True, blank=True)
    typec = models.CharField(max_length=30)
    prixc = models.IntegerField()
    distc = models.IntegerField()
    nbptsc = models.IntegerField()
    quintc = models.BooleanField(default=False)
    arv1c = models.IntegerField()
    arv2c = models.IntegerField()
    arv3c = models.IntegerField()
    arv4c = models.IntegerField()
    arv5c = models.IntegerField(blank=True, null=True)
    rapms4c = models.DecimalField(max_digits=7, decimal_places=2)
    exaquoarvc = models.BooleanField(default=False)

    def __str__(self):
        return self.dater


class Artileocr1(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default = timezone.now, verbose_name="Date de parution")

    class meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        """
        Cette methode que nous definirons dans tous les modeles nous permettra de reconnaitre 
        facilement les differents objets que nous traiterons plus tard sans l'administration
        """

        return self.titre


class Categorieocr1(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom 

class Articleocr1(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorieocr1', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.titre



class Partants(models.Model):
    datec = models.CharField(max_length=30)
    numr = models.IntegerField()
    numc = models.IntegerField()
    numch = models.IntegerField()
    nomch =  models.CharField(max_length=30)
    particular1 = models.CharField(max_length = 30, null=True, blank=True)
    particular2 = models.CharField(max_length = 30, null=True, blank=True)
    nomjock = models.CharField(max_length=30)
    redkm = models.CharField(max_length=30, null=True, blank=True) 
    coteavt = models.DecimalField(max_digits=5, decimal_places=1)
    coteapr = models.DecimalField(max_digits=5, decimal_places=1)
    commentapc = models.TextField(null=True)
    rang = models.IntegerField()
    motifrg = models.CharField(max_length=10, null=True, blank=True)

    def __str__(numch):
        return self.numch
