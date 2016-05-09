from django import forms
# Form Frame -->for HTML define a Form class
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False,label='Your E-mail Address')	# be selectable
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError('Not Enough Words.')
		return message