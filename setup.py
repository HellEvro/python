from distutils.core import setup
setup(
  name = 'stampery',
  packages = ['stampery'],
  version = '0.1.1',
  description = 'Stampery API for Python. Notarize all your data using the blockchain',
  author = 'Luis Ivan Cuende',
  author_email = 'luis@stampery.com',
  url = 'https://github.com/stampery/python',
  download_url = 'https://github.com/stampery/python/archive/master.zip',
  keywords = ['blockchain', 'stampery', 'notary', 'notarization'],
  classifiers = [],
  install_requires=[
    "requests",
  ],
)
