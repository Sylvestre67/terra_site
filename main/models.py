from django.db import models


GENDER = (('F', 'F'), ('M', 'M'))


class Gender(models.Model):
    """
    A model to keep track of gender (Male or Female) of a given name.
    """
    type = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return u'{}'.format(self.type)

class State(models.Model):
    """
    A model to keep track of state in which a given name has been recorded.
    """
    state = models.CharField(max_length=256)

    def __str__(self):
        return u'{}'.format(self.state)


class Name(models.Model):
    """
    A model to store name information.
    """
    name = models.CharField(max_length=256)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return u'{}'.format(self.name)


class NameInState(models.Model):
    """
    A model to keep track of State and Model information.
    A `manual` many_to_many relationship.
    """
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField()
