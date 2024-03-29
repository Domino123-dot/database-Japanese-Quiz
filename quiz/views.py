from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def questions_list(request):
    if request.method == 'GET':
        data = questions.objects.all()

        serializer = questionsSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = questionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT', 'DELETE'])
def questions_detail(request, pk):
    try:
        question = questions.objects.get(pk=pk)
    except questions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = questionsSerializer(question, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def changelog_list(request):
    if request.method == 'GET':
            data = changelog.objects.all()

            serializer = changelogSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = changelogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def discordBot_list(request):
    if request.method == 'GET':
            data = DiscordBotRequests.objects.all()

            serializer = changelogSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = changelogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)