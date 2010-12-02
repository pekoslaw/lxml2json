# -*- coding: utf-8 -*-
from simplejson import dumps 


def lxml_to_dict(etree, text_attribute_name='text', tail_attribute_name='tail', show_element_tag=True):
    res = {}
    if show_element_tag:
        res[etree.tag] = {}
        elem = res[etree.tag]
    else:
        elem = res
	
    for k in etree.keys():
        assert k <> text_attribute_name, 'You cant use %s attribute in xml, or change text_attribute_name' % text_attribute_name
        assert k <> tail_attribute_name, 'You cant use %s attribute in xml, or change tail_attribute_name' % text_attribute_name
        elem[k]=etree.attrib[k]
    if etree.text:
        elem[text_attribute_name]=etree.text
    if etree.tail:
        elem[tail_attribute_name]=etree.text
    for c in etree.getchildren():
        if elem.has_key(c.tag):
            elem[c.tag].append( lxml_to_dict(c,text_attribute_name,tail_attribute_name,False) )
        else:
            elem[c.tag] =[ lxml_to_dict(c,text_attribute_name,tail_attribute_name,False) ]
    return res

def lxml_to_json(etree):
    d = lxml_to_dict(etree)
    return dumps(lxml_to_dict(elem))



