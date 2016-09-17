from django import forms

race_choices = [('asian','Asian'), ('white', 'White'), ('black', 'Black')]
gender_choices = [('straight', 'Straight'), ('gay', 'Gay'), ('bi', 'Bi')]


class PersonForm (forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	your_age = forms.IntegerField(label='Your age')
	your_race = forms.ChoiceField(label='Your race', widget=forms.Select, choices=race_choices,)
	your_genger = forms.ChoiceField(label='Gender', widget=forms.Select, choices=gender_choices,)




#f = UserData()

#data = {'Name', 'Age', 'Race', 'Gender', "Sexuality", "Roast"}

#f = UserData(data)

