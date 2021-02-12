#Form API
from django import forms #para api forms
from django.core import validators #validadores

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "titulo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
            'placeholder': 'ingresa el titulos',
            'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, "El titulo es demasiado corto"),
            validators.RegexValidator('^[A-Za-z0-9ñáéíóúüÁÉÍÓÚÜ ]*$', 'EL titulo esta mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,

        validators=[
            validators.MaxLengthValidator(20, 'Te has pasado de la cantidad maxima de caracteres')
        ]
    )
    content.widget.attrs.update({ #otra forma tambien puede hacerse como arriba
        'placeholder': 'ingresa el titulos',
        'class': 'titulo_form_article'
    })

    public_options =[
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices =  public_options
    )