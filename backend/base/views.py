from asyncio.windows_events import NULL


import form as form
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self,request):
       return render(request,'base.html',{})

class HomeEmp(View):
    def get(self,request):
        return render(request,'Emp.html',{})

class HomeResp(View):
    def get(self,request):
        return render(request,'Resp.html',{})

class EmployeList(View):
    def get(self,request):
        liste= Employe.objects.all() #récupérer tous les enrg depuis la BD, depuis le modèle Employe => select * from Employe
        return render(request,'listEmp.html',{'EmpKey':liste}) #envoyer à listEmp la variable liste qui contient les infos sur les emp

class DetailEmp(View):
    def get(self,request,idEmp): #il va prendre l'id comme input
        Emp=Employe.objects.get(id=idEmp) #récupérer la ligne que son id= id qu'on aura envoyé à la vue
        return render(request,'EmpDetails.html',{'empK':Emp})


class AjouterEmp(View):
    def get(self,request):
        formE = EmployeForm()
        return render(request,'addEmployee.html',{'frm': formE})
    def post(self,request): #permet de récupérer les données du formulaire entrés par l'utilisateur
        formE= EmployeForm(request.POST) # à travers la requete http post
        if formE.is_valid():
            formE.save()
            return HttpResponseRedirect('/listE/') # après le clique sur le btn Ajouter, on fait une redirection vers la page listEmp pour voir l'ajout
        return render(request,'addEmployee.html',{'frm': formE})



class DeleteEmployee(View):
    def get(self, request,idE):
        Employee= Employe.objects.get(id=idE)
        Employee.delete()
        return HttpResponseRedirect('/listE/')




