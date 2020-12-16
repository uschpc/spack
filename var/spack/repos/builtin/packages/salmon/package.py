# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Salmon(CMakePackage):
    """Salmon is a tool for quantifying the expression of transcripts using
       RNA-seq data."""

    homepage = "http://combine-lab.github.io/salmon/"
    url      = "https://github.com/COMBINE-lab/salmon/archive/v0.8.2.tar.gz"

    version('1.1.0', sha256='550bbdc18970b015f467d418385a5779cd0d6f642cb710766c66761c12c9bc50')
    version('0.14.1', sha256='05289170e69b5f291a8403b40d6b9bff54cc38825e9f721c210192b51a19273e')
    version('0.12.0', sha256='91ebd1efc5b0b4c12ec6babecf3c0b79f7102e42b8895ca07c8c8fea869fefa3')
    version('0.9.1', sha256='3a32c28d217f8f0af411c77c04144b1fa4e6fd3c2f676661cc875123e4f53520')
    version('0.8.2', sha256='299168e873e71e9b07d63a84ae0b0c41b0876d1ad1d434b326a5be2dce7c4b91')

    depends_on('tbb')
    depends_on('jemalloc')
    depends_on('libiconv', 'build')
    depends_on('libgff')
    depends_on('boost')

    depends_on('curl', when='@0.14.1:')

    conflicts('%gcc@:5.1', when='@0.14.1:')

    def patch(self):
        # remove static linking to libstdc++
        filter_file('-static-libstdc++', '', 'CMakeLists.txt', string=True)

    def cmake_args(self):
        args = ['-DBOOST_ROOT=%s' % self.spec['boost'].prefix]
        args.append('-DTBB_INSTALL_DIR=%s' % self.spec['tbb'].prefix)
        args.append('-DIconv_INCLUDE_DIR=%s/include' % self.spec['libiconv'].prefix)
        args.append('-DIconv_LIBRARY=%s/lib/libiconv.so' % self.spec['libiconv'].prefix)
        args.append('-DJEMALLOC_LIBRARY=%s/lib' % self.spec['jemalloc'].prefix)
        args.append('-DJEMALLOC_INCLUDE_DIR=%s/include' % self.spec['jemalloc'].prefix)
        args.append('-DGFF_INCLUDE_DIR=%s/include' % self.spec['libgff'].prefix)
        args.append('-DGFF_LIBRARY=%s/lib' % self.spec['libgff'].prefix)
        args.append('-DCMAKE_CXX_FLAGS=-I%s/lib -L%s/include' % (self.spec['libgff'].prefix,self.spec['libgff'].prefix))

        return args
