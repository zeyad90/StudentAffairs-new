from django import forms
from django.forms.widgets import DateInput, TextInput
from django import forms
from .models import ExcelFile
from .models import *
from django import forms
from django.core.validators import RegexValidator

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    idnumber = forms.CharField(required=True,validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')])
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
        'password': forms.PasswordInput(),
    }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).admin.email.lower()
            if dbEmail != formEmail:  # There has been changes
                if CustomUser.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError("The given email is already registered")

        return formEmail
    
    
    def clean_idnumber(self, *args, **kwargs):
        formID = self.cleaned_data['idnumber'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(idnumber=formID).exists():
                raise forms.ValidationError("The given id is already registered")
        else:  # Update
            idnumber = self.Meta.model.objects.get(id=self.instance.pk).admin.idnumber.lower()
            if idnumber != formID:  # There has been changes
                if CustomUser.objects.filter(idnumber=formID).exists():
                    raise forms.ValidationError("The given id is already registered")
        return formID
    


    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',  'password' ,'idnumber']


class StudentForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields +['Semester']

class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
    class Meta(CustomUserForm.Meta):        
        model = Admin
        fields = CustomUserForm.Meta.fields


class StaffForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields + \
            ['Semester' ]
   

from django.forms import ModelForm, TimeInput
from .models import Semester

class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Semester
        fields = ['name']

from django import forms
from django.core.validators import RegexValidator

class SubjectForm(FormSettings):

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Subject
        fields = ['name', 'staff', 'Semester']


class SessionForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Session
        fields = '__all__'
        widgets = {
            'start_year': DateInput(attrs={'type': 'date'}),
            'end_year': DateInput(attrs={'type': 'date'}),
        }


class LeaveReportStudentForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(LeaveReportStudentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = LeaveReportStudent
        fields = ['date', 'message', 'attachment']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'date': 'Date (yyyy-mm-dd)',
            'message': 'Leave message',
            'attachment': 'Attachment (optional)',
        }

class StudentEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields 


class StaffEditForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StaffEditForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields



class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file',)