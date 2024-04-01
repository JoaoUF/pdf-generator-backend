from pdf_app.models.ProfileModel import Profile
from pdf_app.serializers.ProfileSerializer import ProfileSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
