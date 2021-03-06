#!/usr/bin/env python
"""
Check the tags in a corpus.

Constantine Lignos
February 2013

"""

# Copyright (c) 2013 Constantine Lignos
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import codecs

# Hack to allow import of split_token, forces this to be run from subdir.
sys.path.append('..')
from eval_codeswitch import split_token


GOOD_TAGS = set(['e', 's', 'n'])


linenum = 0
for line in codecs.getreader('utf_8')(sys.stdin):
    linenum += 1
    line = line.rstrip()
    try:
        _, tags = zip(*[split_token(token) for token in line.split()])
    except ValueError as err:
        print err
        print "From line {}: {!r}".format(linenum, line)
    
    for tag in tags:
        if tag not in GOOD_TAGS:
            print "Bad tag:", tag
            print "From line {}: {!r}".format(linenum, line)
