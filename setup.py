# Available at setup time due to pyproject.toml
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = "0.0.6"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension(
        "aalink",
        ["src/aalink.cpp"],
        include_dirs=["ext/link/include", "ext/link/modules/asio-standalone/asio/include"],
        library_dirs=["ext/link", "ext/link/modules/asio-standalone/asio"],
        libraries=["AbletonLink", "ASIO"],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="aalink",
    version=__version__,
    author="Artem Popov",
    author_email="art@artfwo.net",
    url="https://github.com/ceebeel/aalink",
    description="Async Python interface for Ableton Link",
    long_description="",
    ext_modules=ext_modules,
    # extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
