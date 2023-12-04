from datetime import date

from rest_framework import serializers
from src.apps.movie.models.actor import Actor


class ActorSerializer(serializers.ModelSerializer):
    #    age = serializers.IntegerField(source='get_age', read_only=True)
    age = serializers.SerializerMethodField(read_only=True)
    cinema_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

    @staticmethod
    def get_age(obj: Actor):
        today = date.today()
        age = today.year - obj.date_of_birth.year - (
                (today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))
        return age

    @staticmethod
    def get_cinema_count(obj: Actor):
        return obj.movies.all().count()
