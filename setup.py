from setuptools import setup, find_packages

setup(name='kyma_poc',
      version='0.0.1',
      description='Generative AI POC for Konveyor.io source code modernization',
      url='https://github.com/jwmatthews/kyma_poc',
      author='John Matthews',
      author_email='jwmatthews@gmail.com',
      license='Apache Software License 2.0',
      packages=find_packages(where='src'),
      zip_safe=False)