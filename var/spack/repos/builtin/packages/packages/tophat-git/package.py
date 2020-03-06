# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install tophat-git
#
# You can edit this file again by typing:
#
#     spack edit tophat-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class TophatGit(Package):
    """TopHat is a fast splice junction mapper for RNA-Seq reads."""

    homepage = "https://ccb.jhu.edu/software/tophat/index.shtml"
    url      = "https://github.com/infphilo/tophat.git"

    maintainers = ['CeSul']

    version('2.1.2', '37540ce3f0c10e0f0bfafa2f29450055fc5da384')

    depends_on('autotools')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
