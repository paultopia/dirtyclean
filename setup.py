from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dirtyclean',
      version='0.1',
      description='get rid of unicode punctuation and other garbage from strings',
      long_description=readme(),
      url='https://github.com/paultopia/dirtyclean',
      classifiers=[
          'Development Status :: 3 - Alpha',
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3 :: Only"
      ],
      keywords="textmining, nlp, datacleaning",
      author='Paul Gowder',
      author_email='paul.gowder@gmail.com',
      license='MIT',
      packages=['dirtyclean'],
      python_requires='>=3',
      zip_safe=False)
