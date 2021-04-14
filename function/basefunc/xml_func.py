# -*- coding: utf-8 -*-

'''
读取xml文件数据
'''

from xml.etree import ElementTree as ET

tree = ET.parse('../data/data-text.xml')
root = tree.getroot()
data = root.find('Data')
all_data = []

for observation in data:
    for item in observation:
        if item is not None:
            lookup_key = item.attrib.keys()
            record = {}
            for key in lookup_key:
                if key == 'Numeric':
                    rec_key = 'NUMERIC'
                    rec_value = item.attrib['Numeric']
                else:
                    rec_key = item.attrib[key]
                    rec_value = item.attrib['Code']
                record[rec_key] = rec_value
        all_data.append(record)
print (all_data)
