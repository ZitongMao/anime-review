from rest_framework import serializers
from kanban.models import Title

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('url','user','title','japanese_title','created_at','rating','review','status','year')
