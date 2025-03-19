
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from portfolioapi.models import Wiki,Section
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

class SectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'

class SectionsViewSet(ViewSet):

    permission_classes = (AllowAny,)

    def list(self, request):

        wiki_id = request.query_params.get('wiki')

        if not wiki_id:
            return Response({'error':'wiki ID must be provided in body'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            wiki=Wiki.objects.get(pk=wiki_id)
        except:
            return Response({'error':'wiki entry not found'},status=status.HTTP_404_NOT_FOUND)

        sections= Section.objects.filter(wiki=wiki)
        if not sections.exists():
            return Response({'error':'no section entries associated this wiki'}, status=status.HTTP_404_NOT_FOUND)

        serialized_sections = SectionsSerializer(sections,many=True)
        return Response(serialized_sections.data, status=status.HTTP_200_OK)