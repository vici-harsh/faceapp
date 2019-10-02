from django.test import TestCase

# Create your tests here.
import os
dir = os.getcwd()
print(dir)

print(os.getcwd().replace('Demo','')+'Media')
print('hello')
