
from functools import partial
from importlib.resources import Resource
import io
from lib2to3.pygram import python_grammar_no_print_statement
from venv import create
from certifi import contents
from django import views
from django.shortcuts import render
from django.urls import clear_script_prefix
from requests import Response, delete, request
from first_rest.models import College, Student
from first_rest.Serializers import CollegeSerializer, StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


def get_single_data(request, pk):
    stud = Student.objects.get(id=pk)   # complex data
    python_dic = StudentSerializer(stud)   # complex data converted in to netive python
    json_data = JSONRenderer().render(python_dic.data)   # python to json/ jisko serialise krte uska data send krte mahnun python_dic.data
    return HttpResponse(json_data, content_type='application/json')


def get_all_stud(request):
    stud = Student.objects.all() # complex data
    python_dic = StudentSerializer(stud, many=True)  # complex to netive python
    json_data = JSONRenderer().render(python_dic.data)  # json data 
    return HttpResponse(json_data, content_type = 'application/json')

"""
import io
@csrf_exempt

def create_data(request):
    if request.method == "POST":
        byte_data = request.body
        steam_data = io.BytesIO(byte_data)
        python_dic= JSONParser().parse(steam_data)
        ser = StudentSerializer(data=python_dic)
        if ser.is_valid():
            ser.save()
            msg = {"msg":"data create sucessfully...!"}
            res = JSONRenderer().render(msg)
            return HttpResponse(res, content_type = 'application/json')
        else:
            msg = {"error":" only post method allowd...!"}
            res = JSONRenderer().render(msg)
            return HttpResponse(res, content_type = 'application/json')
-----------------------------------------------------------------------------------------------
from rest_framework.response import Response
@csrf_exempt
@api_view(["GET","POST","PUT","DELETE"])
def single_method_for_all_data(request):
    if request.method =="GET":
        data = request.body
        byte_data = io.BytesIO(data)
        python_dic = JSONParser().parse(byte_data)
        sid = python_dic.get("id")

        if sid:
            try:

                data = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error":"this data does not exits"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type= "application/json")
            ser = StudentSerializer(data)
            # res = JSONRenderer().render(ser.data)
            # return HttpResponse(res, content_type = "application/json")
            # if i m commenting this two line below single line wil give the out put same as above
            return JsonResponse(ser.data)

        else:
            data = Student.objects.all()
            ser = StudentSerializer(data, many = True)
            # res = JSONRenderer().render(ser.data)
            # return HttpResponse(res, content_type = "application/json")
            # same for all data if i m commenting this two line below single line wil give the out put same as above
            # all data hai isliye safe = false
            return  JsonResponse(ser.data, safe= False)

    elif request.method =="POST":
        data1 = request.data       # aisa lisliye liya upar get me (50,52) line ka short cut h 
        print(data1)
        ser= StudentSerializer(data=data1)

        

        print(ser)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            return JsonResponse(ser.errors,status = 400)

    elif request.method == "PUT":
        data2 = request.body
        byte_data = io.BytesIO(data2)
        python_dic = JSONParser().parse(byte_data)
        sid = python_dic.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            ser = StudentSerializer(instance=stud, data=python_dic, partial = True) # user can sedn partial data means name n id send kychi asel tr
            if ser.is_valid():
                ser.save()
            return JsonResponse(ser.data)
        else:
            return JsonResponse({"error": "invalid data"})


    elif request.method == "DELETE":
        data = request.body
        byte_data = io.BytesIO(data)
        python_dic = JSONParser().parse(byte_data)
        sid =  python_dic.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            stud.delete()
            return JsonResponse({"msg":"all data deleted sucessfully"})

    else:
        msg = {"this method is not valid...!"}
        res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type ="application/json")
"""
# --------------------------------------------------------------------
"""
# above apn functionbase baghitla ata clss base baghu, ani views madhun.
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name = 'dispatch')
class StudenApi(View):
    def get(self,request,*args,**kwargs):
        data = request.body
        stream_data = io.BytesIO(data)
        python_dic = JSONParser().parse(stream_data)
        sid = python_dic.get("id")

        if sid:
            try:

                data = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error":"this data does not exits"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type= "application/json")
            ser = StudentSerializer(data)
            return JsonResponse(ser.data)
        else:
            data = Student.objects.all()
            ser = StudentSerializer(data, many = True)
            # res = JSONRenderer().render(ser.data)
            # return HttpResponse(res, content_type = "application/json")
            # same for all data if i m commenting this two line below single line wil give the out put same as above
            # all data hai isliye safe = false
            return  JsonResponse(ser.data, safe= False)

    def post(self, request, *args, **kwards):
        data1 = request.body
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            return JsonResponse(ser.errors,status = 400)



    def put(self, request, *args, **kwards):
        data2 = request.body
        byte_data = io.BytesIO(data2)
        python_dic = JSONParser().parse(byte_data)
        sid = python_dic.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            ser = StudentSerializer(instance=stud, data=python_dic, partial = True) # user can sedn partial data means name n id send kychi asel tr
            if ser.is_valid():
                ser.save()
            return JsonResponse(ser.data)
        else:
            return JsonResponse({"error": "invalid data"})

    def delete(self, request, *args, **kwards):
        data = request.body
        byte_data = io.BytesIO(data)
        python_dic = JSONParser().parse(byte_data)
        sid =  python_dic.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            stud.delete()
            return JsonResponse({"msg":"all data deleted sucessfully"})
"""

