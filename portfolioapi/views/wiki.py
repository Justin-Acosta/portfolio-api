
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from portfolioapi.models import Wiki,Topic
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

class WikisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wiki
        fields = '__all__'

class WikisViewSet(ViewSet):

    permission_classes = (AllowAny,)

    def retrieve(self,request,pk):
        
        try:
            wiki = Wiki.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'wiki entry not found'}, status=status.HTTP_404_NOT_FOUND)

        serialized_wiki = WikisSerializer(wiki)
        return Response(serialized_wiki.data, status=status.HTTP_200_OK)
    

    def list(self, request):

        topic_id = request.data.get('topic')
        
        if topic_id:
            try:
                topic = Topic.objects.get(pk=topic_id)
                wikis = Wiki.objects.filter(topic=topic)
            except ObjectDoesNotExist:
                return Response({'error':'topic entry not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            wikis = Wiki.objects.all()

        if not wikis.exists():
            return Response({'error':'no wiki entries found'}, status=status.HTTP_204_NO_CONTENT)

        serialized_wikis = WikisSerializer(wikis,many=True)
        return Response(serialized_wikis.data, status=status.HTTP_200_OK)