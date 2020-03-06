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
#     spack install pcl
#
# You can edit this file again by typing:
#
#     spack edit pcl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pcl(CMakePackage):
    """The Point Cloud Library (PCL) is a standalone, large scale, open project for 2D/3D image and point cloud processing."""
    homepage = "http://www.pointclouds.org/"
    url      = "https://github.com/PointCloudLibrary/pcl/archive/pcl-1.9.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.10.0', sha256='dd24f93967ba9512a02d6fa15855084a45deb4cd6f3662f22afbbf0d65978d20')

    # FIXME: Add dependencies if required.
    depends_on('boost')
    depends_on('eigen')
    depends_on('flann')
    depends_on('vtk')
    depends_on('cuda')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
