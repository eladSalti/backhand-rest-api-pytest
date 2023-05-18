from setuptools import setup, find_packages

# find packages will give you the option to add python packages automatically to the setup.py file
# How it works? is going to find packages in any folder that have __init__.py file
setup(name='elad_testing', version='1.0', description="Practice API testing", author="Elad Salti",
      author_email='elad.salti7@gmail.com', packages=find_packages())

