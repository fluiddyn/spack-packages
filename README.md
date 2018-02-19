# spack-packages
A repository of spack packages for FluidDyn

Assuming `spack` is already setup, to add this repo:

```sh
  git clone https://github.com/fluiddyn/spack-packages.git
  spack repo add spack-packages
```

This will add a new repository with the namespace `fluiddyn`.

## Spack cheatsheet
First install [Spack](https://github.com/spack/spack)

```sh
  git clone https://github.com/fluiddyn/spack.git
```

Set the `.bashrc` or similar with the path to where you cloned `spack`.

```sh
  export SPACK_ROOT=$HOME/spack
  . $SPACK_ROOT/share/spack/setup-env.sh
```

or atleast add `$SPACK_ROOT/bin` to the `$PATH` environment variable.

Read more on how to [get started with
Spack](https://spack.readthedocs.io/en/latest/getting_started.html)
Some examples of useful `spack` commands::

```sh
  # List and try to detect compilers 
  spack compilers
  spack compiler find

  # Configure system-wide installed packages that you would like to use
  spack config edit packages

  # Integrate with or install environment-modules / lmod / dotkit
  spack bootstrap

  # To enforce different options, check and install
  spack spec fftw%gcc+openmp cflags="-O3"
  spack install fftw%gcc+openmp cflags="-O3"

  # Clean temporary builds
  spack clean
```
