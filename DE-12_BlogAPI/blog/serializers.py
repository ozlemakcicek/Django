from rest_framework import serializers
from .models import (
    Category,
    Post
)


# api ile djangoya string,Json gonderilir.ama django bundan anlamaz modelden anlar.o yuzden serializer ile anlamlandiriyoruz.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        # fields='__all__'
        # sadece olan fieldi de yazablrz
        # fields=['name']
        # 2.bir cagirma yontemi ise exclude
        exclude=[]

class PostSerializer(serializers.ModelSerializer):
# PostBlog da category_id seklinde yazsin diye;StringRelatedField(str demek.model de yazmistik) i belirtecegiz ama integerField i de eklersek id olarak gelir
    category=serializers.StringRelatedField()
    category_id=serializers.IntegerField()

    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()
    class Meta:
        model=Post
        exclude=[]
        