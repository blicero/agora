#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2024-05-25 23:36:25 krylon>
#
# /data/code/python/agora/test_model.py
# created on 25. 05. 2024
# (c) 2024 Benjamin Walkenhorst
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY BENJAMIN WALKENHORST ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""
agora.test_model

(c) 2024 Benjamin Walkenhorst
"""

import traceback
import unittest
from typing import Final

from agora.model import Building


class BuildingTest(unittest.TestCase):
    """Test the Building class, lest they collapse."""

    def test_building_create(self) -> None:
        """
        Test creating a building.

        Fortunately, it's cheaper and quicker to do in software.
        """
        try:
            b: Building = Building(  # pylint: disable-msg=E1123
                ID=42,
                name="Bikeshed",
                description="Where you put your bicycles",
                hp=25,
                hp_max=25,
            )
        except Exception as err:  # pylint: disable-msg=W0718
            msg: Final[str] = "\n".join(traceback.format_exception(err))
            self.fail(msg)

        self.assertEqual(b.ID, 42)

# Local Variables: #
# python-indent: 4 #
# End: #
