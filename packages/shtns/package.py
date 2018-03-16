##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Shtns(AutotoolsPackage, PythonPackage):
    """SHTns: a spherical harmonics transform library.

       SHTns is a high performance library for Spherical Harmonic Transform
       written in C, aimed at numerical simulation (fluid flows, mhd, ...) in
       spherical geometries."""

    homepage = "https://users.isterre.fr/nschaeff/SHTns"
    url      = "https://bitbucket.org/nschaeff/shtns/downloads/shtns-2.9-r597.tar.gz"
    list_url = "https://bitbucket.org/nschaeff/shtns/downloads/"

    version('3.0-r618', 'b2a3b1e1d661a3db7c5c214d6212aadd')
    version('2.9-r597', '7c2389a415cf5605b65298c2148eceec')

    variant('openmp', default=False, description="Enable OpenMP support.")
    variant('python', default=False, description="Enable Python bindings.")

    depends_on('fftw')
    depends_on('fftw+openmp', when='+openmp')
    depends_on('py-numpy', when='+python')

    @property
    def libs(self):
        # Construct the list of libraries that needs to be found
        libraries = ['libshtns', 'libfftw3']

        if 'openmp' in query_parameters and '+openmp' in self.spec:
            libraries.append('libfftw3' + '_omp')

        return find_libraries(libraries, root=self.prefix, recurse=True)

    def autoreconf(self, spec, prefix):
        pass

    def configure(self, spec, prefix):
        # Base options
        options = [
            '--prefix={0}'.format(prefix),
        ]

        if '+openmp' in spec:
            # Note: Apple's Clang does not support OpenMP.
            if spec.satisfies('%clang'):
                ver = str(self.compiler.version)
                if ver.endswith('-apple'):
                    raise InstallError("Apple's clang does not support OpenMP")
            options.append('--enable-openmp')

        if '+python' in spec:
            options.append('--enable-python')
        else:
            options.append('--disable-python')

        configure = Executable('./configure')
        configure(*options)

    def install(self, spec, prefix):
        if '+python' in spec:
            PythonPackage.install(self, spec, prefix)
        else:
            make('PREFIX={0} install'.format(prefix))
