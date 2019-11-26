from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, choices=['sdist', 'upload'])

    def handle(self, *args, **options):
        # print(args)
        # print(options)
        action = options.get('action')
        print(action)
        print('success~')
