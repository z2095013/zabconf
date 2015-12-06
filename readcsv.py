# -*- coding: utf-8 -*-
import csv

class Readcsv:

#  def __init__(self):
#      print('Hello!')
    def csvread(self):
        csvfile = 'test.csv'
        file = open(csvfile, 'r')
        datalist = csv.DictReader(file)
        for data in datalist:
            for k, v in data:

                try:
                    host = data['host']
                    ip = data['ip']
                    group = data['group']
                    template = data['template']
                    application = data['application']
                    item = ['item']
                    trigger = ['trigger']
                    graph = ['graph']
                    graph_item = ['graph_item']
                except KeyError:
                    pass
        file.close()



if __name__ == "__main__":
    import sys, csv
    try:
        csvfile = sys.argv[1]
        Readcsv()
    except IndexError:
        print 'csvファイルを指定してください。'
