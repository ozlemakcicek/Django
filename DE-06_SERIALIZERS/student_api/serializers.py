"""Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.  """

from rest_framework import serializers
from .models import Student,Path


#eski tarz kullanim
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     age = serializers.IntegerField()


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

# yeni tarz models serializer kullanimi.importu yukarida


class StudentSerializer(serializers.ModelSerializer):

    born_year = serializers.SerializerMethodField() # read only
       #! read_only, post isleminde devreye girmeyip get islemi esnasinda dahil oluyor. "MethodField" nin bir ozelligi bu,
    #! ve tablomuzda bu field gpzukmeyecek.
    path=serializers.StringRelatedField() # read only o.i alttaki satiri ekledik
    path_id=serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = "__all__"
        # field leri spesifik yapablrsn
        # fields=("first_name","age")
        #exclude=["number"]

#methodField icin get ile baslayacak kesinlikle ve field in ismi

            #! methodField buraya atanacak degeri icin fonk. get ile baslamasi gerekiyor, ve ustteki variable nin ismini almasi gerekiyor
    def get_born_year(self,obj):
        import datetime
        current_time=datetime.datetime.now()
        return current_time.year-obj.age

class PathSerializer(serializers.ModelSerializer):
    # ayni pathe sahip kisileri beraber gosterir postman de
        #* "StringRelatedField" foreign key oldugunda ilgili id nosunu verdigi icin, bu kod ile ilgili string donuyor.
    # students=serializers.StringRelatedField(many=True, read_only=True)
    # en yukaridaki StudentSerializer i referans alarak yapiyoruz.boylece butun bilgileri getirrir.
    students=StudentSerializer(many=True, read_only=True)
     #! her iki durumda da read_only ekledik, cunku path eklerken ogrenci olusturmak zorunda kalmayalim diye
    class Meta:
        model = Path
        fields = "__all__"



    


