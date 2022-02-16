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
#     spack install r-shinycssloaders
#
# You can edit this file again by typing:
#
#     spack edit r-shinycssloaders
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RShinycssloaders(RPackage):
    """Add loading animations to a Shiny output while it's recalculating."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/daattali/shinycssloaders/r"
    url      = "https://github.com/daattali/shinycssloaders/archive/refs/tags/1.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.0.0', sha256 = '48b2a4eb3ca08ce0bb9c91f265c8812a8a1e5bb59daaf900f52dd7780add5f8e')

    # FIXME: Add dependencies if required.
    depends_on('r-shiny')

