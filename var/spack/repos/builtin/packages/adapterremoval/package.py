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
#     spack install adapterremoval
#
# You can edit this file again by typing:
#
#     spack edit adapterremoval
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Adapterremoval(MakefilePackage):
    """AdapterRemoval searches for and removes adapter sequences from High-Throughput Sequencing (HTS) data and (optionally) trims low quality bases from the 3' end of reads following adapter removal. """

    homepage = "https://github.com/MikkelSchubert/adapterremoval"
    url      = "https://github.com/MikkelSchubert/adapterremoval/archive/v2.3.1.tar.gz"

    maintainers = ['CeSul']

    version('2.3.1', sha256='82468c69e65ee6ca3580754fbfe5775210e684c7300fee07a8d39944ed331e77')
    version('2.3.0', sha256='626fbe59e49a434f6c835339986b9cf034d4dab3145ff16cb4df9f244bed0b97')
    version('2.2.4', sha256='30df9464a1b4be3e6ea80a28a01e0d95f3a9f188bee260329237d1df2974f7b1')


    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter('PREFIX := /usr/local', 'PREFIX='+prefix)
