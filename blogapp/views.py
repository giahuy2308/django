from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Account
from .serializers import *


class AccountListView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class MainPageView(RetrieveUpdateDestroyAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer


class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer


class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
