import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django_asgi_app = get_asgi_application()

from shop.models import *

item1 = Item.objects.create(name='Almurut', price=90)
item2 = Item.objects.create(name='Alma', price=90)
item3 = Item.objects.create(name='Buldurkon', price=90)
item4 = Item.objects.create(name='Itmurun', price=90)
item5 = Item.objects.create(name='TbIT', price=90)
item6 = Item.objects.create(name='Baka-jalbyrak', price=90)
item7 = Item.objects.create(name='At kulak', price=90)
item8 = Item.objects.create(name='Jugoru', price=90)
item9 = Item.objects.create(name='Buudai', price=90)
item10 = Item.objects.create(name='Arpa', price=90)


item1.purchases.create(name='Azat', age=99)
item1.purchases.create(name='Azat', age=99)
item2.purchases.create(name='Vasya', age=99)
item2.purchases.create(name='Vasya', age=99)
item3.purchases.create(name='Ulan', age=99)
item3.purchases.create(name='Ulan', age=99)
item4.purchases.create(name='Tilek', age=99)
item4.purchases.create(name='Tilek', age=99)
item5.purchases.create(name='Radion', age=99)
item5.purchases.create(name='Radion', age=99)
item6.purchases.create(name='Asan', age=99)
item6.purchases.create(name='Asan', age=99)
item7.purchases.create(name='Uson', age=99)
item7.purchases.create(name='Uson', age=99)
item8.purchases.create(name='Azat', age=99)
item8.purchases.create(name='Azat', age=99)
item9.purchases.create(name='Tynchtyk', age=99)
item9.purchases.create(name='Tunchtyk', age=99)
item10.purchases.create(name='Azat', age=99)
item10.purchases.create(name='Azat', age=99)
