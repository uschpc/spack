# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Time(AutotoolsPackage):
    """The time command runs another program, then displays
       information about the resources used by that program."""

    homepage = "https://www.gnu.org/software/time/"
    url      = "https://ftpmirror.gnu.org/time/time-1.9.tar.gz"

    version('1.9', sha256='fbacf0c81e62429df3e33bda4cee38756604f18e01d977338e23306a3e3b521e')

    build_directory = 'spack-build'
