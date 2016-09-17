from django import forms

race_choices = [('asian','Asian'), ('white', 'White'), ('black', 'Black'), ('indian', 'Indian'),
				('native american', 'Native American')]
sexuality_choices = [('straight', 'Straight'), ('gay', 'Gay'), ('bi', 'Bi')]
gender_choices = [('male', 'Male'), ('female', 'Female'), ('trans', 'Transgender')]
roast_choices = [('light', 'Light'), ('medium', 'Medium'), ('dark', 'Dark')]
topic_choices = [('1', 'Politics'), ('2', 'Environment'), ('3', 'Kai'), ('4', 'Religion')]

class PersonForm (forms.Form):
	your_name = forms.CharField(label='Your Name', max_length=100)
	your_age = forms.IntegerField(label='Age')
	your_race = forms.ChoiceField(label='Race', widget=forms.RadioSelect, choices=race_choices,)
	your_gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=gender_choices,)
	your_sexuality = forms.CharField(label='Sexuality')
	your_roast = forms.ChoiceField(label='Your Preferred Roast', widget=forms.RadioSelect, choices=roast_choices)
	your_topic = forms.ChoiceField(label='Topic you Want to Talk About', widget=forms.RadioSelect, choices=topic_choices)

#class Welcome(forms.Form):
#	welcome = 

#f = UserData()

#data = {'Name', 'Age', 'Race', 'Gender', "Sexuality", "Roast"}

#f = UserData(data)

