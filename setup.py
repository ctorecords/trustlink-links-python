from setuptools import setup, find_packages

setup(
    name = 'trustlink-links-python',
    version = '0.1.0',
    description = 'Links inserter from trustlink.ru.',
    author = 'Dmitry V. Simonov',
    author_email = 'dsimonov@gmail.com',
    keywords = 'seo tool',
    license = 'New BSD License',
    url = 'https://github.com/dsimonov/trustlink-links-python',
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
)
