from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = "0.0.6"


ext = Pybind11Extension(
        "aalink",
        ["src/aalink.cpp"],
        include_dirs=["ext/android-ifaddrs", "ext/link/include", "ext/link/modules/asio-standalone/asio/include"],
        define_macros=[("VERSION_INFO", __version__)],
        cxx_std=20,
    )


ext.extra_compile_args += ["-DLINK_PLATFORM_LINUX"]
ext.extra_compile_args += ["-Wno-multichar"]

setup(
    name="aalink",
    version=__version__,
    author="Artem Popov",
    author_email="art@artfwo.net",
    url="https://github.com/ceebeel/aalink",
    description="Async Python interface for Ableton Link",
    long_description="",
    ext_modules=[ext],
    # extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
