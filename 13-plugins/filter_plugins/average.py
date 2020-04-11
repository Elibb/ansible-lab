#!/usr/bin/env python

def average(list):

    return sum(list) / float(len(list))

class FilterModule(object):

    def filters(self):
        return {
            'avg': average
        }
