from django import forms
from django.utils import timezone
from crispy_forms.layout import Submit, HTML
from crispy_forms.helper import FormHelper, Layout
from .models import JournalEntry

class JournalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JournalForm, self).__init__(*args, **kwargs)
        self.fields['actual_date'].initial = timezone.now
        self.helper = FormHelper()
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-4'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            'actual_date',
            'image',
            HTML("""{% if form.image.value %}<img class="image-responsive"
            src="{{ form.image.url }}">{% endif %}""", ),
            'content',
            HTML("""<h2>Word of the Day</h2>"""),
            'word_of_the_day',
            'word_of_the_day_def',
            HTML("""<h2>Quote of the Day</h2>"""),
            'quote_author',
            'quote_content',
            HTML("""<h2>Posture Changes Noted</h2>"""),
            'posture_changes',
        )

    actual_date = forms.DateField(initial=timezone.now, label="Date of Entry", required=True)
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea)
    word_of_the_day = forms.CharField(required=False, label="Word")
    word_of_the_day_def = forms.CharField(required=False, label="Definition")
    posture_changes = forms.IntegerField(required=False)
    quote_author = forms.CharField(required=False)
    quote_content = forms.CharField(required=False)

    class Meta:
        model = JournalEntry
        fields = ['actual_date', 'image', 'content', 'quote_author', 'quote_content',
                  'word_of_the_day', 'word_of_the_day_def', 'posture_changes']
