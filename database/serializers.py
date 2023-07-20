# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
# from .models import Member, ProfilePic, Chess, Player

# Create a model serializer
# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = Member
# 		fields = ('id', 'firstname', 'lastname', 'email', 'password', 'about', 'phone', 'joined_date', 'is_active')