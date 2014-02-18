from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pybucket',
      version='0.1',
      description='Python implementation of IRC bot Bucket',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPL v3',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='irc bucket willie',
      url='https://github.com/Preston4tw/pybucket',
      license='GPL v3',
      packages=['pybucket'],
      include_package_data=True,
      zip_safe=False)
