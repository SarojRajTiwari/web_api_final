from rest_framework import serializers
from django.utils.text import slugify

from apis.news.models import News

class CreateNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'title', 'article', 'category', 'cover_image'
        extra_kwargs = {
            'author':{'required':False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(kwargs)
        context = kwargs.get('context')
        request = context.get('request')
        print(request.user)
        self.author = request.user
        
    def create(self, validate_data):
        title = validate_data.get('title')
        print(validate_data)
        slug = slugify(title)
        author = self.author
        # print(author)
        # print(validate_data)
        news = News.objects.create(**validate_data, slug=slug, author = author)
        print(news)
        print(news.author, news.slug)
        return news


class UpdateNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'article', 'category', 'author']

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title')
        instance.article = validate_data.get('article')
        instance.category = validate_data.get('category')
        slug = slugify(validate_data.get('title'))
        instance.slug = validate_data.get('slug', slug)
        print(validate_data)
        print(slug)
        instance.save()
        print(instance)
        print(instance.slug)
        return instance


class ListNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'article', 'category', 'author', 'slug', 'created_at']


class RetrieveNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'article', 'category', 'author', 'slug']


class DestroyNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News


class RequestUserNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'article', 'category', 'author']
    
    