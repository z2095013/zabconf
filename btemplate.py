# -*- coding: utf-8 -*-
# テンプレート作成
from datetime import datetime,date
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, parse, ElementTree
from xml.dom import minidom

class TemplateB:
#    group,template,trigger,graph
#  def __init__(self):
#      print('Hello!')
    def main(self):
        # 作成日
        date = str(datetime.today()).split('.')[0]
        day = date.split(' ')[0]
        time = 'T' + date.split(' ')[1] + 'Z'
        # print day + time

        # ルート
        zabbix = Element('zabbix_export')

        # バージョン
        version = SubElement(zabbix, 'version')
        version.text = '2.0'

        # 日付
        date = SubElement(zabbix, 'date')
        date.text = day + time

        # グループ
        groups = SubElement(zabbix, 'groups')
        group = SubElement(groups, 'group')
        groupname = SubElement(group, 'name')
        groupname.text = 'AAA'

        # テンプレート
        templates = SubElement(zabbix, 'templates')
        template = SubElement(templates, 'template')
        templatechild = SubElement(template, 'template')
        templatechild.text = 'BBB'

        #templatechild.set = ('discription', 'BBB')
        templatename = SubElement(template, 'name')
        templatename.text = 'CCC'

        templategroups = SubElement(template, 'groups')
        templategroup = SubElement(templategroups, 'group')
        templategroupname = SubElement(templategroup, 'name')
        templategroupname.text = 'AAA'

#        while True:
#            templategroups = SubElement(template, 'groups')
#            templategroup = SubElement(templategroups, 'group')
#            templategroupname = SubElement(templategroup, 'name')
#            templategroupname.text = 'AAA'



        # xmlファイル書き込み
        #tree = ElementTree(zabbix)
        #tree.write(xmlfile, 'UTF-8', 'True') #改行なし

        f = open('test.xml', 'w')
        tree = minidom.parseString(tostring(zabbix)).toprettyxml()
        print tree
        f.write(tree)
        f.flush()
        f.close()
