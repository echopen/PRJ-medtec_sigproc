__author__ = 'mehdibenchoufi'
from setuptools import setup, find_packages
setup(
    name='EchoImageProcessing',
    version='0.1',
    description='image_processing',
    classifiers=[
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    install_requires=[
        'scikit-image',
        'numpy',
    ],
    entry_points=dict(
        console_scripts=[
            'scanconverter = EchoImageProcessing.scanconverter:execution',
            'image_metrics = EchoImageProcessing.image_metrics:main',
            'denoise_image = EchoImageProcessing.denoise_image:main',
        ],
))
