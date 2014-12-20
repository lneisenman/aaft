# -*- coding: utf-8 -*-
from __future__ import (print_function, absolute_import,
                        unicode_literals, division)
import six

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from .aaft import AAFTsur
