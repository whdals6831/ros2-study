from setuptools import find_packages, setup

package_name = 'py_topic_advanced'

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
    description='ROS2 Python advanced topic demo',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status_publisher = py_topic_advanced.status_publisher_node:main',
            'status_subscriber = py_topic_advanced.status_subscriber_node:main',
        ],
    },
)
