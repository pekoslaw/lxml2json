# -*- coding: utf-8 -*-
from pprint import pprint

from lxml2json import lxml_to_dict
from lxml import etree as ET
from lxmlwrapper import E

elem = E('resp', status=1)
elem.append( E('lalla').add('e') )
elem.append( E('lalla').add('f') )
elem.append( E('lalla').add( E('chuj') ) )
elem.append( E('lalla', hidden=0,text1='a').add('g') )
elem.append( E('lalla3', hidden=0).add('g') )

print ET.tostring(elem,pretty_print=True)
#<resp status="1">
#  <lalla>e</lalla>
#  <lalla>f</lalla>
#  <lalla>
#    <chuj/>
#  </lalla>
#  <lalla hidden="0" text1="a">g</lalla>
#  <lalla3 hidden="0">g</lalla3>
#</resp>

pprint( lxml_to_dict(elem), width=40 )
#{'resp': {'lalla': [{'text': 'e'},
#                    {'text': 'f'},
#                    {'chuj': [{}]},
#                    {'hidden': '0',
#                     'text': 'g',
#                     'text1': 'a'}],
#          'lalla3': [{'hidden': '0',
#                      'text': 'g'}],
#          'status': '1'}}
