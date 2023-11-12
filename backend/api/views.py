from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework import status

from . models import Blog
from . serializers import BlogSerializer

BLOG_URL_CREATE = '/blog/create/'



@api_view(['GET'])
def get_blogs(request):
    """Take all blogs instead in db."""

    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_blog(request):
    """Create a blog."""   
    

    data = request.data
    
    if 'body' not in data:
        return Response({'error': 'A chave "body" é necessária.'})
    
    blog = Blog.objects.create(body = data['body'])
    serializer = BlogSerializer(blog)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_blog(request, pk):
    """Update a blog instance."""

    data = request.data
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def delete_blog(request, pk):
    """Delete a blog instance."""

    blog = Blog.objects.get(id=pk)
    blog.delete()

    return  Response('Blog Deletado!', status=status.HTTP_204_NO_CONTENT)