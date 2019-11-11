from setuptools import setup, find_packages

setup(name='edgarcli',
      version='0.1',
      description='Cli for interacting with Edgar',
      url='https://github.com/seanxwzhang/edgarcli',
      author='Xiaowen Zhang',
      author_email='seanxwzhang@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'python-edgar~=2.6',
        'pdfkit~=0.6',
        'argparse~=1.4',
      ],
      python_requires='>=3.7',
      entry_points='''
        [console_scripts]
        edgarcli=edgarcli.__main__:__main__
      '''
)