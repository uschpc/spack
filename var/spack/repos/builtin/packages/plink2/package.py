# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os


class Plink2(Package):
    """A comprehensive update to the PLINK association analysis toolset. """

    homepage = "www.cog-genomics.org/plink/2.0/"
    url      = "https://github.com/chrchang/plink-ng/archive/v2.00a2.3.tar.gz"

    maintainers = ['CeSul']

    version('2.00a2.3', sha256='4a9e9ff670967f9766bcd5571d028ed6c04bc8f07781eac1b95366748544df77')
    version('2.00a2.2', sha256='84192d3be05cf6d76e6e572d41870335bb946b31ab9b694610dd9315c2219e7c')
    version('2.00a2.1', sha256='4714fc389b61819bdc40ca05d1a924482e93d25a0164980a89073666a1199f5b')

    depends_on('blas')
    depends_on('zlib')
    depends_on('zstd')
    



    def install(self, spec, prefix):
        
        # Set library locations
        env['CFLAGS']      = "-O3 %s %s %s" %(spec['zstd'].headers.include_flags,
                             spec['blas'].headers.include_flags,spec['zlib'].headers.include_flags)

        env['CXXFLAGS']    = "-O3 %s %s %s" %(spec['zstd'].headers.include_flags,
                             spec['blas'].headers.include_flags,spec['zlib'].headers.include_flags)

        env['ZLIB']        = spec['zlib'].libs.ld_flags
        env['BLASFLAGS64'] = spec['blas'].libs.ld_flags

        # Set install path
        print("Installing to %s" %prefix)
        env['PREFIX']      = prefix
        env['DESTDIR']     = ""

        os.chdir('2.0')


        make()
        make('install')
