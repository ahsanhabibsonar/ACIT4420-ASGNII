from setuptools import setup, find_packages
import os

# Read the README file for the long description
def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()

# Define the automation task (optional, if you have one)
def post_install():
    # You can add any automation task or script you want to run after installation here
    print("Running automation task after installation...")
    os.system('echo "Automation task complete!"')

setup(
    name='morning_greetings',
    version='0.1.0',  # Update the version number as needed
    author='Ahsan Habib Sonar',
    author_email='ahson6184@oslomet.no',
    description='A Python package for sending morning greetings',
    long_description=read_file('README.md'),  # Assumes you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/ahsanhabibsonar/ACIT4420-ASGNII',  # Update with your repository URL
    packages=find_packages(),  # Automatically find all packages and sub-packages
    install_requires=[
        # Add any dependencies your package needs here
        # Example: 'requests>=2.25.1',
    ],
    entry_points={
        'console_scripts': [
            # This allows you to run the automation task from the command line
            'run-automation-task=morning_greetings.automation:post_install',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust the Python version requirement as needed
    include_package_data=True,
    zip_safe=False,
)

# Optionally call the automation task directly during setup
if __name__ == '__main__':
    post_install()
