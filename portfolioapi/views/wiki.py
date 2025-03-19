from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from portfolioapi.models import Wiki,Topic
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist

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

        topic_id = request.query_params.get('topic')

        if not topic_id:
            return Response({'error':'PK must be provided or topic ID must be provided as a query param'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            topic = Topic.objects.get(pk=topic_id)
        except ObjectDoesNotExist:
            return Response({'error':'topic entry not found'}, status=status.HTTP_404_NOT_FOUND)
        

        wikis = Wiki.objects.filter(topic=topic)
        if len(wikis) == 0:
            return Response({'error':'no wiki entries associated this topic'}, status=status.HTTP_404_NOT_FOUND)

        serialized_wikis = WikisSerializer(wikis,many=True)
        return Response(serialized_wikis.data, status=status.HTTP_200_OK)