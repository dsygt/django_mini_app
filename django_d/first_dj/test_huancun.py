import os
import django
from timeit import Timer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_dj.settings")
django.setup()


from django.core.cache import cache

# cache.set('可乐','可口可乐')
print(cache.get('可乐'))

# if data is in the cache:
# 	return data
# else:
# 	generate the data
# 	save the data in the chahe(set timeout)
# 	return the generated data