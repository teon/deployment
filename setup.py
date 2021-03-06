from setuptools import setup
from deployment.version import version

readme = []
with open('README.md', 'r') as fh:
    readme = fh.readlines()

setup(
    name='deployment',
    version=version,
    author='TEONITE',
    author_email='kkrzysztofik@teonite.com',
    packages=['deployment', 'deployment.plugins', 'deployment.libs'],
    scripts=['deploy'],
    url='http://teonite.com/',
    description='Deployment, provisioning and database migration tool.',
    long_description='\n'.join(readme),
    license='Proprietary',
    install_requires=[
        "Fabric >= 1.5.1",
        "GitPython >= 0.3.2.RC1",
        "graypy >= 0.2.7",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 2.7"
    ],
    data_files=[('deployment/conf/', ['conf/conf.json.template'])]
)
