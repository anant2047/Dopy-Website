from django import forms
from .models import *
# from .models import SignUp


class UploadFileForm(forms.ModelForm):
	# event_name=models.CharField(max_length=120, blank=False, null=False)
	#    image = forms.FileField(label='Select a profile Image')#For HTML
 		model = UploadFile
 		fields = ['event_name','upload_file']




class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = SignUp
		widgets = {'password': forms.PasswordInput(),}
		fields = ['fullname', 'email','password']

	def clean_email(self):
		print("working!")
		email = self.cleaned_data.get('email')
		base_email, provider = email.split("@")
		domain, extension = provider.split(".")
		# if not domain == "gmail":
		# 	raise forms.ValidationError("Please enter a valid gmail email")
		if not extension == "edu":
			raise forms.ValidationError("Please enter a valid edu email")
		return email
		