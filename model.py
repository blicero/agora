#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2024-05-25 23:39:57 krylon>
#
# /data/code/python/agora/model.py
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
agora.model

(c) 2024 Benjamin Walkenhorst
"""

from dataclasses import dataclass, field

from krylib import Identifiable


@dataclass(slots=True, kw_only=True)
class Building(Identifiable):
    """A building is a structure of some sort."""

    name: str
    description: str
    hp: int
    hp_max: int
    tags: set[str] = field(default_factory=set[str])


@dataclass(slots=True, kw_only=True)
class City(Identifiable):
    """City is the settlement/town/city the player is trying to grow."""

    name: str
    population: int = 10
    gold: int = 0
    food: int = 250
    buildings: set[Building]


# Local Variables: #
# python-indent: 4 #
# End: #
