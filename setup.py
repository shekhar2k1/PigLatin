from setuptools import setup


setup(
    name='piglatin',
    description='PigLatin Translation app',
    url='https://github.com/shekhar2k1/PigLatin',
    version='0.0.1',
    author_email='abc@gmail.com',
    packages=['piglatin', ],
    install_requires=[
        'Flask',
        'Flask_Cache',
        'Flask-Script',
    ],
)
