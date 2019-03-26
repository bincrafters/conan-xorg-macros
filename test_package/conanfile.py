#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile
import os


class TestPackageConan(ConanFile):
    requires = "m4_installer/1.4.18@bincrafters/stable"

    def test(self):
        rootpath = self.deps_cpp_info["xorg-macros"].rootpath
        m4inc = os.path.join(rootpath, "share", "aclocal")
        m4test = os.path.join(self.source_folder, "test_package.m4")
        self.run("m4 -P -I %s %s" % (m4inc, m4test))
