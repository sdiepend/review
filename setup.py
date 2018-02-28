from setuptools import setup

setup(
    name='reviewer',
    version='0.0.1.dev2',
    description='Easily create and manage gitlab merge requests from the commandline',
    url='https://github.com/sdiepend/review',
    author='Stijn Diependaele',
    author_email='sdiepend@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='gitlab cli tool merge request',
    project_urls={
        'Documentation': 'https://github.com/sdiepend/review/blob/master/README.md'
    },
    py_modules=["review"],
    install_requires=[
        'fire',
        'requests'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['review = review:main']
    },
)
