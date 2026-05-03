from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'headlight'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abduhu S. Chauhdury',
    maintainer_email='etprous@gmail.com',
    description='An open-source autonomy stack using ROS2/Python.',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ui = headlight.ui:main',
            'demo = headlight.demo:main'
        ],
    },
)
