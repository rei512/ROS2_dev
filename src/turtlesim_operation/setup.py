from setuptools import setup

package_name = 'turtlesim_operation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
	'turtlesim_operation.turtlesim_operation', 
	'turtlesim_operation.turtlesim_ope_widget',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ], 
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='t_rei_512@yahoo.co.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'controller= turtlesim_operation.turtlesim_operation'
        ],
    },
)
