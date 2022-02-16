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
#     spack install regtools
#
# You can edit this file again by typing:
#
#     spack edit regtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Regtools(CMakePackage):
    """Integrate DNA-seq and RNA-seq data to identify mutations that are associated with regulatory effects on gene expression.."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/griffithlab/regtools"
    url      = "https://github.com/griffithlab/regtools/archive/refs/tags/0.5.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.5.2', sha256='24d3bc18174237e0fc2d0330839c8dc21c97cdb7d6e528c518188c10f17f3e7e')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
    
    def install(self,spec,prefix):
        mkdir(prefix.bin)
        cmake(self.stage.source_path)
        install(self.build_directory + '/regtools',prefix.bin)
        chmod = which('chmod')
        chmod('+x',prefix.bin.regtools)
     

