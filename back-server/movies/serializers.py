from rest_framework import serializers
from .models import Movie, Rating, User, MovieKeyword, Keyword, KarloImg

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

class MovieDetailSerialzer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MovieImgSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('tmdb_id', 'original_title', 'poster_path', 'popularity','ratings',)


class KarloSerializer(serializers.ModelSerializer):
    img_url = serializers.ImageField(use_url=False)
    class Meta:
        model = KarloImg
        fields = '__all__'