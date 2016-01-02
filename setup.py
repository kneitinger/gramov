try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Telegram bot that uses Markov chains to learn to \
            speak from a chat.',
    'author': 'Kyle J. Kneitinger',
    'url': 'https://github.com/kneitinger/gramov',
    'author_email': 'kneit@pdx.edu',
    'version': '0.1',
    'install_requires': ['pyTelegramBotAPI','markoff'],
    'scripts': ['bin/gramov'],
    'name': 'gramov',
    'license' : 'BSD',
    'classifiers' : [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Text Processing :: Linguistic'
    ]

}

setup(**config)
