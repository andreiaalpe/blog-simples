# blog\forms.py

from django import forms
from .models import User
from django.core.validators import FileExtensionValidator


class ProfileForm(forms.ModelForm):

    image = forms.ImageField(
        label='Foto de perfil',
        required=False,
        # Lista de formatos de imagem de perfil válidos
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.jpg,.jpeg,.png,.webp'})
    )

    # Testa o tamanho máximo em bytes da imagem de perfil
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 2 * 1024 * 1024:
            raise forms.ValidationError('A imagem não pode ultrapassar 2 MB.')
        return image

    class Meta:
        model = User
        fields = ['name', 'email', 'birth_date', 'image', 'metadata',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'metadata': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
