import io
from setuptools import find_packages, setup
from bskan_auto import __version__


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='bskan_auto',
      version=__version__,
      description='Image generation and post processing code of bSKAN',
      long_description=long_description(),
      url='https://github.com/materials-theory/bskan_auto',
      author='Giyeok Lee',
      author_email='lgy4230@yonsei.ac.kr',
      license='MIT',
      packages=find_packages(),
      keywords='STM bSKAN DFT vasp ase chen bardeen',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          ],
      install_requires=['ase', 'numpy', 'scipy',
                        'Pillow', 'matplotlib'],
      entry_points = {'console_scripts':['bskan_auto = main:main']}
      )