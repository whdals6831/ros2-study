from setuptools import find_packages, setup

package_name = 'py_topic_demo'

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
    description='ROS2 Python topic publisher and subscriber demo',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = py_topic_demo.publisher_node:main',
            'subscriber = py_topic_demo.subscriber_node:main',
        ],
    },
)
