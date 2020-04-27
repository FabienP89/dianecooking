from django import forms

from blog.models import Comment, Contact, Newsletter


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text',]
        labels = {'author_name':'',
                  'text':'',}
        widgets = {
            'author_name': forms.TextInput(attrs={'placeholder':'Nom/Pseudo'}),
            'text': forms.Textarea(attrs={'placeholder':'Commentaire'}),
        }

class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = ['name', 'email', 'compagny', 'message']
        labels = {'name':'', 'email':'', 'compagny':'', 'message':''}
    
        widgets = {
                'name': forms.TextInput(attrs={'placeholder':'Prénom / Nom*'}),
                'email': forms.TextInput(attrs={'placeholder':'Email*'}),
                'compagny': forms.TextInput(attrs={'placeholder':'Société / Site internet'}),
                'message': forms.Textarea(attrs={'placeholder':'Votre message*'}),
            }

class NewsletterForm(forms.ModelForm):
    class Meta :
        model = Newsletter
        fields = ['email']
        labels = {'email':''}
        widgets = {'email': forms.TextInput(attrs={'placeholder':'Saisissez votre email ici'})}