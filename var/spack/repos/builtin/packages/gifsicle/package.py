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
#     spack install gifsicle
#
# You can edit this file again by typing:
#
#     spack edit gifsicle
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gifsicle(AutotoolsPackage):
    """Gifsicle is a command-line tool for creating, editing, and getting information about GIF images and animations"""

    homepage = "https://www.lcdf.org/gifsicle/"
    url      = "https://www.lcdf.org/gifsicle/gifsicle-1.92.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.92', sha256='5ab556c01d65fddf980749e3ccf50b7fd40de738b6df679999294cc5fabfce65')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
