from setuptools import setup, find_packages

setup(name='zimuku',
      version='0.1',
      description='fuck the zimuku',
      url='https://github.com/linheimx/ZimuDog_Server',
      author='linheimx',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4','requests'
      ],
      zip_safe=False)
