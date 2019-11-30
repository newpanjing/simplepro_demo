from django.core.management.base import BaseCommand, CommandError
import os
from extensions import conf, utils


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'app', default='',
            type=str,
        )

    def handle(self, *args, **options):
        app = options.get('app')
        if not app:
            raise Exception('manage.py sdist: error: the following arguments are required: app')
        pwd, root = conf.get_plugin_dir()
        p = os.path.join(pwd, app)
        if not os.path.exists(p):
            raise Exception('manage.py sdist: error: Plugin not found:\nPath:{}'.format(p))
        print(p)
        print(utils.check_app('{}.{}'.format(root, app)))
        print('打包app' + app)
