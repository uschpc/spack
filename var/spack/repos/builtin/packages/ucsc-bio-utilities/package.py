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
#     spack install ucsc-bio-utilities
#
# You can edit this file again by typing:
#
#     spack edit ucsc-bio-utilities
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class UcscBioUtilities(MakefilePackage):
    """Genome Browser and Blat application binaries built for standalone
command-line use on various supported Linux and UNIX platforms."""

    homepage = "http://hgdownload.cse.ucsc.edu/admin/exe/"
    url      = "http://hgdownload.cse.ucsc.edu/admin/exe/userApps.v390.src.tgz"

    maintainers = ['CeSul']

    version('394', sha256='e5756cb332c172cf589ba449c99d36d370c826bce3be9a546090bdfdefcab330')

    # FIXME: Add dependencies if required.
    depends_on('zlib', type='build')
    depends_on('libpng', type='build')
    depends_on('pcre', type='build')

    def install(self,spec,prefix):
        install_tree('bin',prefix.bin)
