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
#     spack install py-gunicorn
#
# You can edit this file again by typing:
#
#     spack edit py-gunicorn
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyGunicorn(PythonPackage):
    """Gunicorn (Green Unicorn) is a Python WSGI HTTP server for Unix."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gunicorn.com"
    pypi     = "gunicorn/gunicorn-19.9.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('19.9.0', sha256='fa2662097c66f920f53f70621c6c58ca4a3c4d3434205e608e121b5b3b71f4f3')

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
    # depends_on('py-foo', type=('build', 'run'))

