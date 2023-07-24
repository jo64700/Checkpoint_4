# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Voiture
# from ..car.serializers import VoitureSerializer
# from rest_framework import generics


# def get_voitures(request):
#     voitures = Voiture.objects.all()
#     serializer = VoitureSerializer(voitures, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def get_voiture_details(request, voiture_id):
#     voiture = get_object_or_404(Voiture, pk=voiture_id)
#     serializer = VoitureSerializer(voiture)
#     return JsonResponse(serializer.data)



# from django.shortcuts import render
# from rest_framework import generics
# from car.serializers import VoitureSerializer
# from .models import Voiture

# class VoitureView(generics.CreateAPIView):
#     queryset = Voiture.object.all()
#     serializer_class = VoitureSerializer