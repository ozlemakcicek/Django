from .serializers import TutorialSerializer
from .models import Tutorial
from rest_framework.viewsets import ModelViewSet

class TutorialMVS(ModelViewSet):
    queryset=Tutorial.objects.all()
    serializer_class=TutorialSerializer






#! fbv
# @api_view(['GET','POST'])
# def tutorial_list(request):
#     if request.method== 'GET':
#         tutorials = Tutorial.objects.all()
#         serializer = TutorialSerializer(tutorials,many=True)#bu şekilde bıraktığımızda bize hata veriyor çünkü bu şekilde queryset vermiş olduk.biizm burada serializera açık bir şekilde dememiz gerekiyorki biz sana birden fazla instance gönderiyoruz aşağıda olduğu giibi
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TutorialSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def tutorial_detail(request,id):
#     try:
#         tutorial = Tutorial.objects.get(id=id)
#     except Tutorial.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':404,
#                     'message':'tutorial not found'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
#     if request.method=='GET':
#          serializer = TutorialSerializer(tutorial)#?tek bir query olduğu için many=true yapmamıza gerek yok
#          return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer = TutorialSerializer(tutorial,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         tutorial.delete()
#         return Response({
#                 'success':{
#                     'code':200,
#                     'message':'tutorial is deleted'
#                 }
#             },status=status.HTTP_204_NO_CONTENT) 
