from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial="undefined", help_text="Введите свое имя", max_length=20, min_length=5)
    age = forms.IntegerField(initial=18, help_text="Введите свой возраст", required=False, max_value=99, min_value=1)
    BooleanField = forms.BooleanField()
    NullBooleanField = forms.NullBooleanField()
    CharField = forms.CharField()
    EmailField = forms.EmailField()
    GenericIPAddressField = forms.GenericIPAddressField()
    RegexField = forms.RegexField(regex='^&')
    SlugField = forms.SlugField()
    URLField = forms.URLField()
    UUIDField = forms.UUIDField()
    ComboField = forms.ComboField(fields=[])
    MultiValueField = forms.MultiValueField(fields=[name, age])
    FilePathField = forms.FilePathField(path='./')
    FileField = forms.FileField()
    ImageField = forms.ImageField()
    DateField = forms.DateField()
    TimeField = forms.TimeField()
    DateTimeField = forms.DateTimeField()
    DurationField = forms.DurationField()
    SplitDateTimeField = forms.SplitDateTimeField()
    IntegerField = forms.IntegerField()
    DecimalField = forms.DecimalField()
    FloatField = forms.FloatField()
    ChoiceField = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.RadioSelect)
    TypeChoiceField = forms.TypedChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
    MultipleChoiceField = forms.MultipleChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.CheckboxSelectMultiple)
    TypedMultipleChoiceField = forms.TypedMultipleChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))

    field_order = ["age", "name"]
