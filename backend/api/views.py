from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def get_blogs(request):
    """Take all blogs instead in db."""

    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post_blog(request):
    """Create a blog."""

    data = request.data
    blog = Blog.objects.create(
        body = data['body']
    )
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def att_blog(request, pk):
    """Att a blog instance."""

    data = request.data
    blog = Blog.objects.get(id=pk)
    serialzizer = BlogSerializer(instance=blog, data=data)
    return Response(Serializer.data)



@api_view(['DELETE'])
def delete_blog(request, pk):
    """Delete a blog instance."""

    blog = Blog.objects.get(id=pk)
    blog.delete()
    return  Response('Blog Deletado!')