import os

os.environ['TEST'] = 'test environ'

# delete env
# del os.environ['TEST']

test = os.getenv('TEST')

print(test)
