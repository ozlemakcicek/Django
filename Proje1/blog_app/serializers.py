
#* Serializer python kodlarini json formatina cevirir.Frontend ile beraber calisabilmesi icin bu gerekli.
from rest_framework import serializers
from .models import Category
from .models import Post


class CategorySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Category
        fields = "__all__" # bu su demek ["name"]



class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model= Post
        fields="__all__"
