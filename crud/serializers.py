from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

# creating data Or inserting data
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
# implementing updating data
# in update we have three parameter 1) self 2) instance 3) validated_data
    def update(self, instance, validated_data):
        # check what is in instance parameter
        # print(instance.name) give me old data
        print(instance.name)

        instance.name = validated_data.get('name',instance.name)
        # here print(instance.name) updated 
        print(instance.name)

        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
