from django.conf import settings
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager
from django.utils import timezone

# Create your models here.

# class District(models.Model):
#     district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))
#     district=models.CharField(max_length=100,blank=False,choices=district_list)
#     def __str__(self):
#         return '{}'.format(self.district)
# class Region(models.Model):
#     list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
#     region=models.CharField(max_length=100,blank=False,choices=list_region)
#     def __str__(self):
#         return '{}'.format(self.region)
# class Departement(models.Model):
#     departement=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.departement)
# class Sous_prefecture(models.Model):
#     sous_prefecture=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.sous_prefecture)
# class Commune(models.Model):
#     commune=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.commune)
# class Milieu(models.Model):
#     milieu_r=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}'.format(self.milieu_r)
# class Quartier(models.Model):
#     quartier=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return '{}_{}'.format(self.quartier)

# class Affecter(models.Model):
#     agentr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     localite=models.ForeignKey(Localite,on_delete=models.CASCADE)
#     create=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return '{}_{}'.format(self.agentr,self.localite)

class Personne(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    prenom=models.CharField(max_length=100,blank=False)
    annee_naissance=models.DateField(blank=False)
    lieu_de_naissance=models.CharField(max_length=100,blank=False,default="abidjan")
    nationalite=models.CharField(max_length=100,blank=False,default="ivoirienne")
    numero_cni=models.CharField(max_length=100,blank=False)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    ethnie=models.CharField(max_length=100,blank=False)
    numero=models.CharField(max_length=100,blank=False)
    district_list=(('A','Abidjan'),('B','Bas_Sassandra'),('C','Comoe'),('D','Denguele'),('G','Goh_Djiboua'),('L','Lacs'),('La','Lagunes'),('M','Montagnes'),('SM','Sassandra_Marahoue'),('Sa','Savanes'),('Va','Vallee_du_Bandama'),('W','Woroba'),('Y','Yamoussoukro'),('Za','Zanzan'))
    district=models.CharField(max_length=100,blank=False,choices=district_list)
    list_region=(('A','Abidjan'),('AT','Agneby_tiassa'),('Ba','Bafing'),('Ba','Bagoue'),('Be','Belier'),('B','Bere'),('Bo','Bounkani'),('Ca','Cavally'),('Fo','Folon'),('Gb','Gbeke'),('Gbo','Gbokle'),('Go','Goh'),('Gu','Guemon'),('In','Indenie_djuablin'),('Ka','Kabadougou'),('Na','Nawa'),('Lo','Loh_Djiboua'),('If',' Iffou'),('Mo','Moronou'),('Nz','Nzi'),('LM','La_Me'),('To','Tonkpi'),('Hs','Haut_Sassandra'),('Mr','Marahoué'),('Po','Poro'),('Tc','Tchologo'),('Ha','Hambol'),('Go','Gontougou'),('Sp','San_pedro'),('Sc','Sud_Comoe'),('Wo','Worodougou'))
    region=models.CharField(max_length=100,blank=False,choices=list_region)
    departement=models.CharField(max_length=100,blank=False)
    sous_prefecture=models.CharField(max_length=100,blank=False)
    commune=models.CharField(max_length=100,blank=False)
    milieu_r=models.CharField(max_length=100,blank=False,default='urbain')
    quartier=models.CharField(max_length=100,blank=False,default='Rue_12_Avenue_11')
    class Meta:
        abstract=True
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)

class Chef_menage(Personne):
    owner1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_chef_menage', on_delete=models.CASCADE,null=True)
    type_m=(('Mnf','Menage_non_familial'),('Mbn','Menage_biparental_nucléaire'),('Mbe','Ménage_Biparental_élargi'),('Mi','Ménage_isolé'),('Mm','Ménage_monoparental'),('Mme','Ménage_monoparental_elargi'))
    type_menage=models.CharField(max_length=100,blank=False,choices=type_m)
    nombre_enfant=models.IntegerField(default=0)
    nombre_enfant_v=models.IntegerField(default=0)
    nom_personne_charge=models.IntegerField(default=0)
    immigre=models.BooleanField(default=False)
    date_depart=models.DateField(null=True)
    age_depart=models.PositiveBigIntegerField()
    motif=models.CharField(max_length=100,blank=False)
    migrant=models.BooleanField()
    annee_deplace=models.DateField(blank=False)
    lieu_residence_a=models.CharField(max_length=100,blank=False)
    intention_ret=models.BooleanField()
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)
        
class Conjoint(models.Model):
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    occupation=models.CharField(max_length=100,blank=True,default='Informaticien')
    annee_naissance=models.DateField(blank=False)
    idc=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    owner2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_conjoint', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)
        
