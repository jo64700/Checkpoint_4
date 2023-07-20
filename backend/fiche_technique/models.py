from django.db import models

# Create your models here.


class Fabricant(models.Model):
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Moteur(models.Model):
    nom_moteur = models.CharField(max_length=100)
    cylindre = models.DecimalField(max_digits=4, decimal_places=2)
    energie = models.CharField(max_length=100)
    architecture = models.CharField(max_length=100)
    alimentation = models.CharField(max_length=100)
    injection = models.CharField(max_length=100)
    alésage = models.DecimalField(max_digits=4, decimal_places=2)
    course = models.DecimalField(max_digits=4, decimal_places=2)
    dispostion = models.CharField(max_length=100)
    soupape = models.IntegerField()
    puissance_max = models.IntegerField()
    regime_puissance_max = models.IntegerField()
    couple_max = models.IntegerField()
    regime_couple_max = models.IntegerField()

    def __str__(self):
        return f"{self.nom_moteur} {self.cylindre} cm3 {self.energie} {self.architecture} {self.alimentation} {self.injection} {self.alésage} x {self.course} {self.dispostion} {self.soupape} {self.puissance_max} ch {self.regime_puissance_max} tr/min {self.couple_max}Nm {self.regime_couple_max} tr/min"


class Transmission(models.Model):
    boite_de_vitesse = models.CharField(max_length=100)
    rapport = models.IntegerField()
    mode_transmission = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.boite_de_vitesse} {self.rapport} {self.mode_transmission}"


class Technique(models.Model):
    chassis = models.CharField(max_length=100)
    materiel_chassis = models.CharField(max_length=100)
    diametre_braquage = models.DecimalField(max_digits=4, decimal_places=2)
    type_suspension_avant = models.CharField(max_length=200)
    type_suspension_arriere = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.chassis} {self.materiel_chassis} {self.diametre_braquage} m {self.type_suspension_avant} {self.type_suspension_arriere}"


class Performance(models.Model):
    vitesse_max = models.IntegerField()
    depart_arreter = models.DecimalField(max_digits=4, decimal_places=2)
    drag = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.vitesse_max} km/h {self.depart_arreter} s {self.drag} s"


class Consommation(models.Model):
    cycle_urbain = models.DecimalField(max_digits=4, decimal_places=2)
    extra_urbain = models.DecimalField(max_digits=4, decimal_places=2)
    mixte = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.cycle_urbain} L/100km {self.extra_urbain} L/100km {self.mixte} L/100km"


class Dimension(models.Model):
    longueur = models.DecimalField(max_digits=4, decimal_places=2)
    largeur = models.DecimalField(max_digits=4, decimal_places=2)
    hateur = models.DecimalField(max_digits=4, decimal_places=2)
    empattement = models.DecimalField(max_digits=4, decimal_places=2)
    reservoir = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.longueur} m {self.largeur} m {self.hateur} m {self.empattement} m {self.reservoir} L"


class Habitabilite(models.Model):
    nombre_place = models.IntegerField()
    volume_coffre = models.IntegerField()
    volume_coffre_utile = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_place} {self.volume_coffre} L {self.volume_coffre_utile} L"


class Pneu(models.Model):
    type_pneu = models.CharField(max_length=100)
    taille_roue_avant = models.CharField(max_length=100)
    taille_roue_arriere = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_pneu} {self.taille_roue_avant} {self.taille_roue_arriere}"


class Voiture(models.Model):
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    prix_depart = models.DecimalField(max_digits=10, decimal_places=2)
    fabricant = models.ForeignKey(Fabricant, on_delete=models.CASCADE)
    moteur = models.ForeignKey(Moteur, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    consommation = models.ForeignKey(Consommation, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    habitabilite = models.ForeignKey(Habitabilite, on_delete=models.CASCADE)
    pneu = models.ForeignKey(Pneu, on_delete=models.CASCADE)
