from django import forms


class QuizForm(forms.Form):
    def __init__(self, data, questions, *args, **kwargs):
        self.questions = questions
        for question in questions:
            field_name = "question_%d" % question.pk
            choices = []
            for answer in question.answer_set().all():
                choices.append((answer.pk, answer.answer,))
            # May need to pass some initial data, etc:
            field = forms.ChoiceField(label=question.question, required=True,
                                      choices=choices, widget=forms.RadioSelect)
        return super(QuizForm, self).__init__(data, *args, **kwargs)
