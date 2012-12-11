#!/usr/bin/env python
import os
import pdb
import re
import sys
import toolframe
import xml.etree.ElementTree as ET

from optparse import *

# ---------------------------------------------------------------------------
def xml_attredit(argv):
    """attredit - edit attribute values in XML files

    usage: xmltool attredit [-d] -a attrib -e ... <filename> <filename> ...

    -a     which attribute to edit
    -d     run under python debugger
    -e     edits to make

    Result is written to stdout.
    """
    p = OptionParser()
    p.add_option('-d', '--debug',
                 action='store_true', default=False, dest='debug',
                 help='run the debugger')
    p.add_option('-a', '--attr',
                 action='store', default=None, dest='attrib',
                 help='attribute to edit')
    p.add_option('-e', '--edit',
                 action='append', default=None, dest='edits',
                 help='edit(s) to make on the input')
    p.add_option('-o', '--output',
                 action='store', default=None, dest='output',
                 help='write to file OUTPUT')
    (o, a) = p.parse_args(argv)

    if o.debug: pdb.set_trace()

    ehash = {}
    for e in o.edits:
        q = e.split(e[1])
        ehash[q[1]] = q[2]

    for filename in a:
        tagl = []
        X = ET.parse(filename)
        for el in X.iter():
            if o.attrib in el.attrib:
                # -- do the edit
#            tagl.append(el.tag)

 #       cp = os.path.commonprefix(tagl)
        # print cp

  #      for el in X.iter('%sservice' % cp):
            # print '---------------------------------'
            # print el.attrib
   #         attr = el.attrib
    #        if 'serviceType' in attr.keys() and attr['serviceType'] == 'SRM':
#                editable = el



        # print editable
        # print editable.attrib
        base = editable.attrib['base']
        # print base
        newbase = base.replace('esg2-sdnl1.ccs.ornl.gov', 'esg.ccs.ornl.gov')
        editable.attrib['base'] = newbase

        X.write(sys.stdout)

    pass
    

# ---------------------------------------------------------------------------
toolframe.tf_launch("xml")
