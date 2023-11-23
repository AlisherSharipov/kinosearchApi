from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from ..movie.models.movie import Movie, UserMovieRelation
from ..movie.models.actor import Actor


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'date_release', 'get_actor_name', 'description']
    form = MovieAdminForm

    @staticmethod
    def get_actor_name(obj: [Actor]):
        return obj.actor.name


@admin.register(UserMovieRelation)
class UserMovieRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Actor)
