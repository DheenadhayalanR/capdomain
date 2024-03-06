from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userLoginSerializer
from .models import UserLogin

@api_view(['POST','GET','DELETE'])
def userLogin(request):
   if request.method == 'POST':
        data=request.data
        serializer=userLoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(data)

   if request.method == 'GET':
       data=UserLogin.objects.all()
       serializer = userLoginSerializer(data, many=True)
       return Response(serializer.data)
   
   if request.method == 'DELETE':
       user_name=request.data.get('user_name')
       data=UserLogin.objects.filter(user_name=user_name)
       data.delete()
       return Response(data)
