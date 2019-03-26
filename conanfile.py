#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanInvalidConfiguration
import os


class XOrgMacrosConan(ConanFile):
    name = "xorg-macros"
    version = "1.19.2"
    description = "This is a set of autoconf macros used by the configure.ac scripts in" \
                  "other Xorg modular packages, and is needed to generate new versions " \
                  "of their configure scripts with autoconf."
    topics = ("conan", "xorg-macros", "macros", "x11")
    url = "https://github.com/bincrafters/conan-xorg-macros"
    homepage = "https://gitlab.freedesktop.org/xorg/util/macros"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "X11"
    exports = ["LICENSE.md"]
    settings = "os", "arch", "compiler", "build_type"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("only Linux is supported")

    def source(self):
        source_url = "https://www.x.org/archive//individual/util/util-macros-%s.tar.bz2" % self.version
        tools.get(source_url, sha256="d7e43376ad220411499a79735020f9d145fdc159284867e99467e0d771f3e712")
        os.rename("util-macros-" + self.version, self._source_subfolder)

    def build(self):
        with tools.chdir(self._source_subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            env_build.make()
            env_build.install()

    def package(self):
        self.copy(pattern="COPYING*", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
