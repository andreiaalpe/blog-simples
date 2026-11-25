
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'name', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'name', 'email',
                    'is_staff', 'is_active', 'is_deleted',)
    list_filter = ('is_staff', 'is_active', 'is_deleted',)
    search_fields = ('username', 'name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {
         'fields': ('name', 'email', 'birth_date', 'image', 'metadata')}),
        ('Permissões', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions',)}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Exclusão', {'fields': ('is_deleted',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': (
            'username', 'name', 'email', 'password1', 'password2'), }),
    )

    def get_queryset(self, request):
        # return User.all_objects.all() # apagados aparecem para o admin
        return User.objects.all()   # apagados não aparecem para o admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'created_at', 'is_active', 'is_deleted',)
    list_filter = ('is_active', 'is_deleted', 'created_at',)
    search_fields = ('title', 'summary', 'textbody', 'user__name',)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        # return Post.all_objects.all() # apagados aparecem para o admin
        return Post.objects.all()       # apagados não aparecem para o admin