from setuptools import setup

with open('hieu_distributions/README.md', 'r') as f:
    long_description = f.read()

setup(name='hieu_distributions',
      version='0.3',
      description='Gaussian distributions',
      packages=['hieu_distributions'],
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown')

# zip_safe=False: the package cannot be run directly from a zip file