#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Last Change: Tue Jul 17 05:00 PM 2007 J

# The code and descriptive text is copyrighted and offered under the terms of
# the BSD License from the authors; see below. However, the actual dataset may
# have a different origin and intellectual property status. See the SOURCE and
# COPYRIGHT variables for this information.

# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     * Neither the author nor the names of any contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Name of dataset."""

__docformat__ = 'restructuredtext'

COPYRIGHT   = """Pending"""
TITLE       = ""
SOURCE      = """
"""

DESCRSHORT  = """"""

DESCRLONG   = """"""

NOTE        = """
When loaded, the attributes are

exog = AVGEXP

endog = AGE INCOME INCOME**2 OWNRENT

There are 72 observations for which AVGEXP != 0

The original dataset including the following
can be found in the ccard/src/ folder
----------------------------------------------

MDR = Number of derogator reports

Acc = Credit card application accpeted (1=yes)

Age = Age in years + 12ths of a year

Income = Income divided by 10,000

Avgexp = Avg. monthly credit card expenditure

Ownrent = Indiviual owns(1) or rents(0) home

Selfempl = (1=yes, 0=no)

"""

import numpy as np

class load():
    """load the credit card data and returns a data class.

    :returns:
        data instance:
            a class of the data with array attrbutes 'endog' and 'exog'
    """
    def __init__(self):
        from ccard import __dict__, names
        self._names = names
        self._d = __dict__
        self.endog = np.array(self._d[self._names[0]], dtype=np.float)
        self.exog = np.column_stack(self._d[i] \
                    for i in self._names[1:]).astype(np.float)

