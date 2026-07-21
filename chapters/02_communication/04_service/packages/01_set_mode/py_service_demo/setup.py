from setuptools import find_packages, setup

package_name = 'py_service_demo'

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
    description='ROS2 Python service demo',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'mode_server = py_service_demo.mode_server_node:main',
            'mode_client = py_service_demo.mode_client_node:main',
        ],
    },
)
