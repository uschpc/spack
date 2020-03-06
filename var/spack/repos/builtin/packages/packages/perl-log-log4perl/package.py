# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlLogLog4perl(PerlPackage):
    """Log4j implementation for Perl"""

    homepage = "http://search.cpan.org/~mschilli/Log-Log4perl-1.44/lib/Log/Log4perl.pm"
    url      = "https://github.com/mschilli/log4perl/archive/rel_146.tar.gz"

    version('146', sha256='a361e483095795753b97f8a506b40c24c753cf73828bb8697665499ef8596402')
