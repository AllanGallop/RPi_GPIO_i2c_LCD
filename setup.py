from setuptools import setup, find_packages

setup(
    name='RPi_GPIO_i2c_LCD',
    version='0.1.0',
    description='Simple module for using a HD44780 LCD over I2C',
    url='https://github.com/AllanGallop/RPi_GPIO_i2c_LCD',
    download_url='https://github.com/AllanGallop/RPi_GPIO_i2c_LCD/archive/0.1.0.tar.gz',
    author='Allan Gallop',
    author_email='allangallop@gmail.com',
    keywords='LCD i2c HD44780 PCF8574 raspberry pi',
    packages=find_packages(),
    install_requires=['SMBUS'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)