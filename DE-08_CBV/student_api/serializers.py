"""Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.  """

from rest_framework import serializers
from .models import Student, Path

""" class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    number = serializers.IntegerField(required=False)
    age = serializers.IntegerField()


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance """
    
 #! ustteki ilkel bir kullanim tek tek elle Serializer diyerek yaziyorsun.onun yerine ModelSerializer kullanarak ordan cekiyoruz   
class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField()  # read_only  bunu frontend gorur
    path_id = serializers.IntegerField()    # bunu da backend gorsun diye yazdik.sart degil
    

    # Meta tamirci gibi.degisiklikler yapabilmek icin kullanilir
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ("first_name", "age" )
        # exclude = ['number']
        
    
    def get_born_year(self, obj):  # method olustururken get ile baslamali
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age


class PathSerializer(serializers.ModelSerializer):
   # many=True bir path e ait birden cok ogrenci olacagi icin bunu eklemeliyiz 
    students = StudentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]