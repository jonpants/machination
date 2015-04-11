##########################################################################
# Machination
# Copyright (c) 2014, Alexandre ACEBEDO, All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.
##########################################################################

import logging
from logging import StreamHandler

formatter = logging.Formatter('%(message)s')
strHandler = StreamHandler()
strHandler.setLevel(logging.DEBUG)
strHandler.setFormatter(formatter)

COMMANDLINELOGGER = logging.getLogger("cmdline")
COMMANDLINELOGGER.addHandler(strHandler)

REGISTRYLOGGER = logging.getLogger("registries")
REGISTRYLOGGER.addHandler(strHandler)

CORELOGGER = logging.getLogger("core")
CORELOGGER.addHandler(strHandler)

FILEGENERATORLOGGER = logging.getLogger("filegenerator")
FILEGENERATORLOGGER.addHandler(strHandler)

  
def setGlobalLogLevel(lvl):
  FILEGENERATORLOGGER.setLevel(logging.DEBUG)
  CORELOGGER.setLevel(logging.DEBUG)
  REGISTRYLOGGER.setLevel(logging.DEBUG)
  COMMANDLINELOGGER.setLevel(logging.DEBUG)