class Recenser(models.Model):
    parent=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    owner3 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_recenser', on_delete=models.CASCADE,null=True)
    list_religion=(('C','Catholique'),('M','Méthodique'),('E','Evangélique'),('Ce','Céleste'),('H','Harriste'),('Au','AutreRC'),('Mu','Mulsuman'),('An','Animiste'),('Au','AutreR'),('S','Sans_Religion'))
    religion=models.CharField(max_length=100,blank=False,choices=list_religion)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    list1=(('Vm','Vie_Ménage'),('Hm','Hors_Ménage'),('D','Décédé'),('N','RAS'))
    survie_de_mere=models.CharField(max_length=100,blank=False,choices=list1)
    survie_de_pere=models.CharField(max_length=100,blank=False,choices=list1 )
    alphabetisation=models.BooleanField(default=False)
    niveau_instruction=models.CharField(max_length=100,blank=False)
    status_occupation=models.CharField(max_length=100,blank=False)
    occupation_actuelle=models.CharField(max_length=100,blank=False)
    situation_occupation=models.CharField(max_length=100,blank=False)
    branche_activite=models.CharField(max_length=100,blank=False)
    situation_matrimoniale=models.CharField(max_length=100,blank=False)
    #Fins de mois assez difficile ou faciles
    Fins_de_mois=models.BooleanField(default=False)
    class Meta:
        ordering=['parent']
    def __str__(self):
        return '{}'.format(self.parent)

class Enfant(models.Model):
    parentf=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    annee_naissance=models.DateField(blank=False)
    owner4 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_enfant', on_delete=models.CASCADE,null=True)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    sexe=(('M','Maxculin'),('F','Feminin'))
    sexes=models.CharField(max_length=1,choices=sexe)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)
class Commodite(models.Model):
    parentc=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    owner5 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_commodite', on_delete=models.CASCADE,null=True)
    nombre_piece=models.IntegerField(default=1)
    nombre_piece_dormir=models.IntegerField(default=1)
    nature_mur=models.CharField(max_length=100,blank=False)
    nature_toit=models.CharField(max_length=100,blank=False)
    nature_sol=models.CharField(max_length=100,blank=False)
    lieu_aisance=models.CharField(max_length=100,blank=False)
    alimentation_eau=models.CharField(max_length=100,blank=False)
    temps_acces_eau=models.CharField(max_length=100,blank=False)
    eclairage=models.CharField(max_length=100,blank=False)
    cuisson=models.CharField(max_length=100,blank=False)
    evacuation_ordure=models.CharField(max_length=100,blank=False)
    evacuation_eau=models.CharField(max_length=100,blank=False)
    loyer=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parentc']

class Equipement(models.Model):
    parente=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    owner6 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_equipement', on_delete=models.CASCADE,null=True)
    moyen_deplacement=models.CharField(max_length=100,blank=False)
    equipement_electr=models.CharField(max_length=100,blank=False)
    equipement_audio=models.CharField(max_length=100,blank=False)
    statut_occupation=models.CharField(max_length=100,blank=False)
    class Meta:
        ordering=['parente']

class Deces(models.Model):
    parentd=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    owner7 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_deces', on_delete=models.CASCADE,null=True)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    annee_deces=models.DateField(blank=False)
    class Meta:
        ordering=['parentd']
    def __str__(self):
        return '{}_{}'.format(self.nom_decede,self.prenom_decede)

class Charge(models.Model):
    parentg=models.ForeignKey(Chef_menage,on_delete=models.CASCADE)
    sexed=(('M','Maxculin'),('F','Feminin'))
    sexesd=models.CharField(max_length=1,choices=sexed)
    annee_naissance=models.DateField(blank=False)
    owner8 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='list_charge', on_delete=models.CASCADE,null=True)
    niveau_etude=models.CharField(max_length=100,blank=True,default='master')
    occupation=models.CharField(max_length=100,blank=True,default='Informaticien')
    immigre=models.BooleanField(default=False)
    list_handicap=(('S','Sans_Handicap'),('Nv','Non_voyant'),('So','Sourd'),('Mu','Muet'),('Be','Begue'),('Al','Albinos'),('Hms','Handicap_membre_superieurs'),('Hmi','Handicap_membre_inferieurs'),('Hp','Handicap_physiques'),('Au','Autre_handicap'))
    handicap=models.CharField(max_length=100,blank=False,choices=list_handicap)
    intention_ret=models.BooleanField()
    def __str__(self):
        return '{}_{}'.format(self.nom,self.prenom)



