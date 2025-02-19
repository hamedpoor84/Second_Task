from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import PostSerializer , LikeSerializer , CommentSerializer

class PostListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)

    def post(self , request ):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self , request ,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        if post is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


    def patch (self , request , pk):
        post = self.get_object(pk)
        if post is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if post.user == request.user:
            serializer = PostSerializer(post , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"error" : "You don't have permission to edit this post"})


    def delete (self , request , pk):
        post = self.get_object(pk)
        if post is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if post.user == request.user:
            post.delete()
            return Response({"massage" : "post deleted"})
        return Response({"error" : "You don't have permission to delete this post"})
    
class GetLikeByPostIDAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def post(self, request, post_ID):
        post = self.get_object(post_ID)
        like , created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            post.like_count = post.like_count + 1
            post.save()
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            post.like_count = post.like_count - 1
            post.save()
            return Response({"message": "Like removed"}, status=status.HTTP_204_NO_CONTENT) # vasam ajibe ke baray gereftan like haye ye post ye class joda bezanam
        
class GetCommentByIDAPIView(APIView):
    permissoin_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
        
    def post (self, request, post_ID):
        post = self.get_object(post_ID)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user , post=post)
            post.comment_count = post.comment_count + 1
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, user=request.user)  # Ensure user owns the comment
        post = comment.post 
        post.comment_count = post.comment_count - 1
        post.save()
        comment.delete()
        return Response({"message": "Comment deleted"}, status=status.HTTP_204_NO_CONTENT)

class GetPostCommentsAPIView(APIView) :
    permissoin_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
        
    def post (self, request, post_ID):
        post = self.get_object(post_ID)
        if post :
            comments = Comment.objects.filter(post=post).order_by("created_at")
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=200)  # Return serialized data
        return(Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND))



