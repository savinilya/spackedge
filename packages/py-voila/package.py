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
#     spack install py-voila
#
# You can edit this file again by typing:
#
#     spack edit py-voila
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyVoila(PythonPackage):
    """VOILA - majiq visualistion tool"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://majiq.biociphers.org"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url      = "https://github.com/savinilya/spackedge/raw/main/src/voila-2.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.0.0', sha256='ea7f63fd18ef021d2123eba502573e94c1515d91988fd249330b47c77044c09d')

    depends_on('python@3.8', type=('build', 'run'))
    # depends_on('py-pip@X.Y:', type='build')
    # depends_on('py-wheel@X.Y:', type='build')

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on('py-setuptools', type='build')
    depends_on('py-setuptools-scm', type='build')
    # depends_on('py-flit-core', type='build')
    # depends_on('py-poetry-core', type='build')

    # FIXME: Add additional dependencies if required.
    depends_on('py-click', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-flask', type=('build', 'run'))
    depends_on('py-flask-session', type=('build', 'run'))
    depends_on('py-flask-wtf', type=('build', 'run'))
    depends_on('py-gitdb', type=('build', 'run'))
    depends_on('py-gitpython', type=('build', 'run'))
    depends_on('py-gunicorn', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-itsdangerous', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-markupsafe', type=('build', 'run'))
    depends_on('py-networkx', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-psutil', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-smmap', type=('build', 'run'))
    depends_on('py-waitress', type=('build', 'run'))
    depends_on('py-werkzeug', type=('build', 'run'))
    depends_on('py-wtforms', type=('build', 'run'))

