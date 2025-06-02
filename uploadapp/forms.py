from django import forms

class FileUploadForm(forms.Form):
    file_name = forms.CharField(max_length=255)
    public_id = forms.CharField(max_length=255, required=False, initial='dummy')
    file = forms.FileField()