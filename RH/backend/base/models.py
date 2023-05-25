from django.db import models
# Create your models here.
#class Profil(models.Model):
   # Emp = models.IntegerField(null=True, blank=True)
    #RH= models.IntegerField(null=True, blank=True)



class Employe(models.Model):
   # id= models.ForeignKey(Profil, on_delete=models.SET_NULL,null=True)
    nom = models.CharField(max_length=200, null=True, blank=True)
    prenom = models.CharField(max_length=200, null=True, blank=True)
    adresse= models.CharField(max_length=200, null=True, blank=True)
    CIN = models.CharField(max_length=200, null=True, blank=True,unique=True)
    email = models.EmailField(max_length=200, null=True, blank=True, help_text='enter your employee email')
    tel = models.CharField(max_length=10, blank=True,null=True, unique=True)
    CNSS = models.CharField(max_length=200, null=True, blank=True, unique=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    langue = models.TextField(max_length=100, null=True, blank=True)
    passwd = models.CharField(max_length=10, null=True, blank=True)
    #createAt = models.DateTimeField(auto_now_add=True)
    profil= models.CharField(max_length=200,null=True, blank=True)
    login= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nom

class Conge(models.Model):
     Nom= models.CharField(max_length=200, null=True, blank=True)
     Prenom= models.CharField(max_length=200, null=True, blank=True)
     Type= models.CharField(max_length=200, null=True, blank=True)
     DateDebut= models.DateField(null=True, blank=True)
     DateFin= models.DateField(null=True, blank=True)

     def __str__(self):
         return self.Type

class Diplome(models.Model):
     employe = models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True)
     nom= models.CharField(max_length=200, null=True, blank=True)
     dateD= models.DateField(null=True, blank=True)

class Competence(models.Model):
     employe=models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True)
     nom= models.TextField(max_length=100, null=True, blank=True)

class CV(models.Model):
    employe= models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True)
    CV_image= models.ImageField(null=True,blank=True)


class FichePaie(models.Model):
    nom= models.CharField(max_length=200, null=True, blank=True)
    prenom= models.CharField(max_length=200, null=True, blank=True)
    salaire=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)


