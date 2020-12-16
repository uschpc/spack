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
#     spack install libgff
#
# You can edit this file again by typing:
#
#     spack edit libgff
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libgff(CMakePackage):
    """This is an attempt to perform a simple "libraryfication" of the GFF/GTF parsing code that is used in the Cufflinks codebase."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/Kingsford-Group/libgff"
    url      = "https://github.com/Kingsford-Group/libgff/archive/v1.0.tar.gz"

    maintainers = ['CeSul']

    version('1.0', sha256='9a2265a5b9c30bd7da243e4618b6ee71db5bb4a384965ef74ecf540a7db7846d')


#    def cmake_args(self):
#        # FIXME: Add arguments other than
#        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
#        # FIXME: If not needed delete this function
#        args = [""]
#        return args
