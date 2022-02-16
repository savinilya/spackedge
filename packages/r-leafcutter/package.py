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
#     spack install r-leafcutter
#
# You can edit this file again by typing:
#
#     spack edit r-leafcutter
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RLeafcutter(RPackage):
    """LeafCutter: Annotation-free quantification of RNA splicing."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://davidaknowles.github.io/leafcutter/"
    url      = "https://github.com/savinilya/spackedge/blob/main/src/leafcutter-0.2.7.tar.gz"
    version('0.2.7',sha256="1b8b6974f32648deb44879f8fb26d8ae097ed55c2174a3537636da5407ffb2a6")

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    # FIXME: Add dependencies if required.
    depends_on('samtools@1.13',type=('build','run'))
    depends_on('regtools',type=('build','run'))
    depends_on('python@2.7.18',type=('build','run'))
    depends_on('r+X@3.5.1',type=('build','run'))
    depends_on('r-domc',type=('build','run'))
    depends_on('r-htmltools@0.5.1',type=('build','run'))
    depends_on('r-dplyr',type=('build','run'))
    depends_on('r-foreach',type=('build','run'))
    depends_on('r-ggplot2',type=('build','run'))
    depends_on('r-gridextra',type=('build','run'))
    depends_on('r-hmisc',type=('build','run'))
    depends_on('r-rcpp',type=('build','run'))
    depends_on('r-rcppeigen',type=('build','run'))
    depends_on('r-reshape2',type=('build','run'))
    depends_on('r-optparse',type=('build','run'))
    depends_on('r-dt',type=('build','run'))
    depends_on('r-shiny',type=('build','run'))
    depends_on('r-shinycssloaders',type=('build','run'))
    depends_on('r-rstan',type=('build','run'))
    depends_on('r-stanheaders',type=('build','run'))
    depends_on('r-r-utils@2.5.0',type=('build','run'))
    depends_on('r-intervals',type=('build','run'))
