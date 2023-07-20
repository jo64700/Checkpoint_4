from django.contrib import admin
from .models import Fabricant
from .models import Moteur
from .models import Transmission
from .models import Technique
from .models import Performance
from .models import Consommation
from .models import Dimension
from .models import Habitabilite
from .models import Pneu
from .models import Voiture

# Register your models here.

class FabricantAdmin(admin.ModelAdmin):
    list_display = ['nom', 'pays']
    

class MoteurAdmin(admin.ModelAdmin):
    list_display = ['nom_moteur', 'cylindre', 'energie', 'architecture','alimentation', 'alésage','course', 'dispostion', 'puissance_max', 'regime_puissance_max', 'couple_max', 'regime_couple_max']

class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['boite_de_vitesse', 'rapport', 'mode_transmission']

class TechniqueAdmin(admin.ModelAdmin):
    list_display = ['chassis','materiel_chassis','diametre_braquage','type_suspension_avant','type_suspension_arriere']

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['vitesse_max','depart_arreter', 'drag']

class ConsommationAdmin(admin.ModelAdmin):
    list_display = ['cycle_urbain','extra_urbain', 'mixte']

class DimensionAdmin(admin.ModelAdmin):
    list_display = ['longueur','largeur', 'hateur','empattement', 'reservoir']
    
class HabitabiliteAdmin(admin.ModelAdmin):
    list_display = ['nombre_place','volume_coffre','volume_coffre_utile']
    
class PneuAdmin(admin.ModelAdmin):
    list_display = ['type_pneu', 'taille_roue_avant', 'taille_roue_arriere']

class VoitureAdmin(admin.ModelAdmin):
    list_display = ['modele','prix_depart','fabricant','transmission','technique','performance','consommation','dimension','habitabilite','pneu']

admin.site.register(Fabricant, FabricantAdmin)
admin.site.register(Moteur, MoteurAdmin)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Consommation, ConsommationAdmin)
admin.site.register(Dimension, DimensionAdmin)
admin.site.register(Habitabilite, HabitabiliteAdmin)
admin.site.register(Pneu, PneuAdmin)
admin.site.register(Voiture, VoitureAdmin)
