SimpleEncrypt README
====================

This small python application was created in order to provide a simple way to encrypt and decrypt arbitrary pieces of text using a password provided by the user. In particular, it is intended for use as a plugin to the Zim Desktop Wiki.

Python Environment Configuration
================================
Install PyCrypto
	1. Download tarball from PyCrypto website
	2. Ensure MS Visual Studio 2010 Express is installed (free)
	3. Set environment to use MSVS2010 using: SET VS90COMNTOOLS=%VS100COMNTOOLS%
	4. In the PyCrypto directory run: python setup.py install
