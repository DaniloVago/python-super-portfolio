from rest_framework import viewsets
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
    )
from projects.serializers import (
    ProfileSerializer,
    ProjectsSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    )
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        profile = Profile.objects.get(pk=id)
        context = {'profile': profile}

        if request.method == 'GET':
            return render(
                request,
                'profile_detail.html',
                context,
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
