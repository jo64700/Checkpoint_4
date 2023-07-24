from rest_framework import serializers
from ..fiche_technique.models import Voiture

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        # fields = '__all__'
        fields = ('id', 'modele', 'annee', 'prix_depart', 'fabricant', 'moteur', 'transmission', 'technique', 'performance', 'consommation', 'dimension', 'habitabilite', 'pneu')




