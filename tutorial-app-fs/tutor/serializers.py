from rest_framework import serializers
from .models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model=Tutorial
        fields="__all__"

    def validate(self,data):
        if data["title"]==data["description"]:
            raise serializers.ValidationError({"message":"Title and description must not be same!"})
        return data



# class TutorialSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
    
#     def create(self, validated_data):
#         return Tutorial.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.save()
#         return instance
#     def validate(self,data):#?object level validation yapmak için override ediyoruz  
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description must not be same')
#         return data  
# 
# 
#   # create işleminde mesaj dönmek için override
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({"data":serializer.data,"message":"Successfully created!"}, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()