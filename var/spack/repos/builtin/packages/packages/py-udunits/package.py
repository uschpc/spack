# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class PyUdunits(PythonPackage):
    """The MetOffice cf_units Python interface to the UDUNITS-2 Library."""
    homepage = "https://github.com/SciTools/cf_units"
    url      = "https://github.com/SciTools/cf_units/archive/v1.1.3.tar.gz"

    version('1.1.3', sha256='cc27f4f06c99d242c36beb8dc5c517e1b1124a8c65ca3f76f372b9674aa320ba')

    maintainers = ['citibeth']

    depends_on('py-setuptools', type='build')
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-netcdf4', type=('build', 'run'))
    depends_on('udunits2')

    # See: https://github.com/SciTools/cf_units/blob/master/cf_units/etc/site.cfg.template
    # udunits2_path = /path/to/libudunits2.so
    # udunits2_xml_path = /path/to/udunits2.xml
    site_cfg_template = """[System]
udunits2_path = %s
udunits2_xml_path = %s
"""

    @run_after('install')
    def configure_template(self):
        spec = self.spec

        cfg_templates = find(spec.prefix, ['site.cfg.template'])
        if len(cfg_templates) != 1:
            tty.die(
                'Found %d instances of site.cfg.template, wanted 1' %
                len(cfg_templates))
        cfg_template = cfg_templates[0]

        cfg = os.path.join(os.path.split(cfg_template)[0], 'site.cfg')

        udunits2_xml_path = os.path.join(
            spec['udunits2'].prefix, 'share', 'udunits', 'udunits2.xml')

        with open(cfg, 'w') as fout:
            fout.write(self.site_cfg_template %
                       (spec['udunits2'].libs, udunits2_xml_path))
