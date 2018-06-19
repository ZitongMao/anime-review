from django import forms
from kanban.models import Title


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'japanese_title', 'year','status', 'rating', 'review']
    def clean_title(self):
        title = self.cleaned_data.get('title').encode('utf-8')
        if len(title) > 120:
            raise forms.ValidationError("Length of title should be less than 120.")
        return title

    def clean_japanese(self):
        title = self.cleaned_data.get('japanese_title').encode('utf-8')
        if len(title) > 120:
            raise forms.ValidationError("Length of title should be less than 120.")
        return japanese_title

    def clean_year(self):
        year = self.cleaned_data.get('year')
        return year

    def clean_status(self):
            status = self.cleaned_data.get('status')
            return status

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        return rating
    def clean_review(self):
        review = self.cleaned_data.get('review').encode('utf-8')
        return review
