# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Category, Product
# from account.models import Account

# create a serializer class
class CategorySerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Category
		fields = ('name','id')



class ProductSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Product
		fields = ('title','id','description', 'file')


# class AccountSerializer(serializers.ModelSerializer):

# 	# create a meta class
# 	class Meta:
# 		model = Account
# 		fields = ('name','email','address', 'phone')