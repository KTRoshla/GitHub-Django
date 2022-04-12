from rest_framework import serializers
from EmployeeApp.models import MasterCategory,MasterCategoryValues
class MasterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MasterCategory
        fields=('CatID','CatName','Status','Parent','Description')


class MasterCategoryValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=MasterCategoryValues
        fields=('CatValID','Value','Status','SortOrder','CatID','Description','ParentID')