from setuptools import setup

setup(name='stockgo',
      version='0.1',
      description='The stock go in the world',
      url='https://github.com/walkacross/stockgo',
      author='alen yu',
      author_email='yujiangallen@126.com',
      license='MIT',
      packages=['stockgo'],
      entry_points = {
              'console_scripts':['stockgo-joke=stockgo.command_line:main'],
              },
      install_requires=[
          'markdown','numpy'
      ],
      zip_safe=False)