# ------------------------------------------------------------------------------------------------------------
""" 
# Api_views

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def student_api_view(request):
    if request.method == "GET":
        sid = request.data.get("id")
        
        if sid:
            stud = Student.objects.get(id= sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        else:
            stud = Student.objects.all()
            ser = StudentSerializer(stud, many=True)
            # print(ser)
            return Response(ser.data)


    elif request.method == "POST":
        data1 = request.data
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data created sucessfully"})
        else:
            return Response(ser.errors)


    elif request.method == "PUT":
        data= request.data
        sid = data.get("id")
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return Response({"msg":"Data updated sucessfully"})
        else:
            return Response({"error":"Invalid data"})


    elif request.method == "DELETE":
        data = request.data
        sid = data.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            stud.delete()
            return Response({"msg":"Data Deleted sucessfully"})

"""

######################################################################################

# Now we are programing by APIView
# APIView is the subclass of views



from rest_framework.views import APIView

class StudentapiNew(APIView):
    def get(self, request, pk= None, formate = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)

        stud = Student.objects.all()
        ser = StudentSerializer(stud, many= True)
        return Response (ser.data)


    def post(self, request, pk= None, formate = None):
        data = request.data
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"data Created sucessfully..!","data": request.data})
        return Response(ser.errors)

    def put(self, request, pk= None, formate = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id = sid)
            ser = StudentSerializer(instance=stud,data= request.data)
            if ser.is_valid():
                ser.data()
                return Response({"msg":"data Updated sucessfully..!", "data": request.data})
            return Response(ser.errors)

    def patch(self, request, pk= None, formate = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instance=stud, data=request.data, partial=True)
            if ser.is_valid():
                ser.data()
                return Response({"msg":"data Updated sucessfully..!", "data": request.data})
            return Response(ser.errors)



    def delete(self, request, pk= None, formate = None):
       
        sid = pk
        if sid:
            stud = Student.objects.all(id = sid, data = request.data)
            stud.delete()
            return Response({"msg":"Data Deleted sucessfully"})

##########################################################

# generic api is subclass of api_view
# genericapi modelmixing
# already defines comman behaviers in mixing

# queryset = Student.objects.all()
# ser = StudentSerializer()

# mixings are
# listmodelmixing == for all data
# retrivemodelmixing = for id
# createmodelmixing 
# updatemodelmixing
# destroymodelmixing

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView


class StudList(GenericAPIView, ListModelMixin):   # ctrl  press kr k genericapi se queyser
    queryset = Student.objects.all()         # GenericAPIView
    serializer_class = StudentSerializer     # GenericAPIView

    def get(self, request, *args, **kwargs):        #ListModelMixin
        return self.list(self, request, *args, **kwargs)


class StudCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()         # GenericAPIView
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)




# classes which required id 
class StudRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()         # GenericAPIView
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

class StudUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()         
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()         
    serializer_class = StudentSerializer   

    def delete(self , request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


# combinemethod

class StudentListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()         
    serializer_class = StudentSerializer  

    def get(self, request, *args,**kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetriveUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args,**kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

####################################################################################

# concrite generic_api_view :- comination of mixing and generic api

from rest_framework.generics import ListAPIView , CreateAPIView ,RetrieveAPIView, UpdateAPIView , DestroyAPIView


class StudList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


###########################################################################################

# viewsets
# repeted lgic can combine one base code
# url router = it generate automaticaly n need togenerate explicity
# no handler method use in view set like get post put

from rest_framework.viewsets import ViewSet

class StudentViewSet(ViewSet):
    def list(self, request):
        data = Student.objects.all()
        ser = StudentSerializer(data = data, many = True)
        return Response(ser.data)

    def create(self, request):
        ser = StudentSerializer(data = request.data)
        if ser.is_valid():
            ser.data()
            return Response(ser.data)
        return Response(ser.data)


    def retrive(self, request, pk = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        

    def update(Self, request, pk = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id = sid)
            ser = StudentSerializer(instance= stud , data = request.data)
            if ser.is_valid():
                ser.data()
                return Response(ser.data)
            return Response(ser.errors)

    def partial_update(self, request, pk = None):
        sid = pk
        if sid:
            stud = Student.objects.get(id = sid)
            ser = StudentSerializer(instance= stud , data = request.data, partial= True)
            if ser.is_valid():
                ser.data()
                return Response(ser.data)
            return Response(ser.errors)

        

    def destroy(self, request, pk= None):
        sid = pk
        if sid:
            stud = Student.objects.all(id = sid, data = request.data)
            stud.delete()
            return Response({"msg": "Data Deleted sucessfully....!"})
        

#############################################################################
# session madhe crediantioal pass krte hai but it acess from session auth table

# Authontication : In credintial through you can login user called as authontication
# Authorization : we can do any operation  when you got permission like changing setting n all 

# data show -- user which is authonticate
# creator - object level
# read data - in case of un authonticated

# Authonticathion:
# credintioal -- login , password, ---token
# drf provied different type of authontication
# Basic
# session
# token
# Remotuser
#custom

# Basic
#  we can pass credintial in Basic , we can use development in basic , but not use for production purpose
# if user authnticated then provied data otherwise give error 401 - unauthorized error in case of unauthonticated

# permmision
   # permission classes
   # Allow any
   # IsAuthontication
   # IsAdminuser
   # IsAuthonticatedor Readonly
   # Djangomodelpermission
   #djangomodelpermissionorAnnonReadonly
   #djangoObjectpermission
   #CustomePermission
   # 
   # 
   # Token-
   #     first time username
   # token is generated respective to user
   # multiple ways to generate token:
   # admin User interface (admin uI)
   # python manage.py drf_create_token_username
   # api endpoint- function - need to pass username n password
   # using signals ---
   # postman
   # headers madhe pass karaych

   # how to pass token ? ans with the help of postman-- heders then  pass  key Authorization :token 08a436439f7450edc3957168f3b69d36ae43b305

   # how to generate tokrn by using admin UI
   # by using python manage.py --- manage.py drf_create_token Subadmin (user) hi command use karun
   # one user having one token

# using signals
#   Django signal -- user created -- authomatically token generated for that specific user


   ###############################################################

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

# allowany - get all permission irrespective if user authontication
# Isauthonticate - permits to only authorised user, no matter which user ur using---in point of is--
# Isadminuser - user which has is-staff enabled, only that user has all acess

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all().filter(is_deleted= 0)
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]  # always in list
    # permission_classes = [AllowAny]    # by default permission allowany 
    # permission_classes= [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'name'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=0)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def destroy(self, request, *args, **kargs):   # override method from mixing Destromixing
        instance = self.get_object()
        instance.is_deleted = 1
        instance.save()
        return Response(status.HTTP_204_NO_CONTENT)
  
    @action(methods=['get'], detail=False, url_path='get-deleted-data', url_name='get-deleted-data')
    def get_deleted_record(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(is_deleted=1)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CollegeModelViewSet(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
 
 ##########################################################
 #jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)    # tuple ormate

    def get(self, request):
        content = {'messege': 'Hello word'}
        return Response(content)
###########################################################################

# Filterning
class StudentListF(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # filter_backends  =
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(created_by = user)