# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class Cellranger(Package):
    """Cell Ranger is a set of analysis pipelines that process Chromium single-cell RNA-seq output to align reads, generate feature-barcode matrices and perform clustering and gene expression analysis."""

    homepage = "https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger"
    url       = "file://{0}/cellranger-4.0.0.tar.gz".format(os.getcwd())




    maintainers = ['CeSul']

    version('4.0.0', sha256='e8e43e91538cba667836d437ac1d5ca675ea9d1acd977ac967f7b65c12254a21')

    depends_on('python')

    def setup_run_environment(self,env):
        # translate 'sourceme.bash' into module file
        
        # PATH
        env.prepend_path('PATH',join_path(self.prefix.bin,'tenkit'))
        env.prepend_path('PATH',join_path(self.prefix,'external','anaconda','bin'))
        env.prepend_path('PATH',join_path(self.prefix,'external','martian','bin'))
        env.prepend_path('PATH',join_path(self.prefix.lib,'bin'))

        # PYTHONPATH
        env.prepend_path('PYTHONPATH',join_path(self.prefix,'lib','python'))
        env.prepend_path('PYTHONPATH',join_path(self.prefix,'external','martian','adapters','python'))

        #MROPATH
        env.prepend_path('MROPATH',join_path(self.prefix,'mro'))

    def install(self, spec, prefix):

        install_tree('.env.json',prefix)
        install_tree('.version',prefix)

        mkdir(prefix.bin)
        install_tree('bin',prefix.bin)
        symlink(prefix.bin.cellranger,prefix.cellranger)

        mkdir(prefix.externel)
        install_tree('external',prefix.external)

        mkdir(prefix.lib)
        install_tree('lib',prefix.lib)

        mkdir(prefix.mro)
        install_tree('mro',prefix.mro)
        install('LICENSE',prefix)
        install('builtwith.json',prefix)

        symlink(prefix.lib.python.cellranger.target_panels,prefix.target_panels)
        #install_tree('target_panels',prefix.target_panels)
