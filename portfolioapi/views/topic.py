from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from portfolioapi.models import Topic
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist

class TopicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'

class TopicsViewSet(ViewSet):

    permission_classes = (AllowAny,)

    def retrieve(self,request,pk):
        
        try:
            topic = Topic.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'topic entry not found'}, status=status.HTTP_404_NOT_FOUND)

        serialized_topic = TopicsSerializer(topic)
        return Response(serialized_topic.data, status=status.HTTP_200_OK)
    

    def list(self, request):

        topics = Topic.objects.all()
        if len(topics) == 0:
            return Response({'error':'no topic entries found'}, status=status.HTTP_404_NOT_FOUND)

        serialized_wikis = TopicsSerializer(topics,many=True)
        return Response(serialized_wikis.data, status=status.HTTP_200_OK)