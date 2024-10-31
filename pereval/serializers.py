from pereval.models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from pereval.views import *



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'spring', 'summer', 'autumn',)


class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('email', 'fam', 'name', 'otc', 'phone',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title',)


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    status = serializers.CharField(read_only=True)
    level = LevelSerializer(allow_null=True)
    user = PassUserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'user',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'coords',
            'level',
            'images',
            'add_time',
            'status',
        )

    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user
            user_data = data.get('user')
            user_fields_check = [
                user_instance.email == user_data.get('email'),
                user_instance.fam == user_data.get('fam'),
                user_instance.otc == user_data.get('otc'),
                user_instance.phone == user_data.get('phone'),
                user_instance.name == user_data.get('name')
            ]
            if not all(user_fields_check):
                raise serializers.ValidationError({'Изменения отклонены': 'К сожалению эти поля нельзя редактировать'})
        return data