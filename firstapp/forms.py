from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "myfield"}))
    # age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "myfield"}))
    # name = forms.CharField(label='Имя', initial="undefined", help_text="Введите свое имя", max_length=20, min_length=3)
    # age = forms.IntegerField(initial=18, help_text="Введите свой возраст", required=False, max_value=100, min_value=1)
    # required_css_class = "field"
    # error_css_class = "error"
    # BooleanField = forms.BooleanField()
    # NullBooleanField = forms.NullBooleanField()
    # CharField = forms.CharField()
    # EmailField = forms.EmailField()
    # GenericIPAddressField = forms.GenericIPAddressField()
    # RegexField = forms.RegexField(regex='^&')
    # SlugField = forms.SlugField()
    # URLField = forms.URLField()
    # UUIDField = forms.UUIDField()
    # ComboField = forms.ComboField(fields=[])
    # MultiValueField = forms.MultiValueField(fields=[name, age])
    # FilePathField = forms.FilePathField(path='./')
    # FileField = forms.FileField()
    # ImageField = forms.ImageField()
    # DateField = forms.DateField()
    # TimeField = forms.TimeField()
    # DateTimeField = forms.DateTimeField()
    # DurationField = forms.DurationField()
    # SplitDateTimeField = forms.SplitDateTimeField()
    # IntegerField = forms.IntegerField()
    # DecimalField = forms.DecimalField()
    # FloatField = forms.FloatField()
    # ChoiceField = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.RadioSelect)
    # TypeChoiceField = forms.TypedChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
    # MultipleChoiceField = forms.MultipleChoiceField(choices=((1, "English"), (2, "German"), (3, "French")), widget=forms.CheckboxSelectMultiple)
    # TypedMultipleChoiceField = forms.TypedMultipleChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))

    # field_order = ["age", "name", 'EmailField']
