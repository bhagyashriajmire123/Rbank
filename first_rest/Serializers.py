from pyexpat import model
from wsgiref.validate import validator
from attr import field
from pytest import mark
from rest_framework import serializers  # pip install rest_framework then use ok
# serializer are always class base
from first_rest.models import Student, College


# validatos se bhi restriction laga sakte

# In API how many types of validation
# 1)field level
# 2)object level validation
# 3) validators

def Special_letter(value):
    if value[0].lower() == "B":
        return value
    raise serializers.ValidationError("Name should be alays start from B")

def len_of_name(value):
    if len(value) >= 3:
        return value
    raise serializers.ValidationError("lengh of name error should be grater than 3")

"""
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators= [Special_letter, len_of_name])
    city = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    marks = serializers.IntegerField()

    def create(self, validated_data):
       stud =  Student.objects.create(**validated_data)
       return stud
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.city = validated_data.get("city", instance.city)
        instance.age = validated_data.get("age", instance.age)
        instance.marks = validated_data.get("marks", instance.marks)
        instance.save()
        return instance

    #  this 2 method is field level validation
    # def validate_age(self, value):
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("age not valid")
        
    # def validate_marks(self, marks):
    #     if marks > 45:
    #         return marks
    #     raise serializers.ValidationError("marks should always greater than 45")


    # object level validation
    def validate(self, data):
        if (data.get("city")== "Nagpur") and (data.get("age") >= 21):
            return data
        raise serializers.ValidationError("city always in pune and age must be greater than 21")
"""


# now we are using model serializers , ya madhe serializer. serializer chi without help gheta method CURD operation karta yeta 
# model serializer , models.py file madhun surve models access kerte manhun to direct shortcut ahe

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        # fields = ["name","city","age","marks"]
        fields = "__all__"   # is me id bhi show karnga , meas 100 fileds hongi to puri show karega
        
        # exclude = ["id", "marks"]  # id marks chod k baki sara data lega
        
        # read_only_fields = ["name"]    # data acess kru shakt write nahi kru shaknar 

        # extra_keywards = ["read_only_fields" == ["name"] , "write_only_fields"== ["age"]]

        # apan varti lavla tasa field validation model serializers madhe lau shakto

    # def validate_age(self, value):
    #         if value >= 20:
    #             return value
    #         raise serializers.ValidationError("age should be above 20")   



class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College

        fields = '__all__'
        

   
