from movieapp.models import Tweet
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def homepage(request):

    tweets = Tweet.objects.all()
    if(request.method == 'GET'):
        serializers = TweetSerializer(tweets, many=True)
        return Response(serializers.data)
    if(request.method == 'POST'):
        serializers = TweetSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def detailpage(request, pk):
    tweets = Tweet.objects.get(pk=pk)
    if(request.method == "GET"):
        serializers = TweetSerializer(tweets)
        return Response(serializers.data)
    if(request.method == "PUT"):
        serializer = TweetSerializer(tweets, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if(request.method == "DELETE"):
        tweets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
