from setuptools import find_packages, setup

package_name = 'py_message_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stupidbox',
    maintainer_email='whdals6831@gmail.com',
    description='ROS2 Python custom message publisher and subscriber demo',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status_publisher = py_message_demo.status_publisher_node:main',
            'status_subscriber = py_message_demo.status_subscriber_node:main',
        ],
    },
)
