from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        #print(options.get('num'))
        number = options.get('num')[0]   # 注意：此处options.get('num')是一个列表
        if number is None:
            number = 5
        password = make_password('@@shulrs')
        for i in range(int(number)):
            data = {
                'username': i,
                #'mobile': faker.phone_number(),
                'password': password,
                'is_superuser': False,
            }
            try:
                User.objects.create(
                    **data
                )
                User.save()
            except:
                CommandError('创建失败！')
            self.stdout.write(self.style.SUCCESS('Successfully create user "%s"' % i))

