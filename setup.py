import setuptools


package = dict(
    name             = 'temporarydirectory',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'A temporary directory context manager',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/temporarydirectory',
    packages         = setuptools.find_packages(),
    install_requires = [
    ],
    tests_require    = [
        'pytest',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
