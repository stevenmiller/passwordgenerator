from setuptools import setup

setup(
    name='cli-password-generator',
    version='1.0',
    py_modules=['password_generator'],
    install_requires=[
        'secrets',
    ],
    entry_points={
        'console_scripts': [
            'generate-password=password_generator:main',
        ],
    },
)