class UpdateEmploye(View):
    def get(self,request,id):
        Employee=Employe.objects.get(id=id)
        form=EmployeForm(instance=Employee)
        return render(request,'addEmployee.html',{'frm':form})
    def post(self,request,id):
        Employee=Employe.objects.get(id=id)
        form= EmployeForm(request.POST,instance=Employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listE/')
        #return render(request,'addEmployee.html',{'frm':form})



class EmpInscription(View):
    def get(self,request):
       form=EmployeLogin() #le formulaire va être stocker dans la var form
       return render(request,'Cnx.html',{'f':form})
    def post(self, request):
       form = EmployeLogin(request.POST) #on récupère les données saisies
       if form.is_valid(): # Nous vérifions que les données envoyées sont valides
           log = form.cleaned_data['login'] #login saisie dans le formulaire
           pwd = form.cleaned_data['passwd']  # ou form.cleaned_data.get('passwd')
           #user=authenticate(request,login=log, passwd=pwd)
           #userU = Employe.objects.filter(login=log) # récupérer tous l'enregistrement
           empl = Employe.objects.get(login=log, passwd=pwd)
           if empl.profil == "Employe":
              return redirect('EmpAccount')
           if empl.profil == "Responsable":
                return redirect('RespAccount')
       else:
            #messages.error(request,"utilisateur n'existe pas")
            return render(request,'Cnx.html', {'f':form})


class DmdConge(View):

    def get(self,request):
        form = CongeForm()
        return render(request,'CongeCreate.html',{'f':form} )

    def post(self,request):
        form = CongeForm(request.POST)  # à travers la requete http post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/cnx/emp/')
        return render(request, 'CongeCreate.html', {'f': form})


class AfficherDemande(View):
    def get(self, request):
         newConge= Conge.objects.all()# récupérer tous les enregistrement de la table Conge
         return render(request,'AfficherDmdCong.html',{'CongKey':newConge})

class CongeAffichage(View):
    def get(self, request):
         newConge= Conge.objects.all()
         return render(request,'CongeSearch.html',{'CongKey':newConge})

class CongeDelete(View):
    def get(self, request,idG):
        Conges= Conge.objects.get(id=idG)
        Conges.delete()
        return HttpResponseRedirect('/GestionConge/')

class GestionCompetence(View):
    def get(self,request):
        form = CompForm()
        return render(request,'CompCreate.html',{'f':form} )

    def post(self,request):
        form = CompForm(request.POST)  # à travers la requete http post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/cnx/emp/')
        return render(request, 'CompCreate.html', {'f': form})

class ComptAffichage(View):
    def get(self, request):
         newCompt= Competence.objects.all()
         return render(request,'ComptSearch.html',{'CompKey':newCompt})

class CompDelete(View):
    def get(self, request,idC):
        CompetenceD= Competence.objects.get(id=idC)
        CompetenceD.delete()
        return HttpResponseRedirect('/Comp/AfficherCompetence/')

class UpdateCompetence(View):
    def get(self,request,idC):
        CompetenceM=Competence.objects.get(id=idC)
        form=CompForm(instance=CompetenceM)
        return render(request,'CompCreate.html',{'f':form})
    def post(self,request,idC):
        CompetenceM=Competence.objects.get(id=idC)
        form= CompForm(request.POST,instance=CompetenceM)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Comp/AfficherCompetence/')


class GestionDiplome(View):
    def get(self,request):
        form = DiplomeForm()
        return render(request,'DiplomeCreate.html',{'f':form} )

    def post(self,request):
        form = DiplomeForm(request.POST)  # à travers la requete http post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/cnx/emp/')
        return render(request, 'DiplomeCreate.html', {'f': form})

class DiplomeAffichage(View):
    def get(self, request):
         dipnew= Diplome.objects.all()
         return render(request,'AfficherDiplome.html',{'DKey':dipnew})

class DiplomeDelete(View):
    def get(self, request,idD):
        diplomes= Diplome.objects.get(id=idD)
        diplomes.delete()
        return HttpResponseRedirect('/Diplome/Afficher/')

class DiplomeUpdate(View):
    def get(self,request,idD):
        diplomes=Diplome.objects.get(id=idD)
        form=DiplomeForm(instance=diplomes)
        return render(request,'DiplomeCreate.html',{'f':form})
    def post(self,request,idD):
        diplomes=Diplome.objects.get(id=idD)
        form= DiplomeForm(request.POST,instance=diplomes)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Diplome/Afficher/')


class GestionCV(View):
    def get(self,request):
        form = CVForm()
        return render(request,'CVCreate.html',{'f':form} )

    def post(self,request):
        form = CVForm(request.POST,request.FILES)  # à travers la requete http post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/cnx/emp/')
        return render(request, 'CVCreate.html', {'f': form})

class AfficherCV(View):
    def get(self, request):
         newCV= CV.objects.all()
         return render(request,'CVAffichage.html',{'CVKey':newCV})


class CVAffImage(View):
    def get(self,request):
        newCV = CV.objects.all()
        return render(request,'afficherImage.html',{'CVKey':newCV})



class GestionFiche(View):
    def get(self,request):
        form = FicheForm()
        return render(request,'FicheCreate.html',{'f':form} )

    def post(self,request):
        form = FicheForm(request.POST)  # à travers la requete http post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/FichePaie/AfficherResp/')
        return render(request, 'FicheCreate.html', {'f': form})

class FicheAffichage(View):
    def get(self, request):
         fiche= FichePaie.objects.all()
         return render(request,'AfficherFicheP.html',{'FKey':fiche})


class FicheAffichageResp(View):
    def get(self, request):
         fiche= FichePaie.objects.all()
         return render(request,'AfficherFicheResp.html',{'FKey':fiche})

class FicheDelete(View):
    def get(self, request,idF):
        fiches= FichePaie.objects.get(id=idF)
        fiches.delete()
        return HttpResponseRedirect('/FichePaie/AfficherResp/')

class FicheUpdate(View):
    def get(self,request,idF):
        fiches=FichePaie.objects.get(id=idF)
        form=FicheForm(instance=fiches)
        return render(request,'FicheCreate.html',{'f':form})
    def post(self,request,idF):
        fiches=FichePaie.objects.get(id=idF)
        form= FicheForm(request.POST,instance=fiches)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/FichePaie/AfficherResp/')










