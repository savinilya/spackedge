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
#     spack install py-flask-wtf
#
# You can edit this file again by typing:
#
#     spack edit py-flask-wtf
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyFlaskWtf(PythonPackage):
    """Simple integration of Flask and WTForms. including CSRF, file upload and reCAPTHCA"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pypi.org/project/Flask-WTF/"
    pypi     = "Flask-WTF/Flask-WTF-0.14.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.14.2', sha256='5d14d55cfd35f613d99ee7cba0fc3fbbe63ba02f544d349158c14ca15561cc36')

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

    # FIXME: Add additional dependencies if required.
    depends_on('py-flask', type=('build', 'run'))
    depends_on('py-wtforms', type=('build', 'run'))
    depends_on('py-itsdangerous', type=('build', 'run'))

