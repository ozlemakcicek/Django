from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

# emaili tek bir defa kullanmalik, unic, ve required yaptik.normalde login icin django kendisi email i sart kosmamis 
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(write_only=True,required=True)
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model= User
        fields=(
        'id',
        'username',
        'first_name',
        'last_name',
        'password',
        'password2',
        'email'
        )

# simdi bu iki passwordu karsilastiralim
    def validate(self,data):
       
        if data['password']!=data['password2']:
            raise serializers.ValidationError({"password":"didn't match"}) # kendin mesaj yazablirsin
        return data

            
# simdi passwordlari cikartalim datanin icinden ve useri olusturup,set_password ile tekrar hashliyor(sifreliyor)
    def create(self,validated_data):
        validated_data.pop('password2')
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user