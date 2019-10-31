import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='vnc_api',  
     version='0.1',
     author="Michael Henkel",
     author_email="michael.henkel@gmail.com",
     description="Contrail VNC API",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
