from django.shortcuts import render
from rest_framework.generics \
        import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from helpers.permissions import IsNewsCreator, IsNewsAuthor
from apis.news.serializers \
        import CreateNewsSerializers, UpdateNewsSerializers, ListNewsSerializers, RetrieveNewsSerializers, DestroyNewsSerializers, RequestUserNewsSerializers
from apis.news.models import News


class CreateNewsAPIView(CreateAPIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsNewsCreator]
    serializer_class = CreateNewsSerializers

class UpdateNewsAPIView(UpdateAPIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsNewsCreator, IsNewsAuthor]
    serializer_class = UpdateNewsSerializers
    # queryset = News.objects.all()

    def get_queryset(self):
        print(self.kwargs)
        return News.objects.filter(pk=self.kwargs['pk'])
    

class ListNewsAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListNewsSerializers
    def get_queryset(self):
        return News.objects.all()



class RetrieveNewsAPIView(RetrieveAPIView): # we should return list of object// filter gives list of object
    permission_classes = [AllowAny]
    serializer_class = RetrieveNewsSerializers
    def get_queryset(self):
        return News.objects.filter(pk=self.kwargs['pk'])


class DestroyNewsAPIView(DestroyAPIView):
    authentication_class = [JWTAuthentication] # not mandatory
    permission_classes = [IsNewsCreator, IsNewsAuthor] # mandatory field
    serializer_class = DestroyNewsSerializers
    queryset = News.objects.all()


def category_news(request):
    category = News.CATEGORY
    return JsonResponse(dict(category))

def politics_news_list(request):
    print(News.objects.filter(category='0'))
    politics = News.objects.filter(category='0')
    try:
        print({n:politic.title for n in range(len(politics)) for politic in politics})    
        print({politic.pk:[politic.title, politic.author]  for politic in politics})    
        politics_news = {n:{politics[n].pk:politics[n].title} for n in range(len(politics))}    
        return JsonResponse(politics_news)
    except ObjectDoesNotExist as e:
        return HttpResponse("NO ANY POLITICS NEWS")


def technologies_news_list(request):
    technologies = News.objects.filter(category='1')
    print(technologies[0])
    print(len(technologies))
    try:
        technologies_news = {n:{technologies[n].pk:technologies[n].title} for n in range(len(technologies))}
        print(technologies_news)
        return JsonResponse(technologies_news)
    except ObjectDoesNotExist as e:
        return HttpResponse("NO ANY TECHNOLOGIES NEWS")



def sports_news_list(request):
    sports = News.objects.filter(category='2')
    try:
        sports_news = {n:{sports[n].pk:sports[n].title} for n in range(len(sports))}
        if sports_news:
            return JsonResponse(sports_news)
        else:
            raise ObjectDoesNotExist('NO ANY SPORTS NEWS')
    except ObjectDoesNotExist as e:
        return HttpResponse(f"<h1>{e}</h1>")


def fashions_news_list(request):
    fashions = News.objects.filter(category='3')
    try:
        fashions_news = {n:{fashions[n].pk:fashions[n].title} for n in range(len(fashions))}
        if fashions_news:
            return JsonResponse(fashions_news)
        else:
            raise ObjectDoesNotExist('NO ANY FASHIONS NEWS')
    except ObjectDoesNotExist as e:
        return HttpResponse(f"<h1>{e}</h1>")



class RequestUserNewsAPIView(ListAPIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = RequestUserNewsSerializers
    def get_queryset(self):
        print(self.request.user)
        return News.objects.all()

