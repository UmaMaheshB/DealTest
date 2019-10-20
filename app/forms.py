from django import forms
from .models import Deal
from datetimepicker.widgets import DateTimePicker
from django.contrib.admin import widgets
class DealForm(forms.ModelForm):

    class Meta:
        model = Deal
        fields = '__all__'
        start_date_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
        end_date_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    # def __init__(self,*args,**kwargs):
    #     super(DealForm, self).__init__(*args, **kwargs)
    #     self.fields['start_date_time'].widget = widgets.AdminSplitDateTime()
    #     # self.fields['start_date_time'].form_class = forms.SplitDateTimeField()
    #     self.fields['end_date_time'].widget = widgets.AdminSplitDateTime()
        # self.fields['end_date_time'].form_class = forms.SplitDateTimeField()