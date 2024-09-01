from setuptools import setup
import os
from glob import glob

package_name = 'nav_robot_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Ensure package.xml is in the right path
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        # Include all world files
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.world'))),
        # Include URDF and model files if they exist
        (os.path.join('share', package_name, 'models'), glob(os.path.join('models', '*.urdf'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mariocool11',
    maintainer_email='roncidesigns11@gmail.com',
    description='Robot simulation package with Gazebo for ROS 2 Humble',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add any entry points if necessary
        ],
    },
)

