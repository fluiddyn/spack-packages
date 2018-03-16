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


class P3dfft(AutotoolsPackage):
    """Scalable Framework for Three-Dimensional Fourier Transforms.

       It is a library for large-scale computer simulations on parallel
       platforms. It implements 3D FFT and related algorithms such as Chebyshev
       transform (an important class of algorithm for simulations in a wide
       range of fields). P3DFFT uses 2D, or pencil, decomposition."""

    homepage = "https://www.p3dfft.net"
    url      = "https://github.com/CyrilleBonamy/p3dfft.git"

    version('2.7.5', git=url, branch='master')

    depends_on('fftw+mpi')
    depends_on('mpi')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')

    #  autoreconf_extra_args = ['-fvi']
    #  force_autoreconf = True

    def autoreconf(self, spec, prefix):
        libtoolize()
        aclocal()
        autoconf()
        automake('--add-missing')

    def configure(self, spec, prefix):
        options = [
            '--prefix={0}'.format(prefix), '--enable-fftw',
            '--with-fftw={0}'.format(spec['fftw'].prefix),
            'CC={0}'.format(spec['mpi'].mpicc),
            'CCLD={0}'.format(spec['mpi'].mpifc),
        ]

        configure = Executable('./configure')
        configure(*options)
        #  configure = Executable('../configure')

    #      if '+double' in spec['fftw']:
    #          with working_dir('double', create=True):
    #              configure(*options)
    #      if '+float' in spec['fftw']:
    #          with working_dir('float', create=True):
    #              configure('--enable-float', *options)
    #
    #  def build(self, spec, prefix):
    #      if '+double' in spec['fftw']:
    #          with working_dir('double'):
    #              make()
    #      if '+float' in spec['fftw']:
    #          with working_dir('float'):
    #              make()
    #
    #  def check(self):
    #      spec = self.spec
    #      if '+double' in spec['fftw']:
    #          with working_dir('double'):
    #              make("check")
    #      if '+float' in spec['fftw']:
    #          with working_dir('float'):
    #              make("check")
    #
    #  def install(self, spec, prefix):
    #      if '+double' in spec['fftw']:
    #          with working_dir('double'):
    #              make("install")
    #      if '+float' in spec['fftw']:
    #          with working_dir('float'):
    #              make("install")
