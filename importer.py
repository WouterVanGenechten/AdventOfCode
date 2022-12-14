#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#general import module

def read_lines(filename):  
    """read individual lines and store them as strings in a list"""
    file1 = open(filename, 'r')
    Lines = file1.read().splitlines()
    return Lines

def read_splitwithinline(filename, splitarg):
    """SUBsplit the lines further into lists according to the splitarguments"""
    file1 = open(filename, 'r')
    Lines = file1.read().splitlines()
    splitted = []
    for line in Lines:
        splitfurther = line.split(splitarg)
        splitted.append(splitfurther)
    return splitted


def read_divideemptyline(filename, splitarg=""):
    """split the lines, then divide according to emptyline"""
    lines = open(filename).readlines()
    groupedlines = []
    temp =[]
    for i in range(len(lines)):
        if lines[i].strip() == splitarg or len(lines) == i+1:
            groupedlines.append(temp)
            temp = []
        else:
            temp.append(lines[i].strip())
    return groupedlines
