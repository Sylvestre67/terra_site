import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from main.models import Name, Gender, State, NameInState

module_dir = os.path.dirname(__file__)  # get current directory

class Command(BaseCommand):
    """
    A custom command to import the names stored in the .txt
    files placed on the dataset subdirectory.
    """
    help = 'import names to DB'

    def get_gender(self, row):
        """
        Try to retrieve the Gender based on the information given the processed row.
        If Gender not found, creates it.
        :param row: list
        :return: Gender
        """
        gender = row[1]
        try:
            gender = Gender.objects.get(type=gender)
        except ObjectDoesNotExist:
            try:
                gender = Gender.objects.create(type=gender)
            except:
                pass

        return gender

    def get_state(self, row):
        """
        Try to retrieve the State based on the information given the processed row.
        If State not found, creates it.
        :param row: list
        :return: State
        """
        state = row[0]
        try:
            state = State.objects.get(state=state)
        except ObjectDoesNotExist:
            try:
                state = State.objects.create(state=state)
            except:
                pass

        return state

    def get_name(self, row, gender, state):
        """
        Retrieve a Name based on the row information. If not found, creates a new one.
        :param row: list
        :param gender: Gender
        :return: Name
        """
        name_string = row[3]
        name_string.lower()
        try:
            name = Name.objects.get(name=name_string, gender=gender)
        except ObjectDoesNotExist:
            name = Name.objects.create(
                name=name_string,
                gender=gender
            )

        return name

    def get_name_in_state(self, name,  state, row):
        """
        Retrieve a NameInState based on the row information. If not found, creates a new one.
        :param name: Name
        :param state: State
        :param row: list
        :return: NameInState
        """
        count = row[4]
        try:
            name_in_state = NameInState.objects.get(name=name, state=state, count=count)
        except ObjectDoesNotExist:
            name_in_state = NameInState.objects.create(
                name=name,
                state=state,
                count=count
            )

        return name_in_state


    def handle(self, *args, **options):
        """
        Processed the list of files found in the dataset subdirectory.
        For each file, for each row creates the corresponding objects
        :param args: None
        :param options: None
        :return: None
        """
        initial_names_count = Name.objects.all().count()
        data_directory = os.listdir(os.path.join(module_dir, 'dataset'))

        for filename in data_directory:

            with open(os.path.join(module_dir, 'dataset', filename), 'rt') as data:
                reader = csv.reader(data)

                for row in reader:
                    if len(row) > 0:
                        gender = self.get_gender(row=row)
                        state = self.get_state(row=row)
                        name = self.get_name(row=row, gender=gender, state=state)
                        name_in_state = self.get_name_in_state(name=name, state=state, row=row)
                        print('processed {}'.format(row[3]))
                    else:
                        print('empty row')

        print('Added {} new names'.format((Name.objects.all().count() - initial_names_count)))
        print('Bye Bye')
