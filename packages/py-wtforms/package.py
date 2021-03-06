# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-wtforms
#
# You can edit this file again by typing:
#
#     spack edit py-wtforms
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyWtforms(PythonPackage):
    """A Flexible forms validation and redering library for Python web development."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pypi.org/project/WTForms"
    pypi     = "WTForms/WTForms-2.2.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.2.1', sha256='0cdbac3e7f6878086c334aa25dc5a33869a3954e9d1e015130d65a69309b3b61') 
    version('2.0.1', sha256='62859c74be4683601b5265ba83b9babd8a8f1cdd0ba31600fa1e70d295cd4ed2')

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on('python@3.8', type=('build', 'run'))
    # depends_on('py-pip@X.Y:', type='build')
    # depends_on('py-wheel@X.Y:', type='build')

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on('py-setuptools', type='build')
    # depends_on('py-flit-core', type='build')
    # depends_on('py-poetry-core', type='build')
    depends_on('py-babel')
    depends_on('py-markupsafe')


