from django.contrib import admin
from .models import Movie, Keyword, MovieKeyword, Rating

# Register your models here.
admin.site.register(Movie)


admin.site.register(Keyword)
admin.site.register(MovieKeyword)
admin.site.register(Rating)